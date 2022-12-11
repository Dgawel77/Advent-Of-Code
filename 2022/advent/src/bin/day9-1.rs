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
    head: (i32, i32),
    tail: (i32, i32),
}

impl Board{
    pub fn new() -> Self{
        let mut tail_visited_tmp = HashSet::<(i32, i32)>::new();
        tail_visited_tmp.insert((0,0));
        Board{
            tail_visited: tail_visited_tmp,
            head: (0,0),
            tail: (0,0),
        }
    }
    
    pub fn move_dir(self: &mut Self, dir: &Move){
        match dir{
            Move::Down => self.head = (self.head.0, self.head.1-1),
            Move::Up => self.head = (self.head.0, self.head.1+1),
            Move::Left => self.head = (self.head.0-1, self.head.1),
            Move::Right => self.head = (self.head.0+1, self.head.1),
        }
        let dif_x: i32 = self.head.0 - self.tail.0;
        let dif_y: i32 = self.head.1 - self.tail.1;
        //dbg!(dif_x, dif_y);
        
        let mut new_tail_x: i32 = 0;
        let mut new_tail_y: i32 = 0;
        let mut change_tail_y: bool = true;

        match dif_x{
            -2 => {
                new_tail_x = self.head.0+1; 
                new_tail_y = self.head.1;
                change_tail_y = false;
            },
            -1 => new_tail_x = self.tail.0,
            0 => new_tail_x = self.tail.0,
            1 => new_tail_x = self.tail.0,
            2 => {
                new_tail_x = self.head.0-1; 
                new_tail_y = self.head.1;
                change_tail_y = false;
            },
            _ => unreachable!("dif_x should be within -2 - 2")
        }
        
        if change_tail_y{
            match dif_y{
                -2 => {new_tail_y = self.head.1+1; new_tail_x = self.head.0},
                -1 => new_tail_y = self.tail.1,
                0 => new_tail_y = self.tail.1,
                1 => new_tail_y = self.tail.1,
                2 => {new_tail_y = self.head.1-1; new_tail_x = self.head.0},
                _ => unreachable!("dif_y should be within -2 - 2")
            }
        }
        self.tail = (new_tail_x, new_tail_y);
        self.tail_visited.insert(self.tail);
    }

    pub fn print(self: &Self){
        for y in (0..=4).rev(){
            for x in 0..=5{
                if (x, y) == (0,0){
                    print!("S");
                } else if (x, y) == self.head{
                    print!("H");
                }else if (x, y) == self.tail{
                    print!("T");
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
            _ => unreachable!("not supposed to happen"),
        };
        for _ in 0..distance{
            board.move_dir(&dir);
            //board.print();
        }
    }
    println!("{}", board.tail_visited.len());
}