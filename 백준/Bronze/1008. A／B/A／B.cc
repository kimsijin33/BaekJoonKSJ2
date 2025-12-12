#include <stdio.h>

int main()
{
    double num1, num2;
    double num3;
    scanf("%lf %lf", &num1, &num2);
    //printf("%d %d\n", num1, num2);
    num3 = num1 / num2;
    printf("%.9f\n", num3);

    return 0;
}