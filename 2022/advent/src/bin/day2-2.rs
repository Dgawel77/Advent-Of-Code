use advent::lib;
use std::io;

fn main() -> Result<(), io::Error>{
    let mut total: i32 = 0;

    let lines = lib::read_lines("./in/day2input.txt").unwrap();
    for line in lines{
        let ip = line?;
        let mut sum = 0;
        let opponent_move = ip.chars().nth(0).unwrap();
        let my_move = ip.chars().nth(2).unwrap();
        // X lose
        // y draw
        // z win
        match my_move{
            'X' => sum += 0,
            'Y' => sum += 3,
            'Z' => sum += 6,
            _ => println!("wrong"),
        }
        // A rock +1
        // B paper +2
        // C scissors +3

        // win  +6
        // draw +3
        // loss +0
        // what piece I need to chose based
        match (opponent_move, my_move){
            ('A', 'X') => sum += 3, //scissors
            ('A', 'Y') => sum += 1, //rock
            ('A', 'Z') => sum += 2, //paper
            ('B', 'X') => sum += 1, //rock
            ('B', 'Y') => sum += 2, //paper
            ('B', 'Z') => sum += 3, //scissors
            ('C', 'X') => sum += 2, //paper
            ('C', 'Y') => sum += 3, //scissors
            ('C', 'Z') => sum += 1, //rock
            _ => println!("{}, {}", opponent_move, my_move),
        }
        total += sum;
    }
    println!("{}", total);
    Ok(())
}