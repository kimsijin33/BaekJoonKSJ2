#include <iostream>

int main() {
    int A, B;
    
    // 변수 입력 받기
    if (!(std::cin >> A >> B)) return 0;
    
    // 비교 로직 수행
    if (A < B) {
        std::cout << "<" << "\n";
    } else if (A > B) {
        std::cout << ">" << "\n";
    } else {
        std::cout << "==" << "\n";
    }
    
    return 0;
}