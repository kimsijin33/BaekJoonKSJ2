 // fs 모듈을 불러옵니다.
const fs = require('fs');

// /dev/stdin 파일을 읽어와 문자열로 변환한 뒤 공백이나 줄바꿈 기준으로 나눕니다.
const input = fs.readFileSync('/dev/stdin').toString().split(/\s/);

// 입력받은 값은 문자열이므로 숫자로 변환합니다.
const num1 = Number(input[0]);
const num2 = Number(input[1]);
const num3 = Number(input[2]);

// 결과 출력
//console.log(num1 + num2);
console.log(num1+num2+num3);