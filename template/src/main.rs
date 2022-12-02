#![feature(fs_try_exists)]
use template::lib;
extern crate strfmt;
use strfmt::strfmt;
use std::collections::HashMap;

use std::env;
use std::fs;
use std::error::Error;

fn del_file(day: String) -> Result<(), Box<dyn Error>>{
    fs::remove_file(format!("C:/Users/David Gawel/OneDrive/Programs/Advent-Of-Code/2022/advent/src/bin/day{}-{}.rs", day, 1)).ok();
    fs::remove_file(format!("C:/Users/David Gawel/OneDrive/Programs/Advent-Of-Code/2022/advent/src/bin/day{}-{}.rs", day, 2)).ok();
    fs::remove_file(format!("C:/Users/David Gawel/OneDrive/Programs/Advent-Of-Code/2022/advent/in/day{}input.txt", day)).ok();
    Ok(())
}

fn make_file(day: String) -> Result<(), Box<dyn Error>>{
    if fs::try_exists(format!("C:/Users/David Gawel/OneDrive/Programs/Advent-Of-Code/2022/advent/src/bin/day{}-{}.rs", day, 1).to_string()).unwrap(){
        //println!("Day {} already exits!", day);
        return Err(format!("Day {} already exits!", day).into())
    }
    
    let template_string: String = lib::read_string("C:/Users/David Gawel/OneDrive/Programs/Advent-Of-Code/template/src/template.txt");

    let mut vars = HashMap::new();
    vars.insert("DAY".to_string(), day.to_string());

    fs::write(format!("C:/Users/David Gawel/OneDrive/Programs/Advent-Of-Code/2022/advent/src/bin/day{}-{}.rs", day, 1).to_string(), 
                strfmt(&template_string, &vars).unwrap()).expect("unable to write bin_file");
    fs::write(format!("C:/Users/David Gawel/OneDrive/Programs/Advent-Of-Code/2022/advent/src/bin/day{}-{}.rs", day, 2).to_string(), 
                strfmt(&template_string, &vars).unwrap()).expect("unable to write bin_file");
    fs::write(format!("C:/Users/David Gawel/OneDrive/Programs/Advent-Of-Code/2022/advent/in/day{}input.txt", day).to_string(), 
                "").expect("unable to write bin_file");
    Ok(())
}

fn main() -> Result<(), Box<dyn Error>>{
    if env::args().len() == 1{
        return Err("No day specified in the command line".into())
    }
    match env::args().len(){
        1 => return Err("No day specified in the command line".into()),
        2 => {
            let args: Vec<String> = env::args().skip(1).collect();
            let day: &str = &args[0];
            return make_file(day.to_string());
        }
        3 => {
            let args: Vec<String> = env::args().skip(1).collect();
            let day: &str = &args[0];
            let cmd: &str = &args[1];
            match cmd {
                "--del" => return del_file(day.to_string()),
                "--add" => return make_file(day.to_string()),
                _ => return Err("Not a command".into()),
            }
        }
        _ => Err("Unknown specifications".into()),
    }
}