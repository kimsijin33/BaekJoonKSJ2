#define _CRT_SECURE_NO_WARNINGS    // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>

int main()
{
    int num1, num2;
    scanf("%d %d", &num1, &num2);
    //printf("%d %d\n", num1, num2);
    printf("%d\n", num1 + num2);

    return 0;
}