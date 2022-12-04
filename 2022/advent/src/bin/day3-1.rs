use advent::lib;
use std::io;
use std::collections::HashSet;

fn main() -> Result<(), io::Error>{
    let mut sum: u32 = 0;
    
    let lines = lib::read_lines("./in/day3input.txt").unwrap();
    for line in lines{
        let ip = line?;
        let mid: usize = ip.len()/2;
        let mut first_half = HashSet::<char>::new();
        let mut second_half = HashSet::<char>::new();
        for (p, c) in ip.chars().enumerate(){
            if p < mid{
                first_half.insert(c);
            }else{
                second_half.insert(c);
            }
        }
        for c in first_half.intersection(&second_half){
            let ascii_val: u32 = *c as u32;
            let value: u32;
            if c.is_uppercase(){
                value = ascii_val - 38;
            }else{
                value = ascii_val - 96;
            }
            sum += value;
        }
    }
    println!("{}", sum);
    Ok(())
}