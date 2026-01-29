/*use std::io;
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    
    io::stdin()
        .read_line(&mut input)
        .expect("입력을 읽지 못했습니다.");
    
   let numbers: Vec<i32> = input
        .split_whitespace()
        .map(|s| s.parse::<i32>().expect("숫자가 아닙니다."))
        .collect();
    
    let result = numbers.into_iter().reduce(|acc, x| acc + x).unwrap();
    println!("{}",result);    
}

use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    // 1. read_to_string으로 입력 전체를 읽어 모든 숫자를 가져옵니다.
    io::stdin().read_to_string(&mut input).unwrap();
    
    let result: i32 = input
        .split_whitespace()
        .map(|s| s.parse::<i32>().unwrap_or(0)) // 숫자가 아니면 0으로 처리
        .fold(0, |acc, x| acc + x);             // 초기값 0부터 시작해서 안전함

    println!("{}", result);
}*/

use std::io;

fn main() {
    let mut input = String::new();
    
    // 한 줄을 읽어옵니다.
    io::stdin()
        .read_line(&mut input)
        .unwrap();
    
    // i32 대신 i64를 사용하여 큰 숫자도 처리할 수 있게 합니다.
    let result: i64 = input
        .split_whitespace()
        .map(|s| s.parse::<i64>().unwrap())
        .sum(); // fold(0, |acc, x| acc + x)와 동일하지만 더 간결합니다.

    println!("{}", result);
}
