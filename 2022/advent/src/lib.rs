pub mod lib{
    use std::fs::File;
    use std::io::{self, BufRead, Read};
    use std::path::Path;

    pub fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
    where P: AsRef<Path>, {
        let file = File::open(filename)?;
        Ok(io::BufReader::new(file).lines())
    }

    pub fn read_lines_vec<P>(filename: P) -> Vec<String>
    where P: AsRef<Path>, {
        let file = File::open(filename).expect("No Such File Name");
        io::BufReader::new(file).lines().map(|l| l.expect("Could Not Parse Line")).collect()
    }

    pub fn read_string<P>(filename: P) -> String
    where P: AsRef<Path>, {
        let mut file = File::open(filename).expect("File not found");
        let mut data = String::new();
        file.read_to_string(&mut data).expect("Error while reading file");
        data.replace("\r\n", "\n")
    }
}