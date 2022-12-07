use advent::lib;
use std::collections::HashSet;

fn main(){
    let lines: Vec<String> = lib::read_lines_vec("./in/day6input.txt");
    for line in lines{
        for p in 0..line.len()-13{
            let mut chars_set = HashSet::<char>::new();
            for c in line[p..p+14].to_string().chars(){
                chars_set.insert(c);
            }
            if chars_set.len() == 14{
                println!("{}", 14+p);
                break
            }
        }
    }
}