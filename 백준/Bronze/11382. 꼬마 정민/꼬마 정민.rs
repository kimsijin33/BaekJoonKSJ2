use std::io;
fn main() {
    let mut input = String::new();
    
    io::stdin()
        .read_line(&mut input)
        .unwrap();
    
    let result: i64 = input
        .split_whitespace()
        .map(|s| s.parse::<i64>().unwrap())
        .sum();
    println!("{}", result);
}