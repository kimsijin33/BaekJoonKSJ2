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
    
   let numbers: Vec<i32> = input
        .split_whitespace()
        .map(|s| s.parse::<i32>().expect("숫자가 아닙니다."))
        .collect();
    let result = numbers.into_iter().reduce(|acc, x| acc - x).unwrap();
    println!("{}",result);

   let numbers2: Vec<i32> = input
        .split_whitespace()
        .map(|s| s.parse::<i32>().expect("숫자가 아닙니다."))
        .collect();
    let result2 = numbers2.into_iter().reduce(|acc, x| acc * x).unwrap();
    println!("{}",result2);    

   let numbers3: Vec<i32> = input
        .split_whitespace()
        .map(|s| s.parse::<i32>().expect("숫자가 아닙니다."))
        .collect();
    let result3 = numbers3.into_iter().reduce(|acc, x| acc / x).unwrap();
    println!("{}",result3);

   let numbers4: Vec<i32> = input
        .split_whitespace()
        .map(|s| s.parse::<i32>().expect("숫자가 아닙니다."))
        .collect();
    let result4 = numbers4.into_iter().reduce(|acc, x| acc % x).unwrap();
    println!("{}",result4);    
}