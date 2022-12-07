use std::{vec};

use advent::lib;

fn make_stacks(col: usize) -> Vec<Vec<char>> {
    let mut ret_vec: Vec<Vec<char>> = Vec::<Vec<char>>::new();
    for _ in 0..col{
        ret_vec.push(vec![]);
    }
    ret_vec
}

fn main(){
    let lines: Vec<String> = lib::read_lines_vec("./in/day5input.txt");
    let num_col = (lines[0].len()+1) / 4;
    let mut stacks = make_stacks(num_col);
    for line in &lines{
        if line[0..2].to_string() == " 1"{
            break
        }
        for p in 0..num_col{
            let c: char = line.as_bytes()[(4*p)+1] as char;
            if c != ' '{
                stacks[p].insert(0, c);
            }
        }
    }

    for line in &lines{
        if line.len() > 0 && line[0..5].to_string() == "move "{
            let mid_split: Vec<&str> = line.split(" from ").collect();
            let dir_split: Vec<&str> = mid_split[1].split(" to ").collect();
            let quantity: usize = mid_split[0][5.. ].parse().unwrap();
            let from: usize = dir_split[0].parse().unwrap();
            let to: usize = dir_split[1].parse().unwrap();
            let mut save_stack = Vec::<char>::new();
            for _ in 0..quantity{
                let lifted: char = stacks[from-1].pop().unwrap();
                save_stack.insert(0, lifted);
            }
            for c in save_stack{
                stacks[to-1].push(c);
            }
        }
    }
    for stack in stacks{
        print!("{}", stack.last().unwrap());
    }
}