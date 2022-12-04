use advent::lib;
use std::io;
use std::collections::HashSet;

fn main() -> Result<(), io::Error>{
    let mut sum: u32 = 0;
    let lines: Vec<String> = lib::read_lines("./in/day3input.txt").unwrap().map(|l| l.expect("Could not parse line")).collect();
    
    for x in (0..lines.len()).step_by(3){
        let one = lines.get(x+0).unwrap();
        let two = lines.get(x+1).unwrap();
        let three = lines.get(x+2).unwrap();

        let mut badge = HashSet::<char>::new();
        for c in one.chars(){
            badge.insert(c);
        }
        badge.retain(|c| two.contains(*c));
        badge.retain(|c| three.contains(*c));
        assert!(badge.len() == 1);
        for c in badge{
            let ascii_val = c as u32;
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