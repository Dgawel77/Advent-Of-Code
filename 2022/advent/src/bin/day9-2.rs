#![allow(unused_assignments, dead_code)]
use std::collections::HashSet;

use advent::lib;

enum Move{
    Left,
    Right,
    Up,
    Down,
}

struct Board{
    tail_visited: HashSet<(i32, i32)>,
    knots: Vec<(i32, i32)>,
}

impl Board{
    pub fn new() -> Self{
        let mut tail_visited_tmp = HashSet::<(i32, i32)>::new();
        tail_visited_tmp.insert((0,0));
        let mut knots_tmp = vec![];
        for _ in 0..10{
            knots_tmp.push((0,0));
        }
        Board{
            tail_visited: tail_visited_tmp,
            knots: knots_tmp,
        }
    }
    
    pub fn move_dir(self: &mut Self, dir: &Move){
        match dir{
            Move::Down => self.knots[0] = (self.knots[0].0, self.knots[0].1-1),
            Move::Up => self.knots[0] = (self.knots[0].0, self.knots[0].1+1),
            Move::Left => self.knots[0] = (self.knots[0].0-1, self.knots[0].1),
            Move::Right => self.knots[0] = (self.knots[0].0+1, self.knots[0].1),
        }

        for x in 0..(self.knots.len()-1){
            self.move_dir_helper(x, x+1);
        }
    }

    pub fn move_dir_helper(self: &mut Self, ahead: usize, before: usize){
        let head = self.knots[ahead];
        let tail = self.knots[before];
        
        let dif_x: i32 = head.0 - tail.0;
        let dif_y: i32 = head.1 - tail.1;
        
        let mut new_tail_x: i32 = tail.0;
        let mut new_tail_y: i32 = tail.1;
        match (dif_x, dif_y){
            //diagonal cases
            (2, 2) => {new_tail_x += 1; new_tail_y += 1;},
            (2, -2) => {new_tail_x += 1; new_tail_y += -1;},
            (-2, 2) => {new_tail_x += -1; new_tail_y += 1;},
            (-2, -2) => {new_tail_x += -1; new_tail_y += -1;},
            //regular cases
            (2, _) => {new_tail_x = head.0-1; new_tail_y = head.1;},
            (-2, _) => {new_tail_x = head.0+1; new_tail_y = head.1;},
            (_, 2) => {new_tail_x = head.0; new_tail_y = head.1-1;},
            (_, -2) => {new_tail_x = head.0; new_tail_y = head.1+1;},
            (_, _) => {},
        }
        self.knots[before] = (new_tail_x, new_tail_y);
        if before == 9{
            self.tail_visited.insert(self.knots[before]);
        }
    }

    pub fn print(self: &Self){
        for y in (-11..=20).rev(){
            for x in -11..=20{
                if (x, y) == (0,0){
                    print!("S");
                } else if self.knots.contains(&(x,y)){
                    let position = self.knots.iter().position(|&i| i == (x,y)).unwrap();
                    if position == 0{
                        print!("H");
                    } else {
                        print!("{}", position);
                    }
                }else{
                    print!(".");
                }
            }
            println!();
        }
        println!();
    }
}

fn main(){
    let lines: Vec<String> = lib::read_lines_vec("./in/day9input.txt");
    let mut board: Board = Board::new();    
    for line in lines{
        let command: Vec<&str> = line.split(" ").collect();
        let distance: u32 = command[1].parse().unwrap();
        let dir: Move = match command[0]{
            "U" => Move::Up,
            "D" => Move::Down,
            "L" => Move::Left,
            "R" => Move::Right,
            _ => unreachable!("Invalid move command"),
        };
        for _ in 0..distance{
            board.move_dir(&dir);
        }
        //board.print();
    }
    println!("{}", board.tail_visited.len());
}