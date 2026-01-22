use std::io;
fn main() {
    let mut input = String::new();
    
    io::stdin()
        .read_line(&mut input)
        .expect("입력을 읽지 못했습니다.");
    
   let sum: i32 = input
        .split_whitespace()
        .map(|s| s.parse::<i32>().expect("숫자가 아닙니다."))
        .sum();
    
    println!("{}",sum);
}