use std::io;
fn main() {
    let mut input = String::new();
    
    io::stdin()
        .read_line(&mut input)
        .expect("입력을 읽지 못했습니다.");
    
   let numbers: Vec<i32> = input
        .split_whitespace()
        .map(|s| s.parse::<i32>().expect("숫자가 아닙니다."))
        .collect();
    let result = (numbers[0] + numbers[1]) % numbers[2];
    let result1 = ((numbers[0] % numbers[2]) + (numbers[1]%numbers[2])) % numbers[2];
    let result2 = (numbers[0] * numbers[1]) % numbers[2];
    let result3 = ((numbers[0] % numbers[2]) * (numbers[1]%numbers[2])) % numbers[2];
    println!("{}",result);
    println!("{}",result1);
    println!("{}",result2);
    println!("{}",result3);

    
    //console.log((num1+num2)%num3);
    //console.log(((num1%num3) + (num2%num3))%num3);
    //console.log((num1*num2)%num3);
    //console.log(((num1%num3) * (num2%num3))%num3);
}