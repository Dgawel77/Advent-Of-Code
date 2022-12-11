use advent::lib;

fn main(){
    let lines: Vec<Vec<u32>> = lib::read_string("./in/day8input.txt")
        .lines()
        .map(|x| x.chars()
            .map(|x| x.to_digit(10).unwrap()).collect::<Vec<u32>>()
        )
        .collect();
    let length: usize = lines.len();
    let width: usize = lines[0].len();
    let r = 1;
    let c = 2;
    let mut _scenic_score: usize = 0;
    let i = lines[r][c];
    let left_count = lines[r][0..c].iter().rev().take_while(|&&x| x < i).count() + 1;
    let right_count = lines[r][c+1..width].iter().take_while(|&&x| x < i).count();
    
    let top_count = lines[0..r].iter().rev().take_while(|x_v| x_v[c] < i).count() + 1;
    let bottom_count = lines[r+1..length].iter().take_while(|x_v| x_v[c] < i).count();

    let tmp_scenic_score = left_count * right_count * top_count * bottom_count;
    _scenic_score = _scenic_score.max(tmp_scenic_score);
    print!("{tmp_scenic_score} ");

    dbg!(left_count, right_count, top_count, bottom_count);

    //match left_vis || right_vis || top_vis || bottom_vis{
    //    true => print!("T "),
    //    false => print!("F "),
    //}

    // if left_vis || right_vis || top_vis || bottom_vis{
    //     sum += 1;
    // }
       
}