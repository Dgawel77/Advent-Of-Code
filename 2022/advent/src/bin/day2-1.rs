use advent::lib;

fn main(){
    let mut total = 0;
    if let Ok(lines) = lib::read_lines("./in/day2input.txt"){
        for line in lines {
            if let Ok(ip) = line {
                let mut sum = 0;
                let opponent_move = ip.chars().nth(0).unwrap();
                let my_move = ip.chars().nth(2).unwrap();
                // X rock
                // y paper
                // z scissors
                match my_move{
                    'X' => sum += 1,
                    'Y' => sum += 2,
                    'Z' => sum += 3,
                    _ => println!("wrong"),
                }
                // A rock
                // B paper
                // C scissors

                // win  +6
                // draw +3
                // loss +0
                match (opponent_move, my_move){
                    ('A', 'X') => sum += 3,
                    ('A', 'Y') => sum += 6,
                    ('A', 'Z') => sum += 0,
                    ('B', 'X') => sum += 0,
                    ('B', 'Y') => sum += 3,
                    ('B', 'Z') => sum += 6,
                    ('C', 'X') => sum += 6,
                    ('C', 'Y') => sum += 0,
                    ('C', 'Z') => sum += 3,
                    _ => println!("{}, {}", opponent_move, my_move),
                }
                total += sum;
            }
        }
    }
    println!("{}", total);
}