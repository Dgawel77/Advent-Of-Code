// Solution based off of chris biscardi's Solution
// https://www.youtube.com/watch?v=t9OQ3ca8OWk
#![feature(iter_intersperse)]
use std::collections::BTreeMap;

use advent::lib;
use nom::{*, 
    bytes::complete::{tag, is_a}, 
    branch::alt, 
    character::complete::{alpha1, newline},
    multi::{separated_list1}, sequence::separated_pair,};

#[derive(Debug)]
enum Operation<'a>{
    Cd(Cd<'a>),
    Ls(Vec<Files<'a>>)
}

#[derive(Debug)]
enum Cd<'a>{
    Root,
    Up,
    Down(&'a str),
}

#[derive(Debug)]
enum Files<'a>{
    File {size: u32, name: &'a str },
    Dir (&'a str),
}

fn file(input: &str) -> IResult<&str, Files>{
    let (input, (size, name)) = separated_pair(
        nom::character::complete::u32,
        tag(" "),
        is_a("qwfpgjluyarstdhneiozxcvbkm."),
    )(input)?;
    Ok((input, Files::File{size, name}))
}

fn directory(input: &str) -> IResult<&str, Files>{
    let (input, _) = tag("dir ")(input)?;
    let (input, name) = alpha1(input)?;
    Ok((input, Files::Dir(name)))
}

fn ls(input: &str) -> IResult<&str, Operation>{
    let (input, _) = tag("$ ls")(input)?;
    let (input, _) = newline(input)?;
    let (input, files) = separated_list1(
        newline, 
        alt((file, directory))
    )(input)?;
    Ok((input, Operation::Ls(files)))
}

fn cd(input: &str) -> IResult<&str, Operation>{
    let (input, _) = tag("$ cd ")(input)?;
    let (input, action) = alt((tag(".."), alpha1, tag("/")))(input)?;
    let op = match action {
        ".." => Operation::Cd(Cd::Up),
        "/" => Operation::Cd(Cd::Root),
        name => Operation::Cd(Cd::Down(name)),
    };
    Ok((input, op))
}

fn commands(input: &str) -> IResult<&str, Vec<Operation>>{
    let (input, cmd) = separated_list1(newline, alt((ls, cd)))(input)?;
    Ok((input, cmd))
}

#[derive(Debug)]
#[allow(dead_code)]
struct File<'a> {
    size: u32,
    name: &'a str,
}

fn main(){
    let lines = lib::read_string("./in/day7input.txt");
    let cmd = commands(lines.as_str()).unwrap().1;
    let mut context: Vec<&str> = vec![];
    let mut directories: BTreeMap<String, Vec<File>> =BTreeMap::new();

    for command in cmd.iter(){
        match command {
            Operation::Cd(Cd::Root) => {
                context.push("");
            },
            Operation::Cd(Cd::Up) => {
                context.pop();
            },
            Operation::Cd(Cd::Down(name)) => {
                context.push(name);
            },
            Operation::Ls(files) => {
                directories.entry(
                    context
                        .iter()
                        .cloned()
                        .intersperse("/")
                        .collect::<String>(),
                ).or_insert(vec![]);
                for file in files.iter(){
                    match file{
                        Files::File { size, name } => {
                            directories.entry(
                                context
                                    .iter()
                                    .cloned()
                                    .intersperse("/")
                                    .collect::<String>(),
                            ).and_modify(|vec| vec.push(
                                File {
                                    size: *size,
                                    name,
                                }
                            ));
                        }
                        Files::Dir(_) => ()
                    }
                }
            }
        } 
    }

    //dbg!(directories);
    let mut sizes: BTreeMap<String, u32> = BTreeMap::new();
    for (path, files) in directories.iter(){
        let dirs = path.split("/").collect::<Vec<&str>>();
        let size: u32 = files
            .iter()
            .map(|File {size, ..}| size)
            .sum();
        for i in 0..dirs.len(){
            sizes
                .entry(
                    (&dirs[0..=i])
                        .iter()
                        .cloned()
                        .intersperse("/")
                        .collect::<String>()
                )
                .and_modify(|v| *v += size)
                .or_insert(size);
        }
    }

    let unused_space = 70_000_000 - sizes[""];
    let target = 30_000_000 - unused_space;
    let answer: u32 = sizes
        .iter()
        .filter(|(_, &size)| size > target)
        .map(|(_, &size)| size)
        .min()
        .unwrap();
    println!("{}", answer);
}