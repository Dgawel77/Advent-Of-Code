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
    
    let mut scenic_score: usize = 0;
    for r in 0..width{
        for c in 0..length{
            if (r==0 || r==length-1) || (c==0 || c==width-1){
                scenic_score = scenic_score.max(0);
                continue;
            }
            // tried to do this with iterators but it was hard to terminate the loop after 
            // keeping the element
            

            let this_tree = lines[r][c];
            let mut left_count: usize = 0;
            for &other_tree in lines[r][0..c].iter().rev(){
                left_count += 1;
                if other_tree >= this_tree{ break; } 
            }

            let mut right_count: usize = 0;
            for &other_tree in lines[r][c+1..width].iter(){
                right_count += 1;
                if other_tree >= this_tree{ break; } 
            }

            let mut top_count: usize = 0;
            for other_tree_v in lines[0..r].iter().rev(){
                top_count += 1;
                if other_tree_v[c] >= this_tree { break; } 
            }
            
            let mut bottom_count: usize = 0;
            for other_tree_v in lines[r+1..length].iter(){
                bottom_count += 1;
                if other_tree_v[c] >= this_tree { break; } 
            }

            let tmp_scenic_score = left_count * right_count * top_count * bottom_count;
            scenic_score = scenic_score.max(tmp_scenic_score);
        }
    }
    println!("{}", scenic_score);
}
