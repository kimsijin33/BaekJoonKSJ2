#include <stdio.h>

int main()
{
	char cha1[50];
	char cha2[] = "??!";

	scanf("%s", cha1);

	printf("%s%s\n", cha1, cha2);

	return 0;
}