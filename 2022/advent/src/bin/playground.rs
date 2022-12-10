use advent::lib;

fn main(){
    let lines: Vec<Vec<u32>> = lib::read_string("./in/day8input.txt")
        .lines()
        .map(|x| x.chars()
            .map(|x| x.to_digit(10).unwrap()).collect::<Vec<u32>>()
        )
        .collect();
    
    let r = 1;
    let c = 2;
    let this_height = lines[r][c];
    let left_vis = lines[r][0..c].iter().all(|&other_height| other_height < this_height);
    let right_vis = lines[r][c+1..width].iter().all(|&other_height| other_height < this_height);
    
    let top_vis = lines[0..r].iter().all(|other_height_vec| other_height_vec[c] < this_height);
    let bottom_vis = lines[r+1..length].iter().all(|other_height_vec| other_height_vec[c] < this_height);

    dbg!(r, c, this_height, left_vis, right_vis, top_vis, bottom_vis);

    //match left_vis || right_vis || top_vis || bottom_vis{
    //    true => print!("T "),
    //    false => print!("F "),
    //}

    // if left_vis || right_vis || top_vis || bottom_vis{
    //     sum += 1;
    // }
       
}