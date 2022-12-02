use advent::lib;
use std::cmp;

fn main(){
    let mut max: Vec::<u32> = vec!();
    let mut sum:u32 = 0;
    if let Ok(lines) = lib::read_lines("./in/day1input.txt"){
        for line in lines {
            if let Ok(ip) = line {
                if ip == ""{
                    max.push(sum);
                    sum = 0;
                }else{
                    sum += ip.parse::<u32>().unwrap();
                }
            }
        }
    }
    max.sort();
    let vec_len = max.len();
    println!("{}", max[vec_len-1] + max[vec_len-2] + max[vec_len-3]);
}