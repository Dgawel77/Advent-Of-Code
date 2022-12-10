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
    
    let mut sum: u32 = 0;
    for r in 0..width{
        for c in 0..length{
            let this_height = lines[r][c];
            let left_vis = lines[r][0..c].iter().all(|&other_height| other_height < this_height);
            let right_vis = lines[r][c+1..width].iter().all(|&other_height| other_height < this_height);
            
            let top_vis = lines[0..r].iter().all(|other_height_vec| other_height_vec[c] < this_height);
            let bottom_vis = lines[r+1..length].iter().all(|other_height_vec| other_height_vec[c] < this_height);

            if left_vis || right_vis || top_vis || bottom_vis{
                sum += 1;
            }
        }
    }
    
    println!("{}", sum);
}