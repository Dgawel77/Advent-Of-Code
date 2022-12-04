use advent::lib;
use std::io;

fn main() -> Result<(), io::Error>{
    let lines: Vec<String> = lib::read_lines_vec("./in/day4input.txt");
    let mut sum = 0;
    for line in lines{
        let parts: Vec<&str> = line.split(",").collect();
        let first: Vec<&str>= parts[0].split("-").collect();
        let second: Vec<&str>= parts[1].split("-").collect();
        let range1: std::ops::RangeInclusive<i32> = first[0].parse().unwrap() ..=first[1].parse().unwrap();
        let range2: std::ops::RangeInclusive<i32> = second[0].parse().unwrap() ..=second[1].parse().unwrap();    
        if range1.contains(range2.start()) && range1.contains(range2.end()){
            sum += 1;
            continue;
        }
        if range2.contains(range1.start()) && range2.contains(range1.end()){
            sum += 1;
            continue;
        }
    }
    println!("{}", sum);
    Ok(())
}