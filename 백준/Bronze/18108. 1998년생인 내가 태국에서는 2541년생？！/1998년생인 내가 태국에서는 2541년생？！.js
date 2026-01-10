const fs = require('fs');

// trim()을 사용하여 입력값 끝의 줄바꿈 문자 등을 제거합니다.
const input = fs.readFileSync('/dev/stdin').toString().trim();

// 결과 출력
const num1 = Number(input);
console.log(num1 - 543);
