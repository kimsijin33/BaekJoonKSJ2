#include <iostream>

int main() {
    int A;
    
    // 변수 입력 받기
    if (!(std::cin >> A)) return 0;
    
    // 비교 로직 수행
    if (A >= 90 && A <= 100) {
        std::cout << "A" << "\n";
    } else if (A >= 80 && A <= 89) {
        std::cout << "B" << "\n";
    } else if (A >= 70 && A <= 79) {
        std::cout << "C" << "\n";
    } else if (A >= 60 && A <= 69) {
        std::cout << "D" << "\n";
    } else {
        std::cout << "F" << "\n";
    }
    
    return 0;
}