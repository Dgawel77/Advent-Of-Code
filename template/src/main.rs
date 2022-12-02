#![feature(fs_try_exists)]
use template::lib;
extern crate strfmt;
use strfmt::strfmt;
use std::collections::HashMap;

use std::env;
use std::fs;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>>{
    if env::args().len() == 1{
        return Err("No day specified in the command line".into())
    }
    
    let args: Vec<String> = env::args().skip(1).collect();
    let day: &str = &args[0];
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