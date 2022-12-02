use advent::lib;
use std::cmp;
fn main(){
    let mut max:u32 = 0;
    let mut sum:u32 = 0;
    if let Ok(lines) = lib::read_lines("./in/day1-1.txt"){
        for line in lines {
            if let Ok(ip) = line {
                if ip == ""{
                    max = cmp::max(sum, max);
                    sum = 0;
                }else{
                    sum += ip.parse::<u32>().unwrap();
                }
            }
        }
    }
    println!("{}", max);
}