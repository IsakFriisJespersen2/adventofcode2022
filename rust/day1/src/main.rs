use std::fs;

fn main() {
    let file_path = "./data.txt";
    println!("In file {}", file_path);

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let mut current_calories: i32 = 0;
    let mut all_calories = Vec::new();

    for line in contents.lines() {
        if line == "" {
            all_calories.push(current_calories);
            current_calories = 0;
            continue;
        }
        let calories: i32 = line.parse().unwrap();
        current_calories += calories;
    }

    println!("Max calories: {}", all_calories.iter().max().unwrap());

    all_calories.sort();
    all_calories.reverse();
    let first_three = &all_calories[0..3];
    let sum = first_three.iter().sum::<i32>();

    println!("Sum of first three elements: {}", sum);

}
