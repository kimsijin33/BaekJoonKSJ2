#include <stdio.h>

int main() {
    int A, B, C;
    //double num3;
    //scanf("%lf %lf", &num1, &num2, &num3);
    scanf("%d %d %d", &A, &B, &C);
    //printf("%d %d\n", num1, num2);
    //num3 = num1 / num2;
    printf("%d\n", (A+B)%C);
    printf("%d\n", ((A%C) + (B%C))%C);
    printf("%d\n", (A*B)%C);
    printf("%d\n", ((A%C) * (B%C))%C);

    return 0;
}
