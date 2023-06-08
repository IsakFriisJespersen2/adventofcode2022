use std::fs;

fn main() {
    let file_path = "data.txt";
    println!("In file {}", file_path);

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");
    println!("Hello, world!");

    for line in contents.lines()  {
        println!("{}", line);
        let cargo_1: &str = &line[0..line.len()/2];
        let cargo_2: &str = &line[line.len()/2..];

        println!("cargo_1: {}", cargo_1);
        println!("cargo_2: {}", cargo_2);

    }
}

