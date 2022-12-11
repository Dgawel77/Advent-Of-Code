use advent::lib;
use nom::{multi::separated_list1, character::complete::newline, branch::alt, IResult, bytes::complete::tag};

#[derive(Debug, Clone, Copy)]
enum Command{
    Noop(),
    Addx(i32),
}

fn noop(input: &str) -> IResult<&str, Command>{
    let (input, _) = tag("noop")(input)?;
    Ok((input, Command::Noop()))
}

fn addx(input: &str) -> IResult<&str, Command>{
    let (input, _) = tag("addx ")(input)?;
    let (input, amount) = nom::character::complete::i32(input)?;
    Ok((input, Command::Addx(amount)))
}

fn commands(input: &str) -> IResult<&str, Vec<Command>>{
    let (input, cmd) = separated_list1(newline, alt((noop, addx)))(input)?;
    Ok((input, cmd))
}


fn main(){
    let lines = lib::read_string("./in/day10input.txt");
    let cmd_v = commands(lines.as_str()).unwrap().1;
    let cycle_count = 220;
    let mut p = 0;
    let mut register = 1;
    let mut op_stack: Vec<(i32, u32)> = Vec::new();
    let mut strength = 0;
    for cycle in 1..=cycle_count{
        if op_stack.is_empty(){
            if p < cmd_v.len(){
                let cmd: Command = cmd_v[p];
                p += 1;
                match cmd{
                    Command::Noop() => {op_stack.push((0,1));},
                    Command::Addx(instr) =>  {op_stack.push((instr,2));}
                }
            }
        }
        if vec![20, 60, 100, 140, 180, 220].contains(&cycle){
            strength += cycle * register;
            //print!("cycle {}: {}\n", cycle, register);
        }
        if !op_stack.is_empty() {
            op_stack[0] = (op_stack[0].0, op_stack[0].1-1);
            if op_stack[0].1 == 0{
                register += op_stack[0].0;
                //println!("{cycle} adding {}", op_stack[0].0);
                op_stack.pop();
            }
        }
    }
    println!("{strength}");
}