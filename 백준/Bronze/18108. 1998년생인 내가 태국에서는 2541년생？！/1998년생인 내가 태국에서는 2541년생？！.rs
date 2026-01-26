use std::io;
fn main() {
    let mut input = String::new();
    
    io::stdin()
        .read_line(&mut input)
        .expect("입력을 읽지 못했습니다.");
    
   let number: i32 = input
        .trim()
        .parse()
        .expect("숫자가 아닙니다.");
 
    let result = number - 543;
    
    println!("{}",result);
}