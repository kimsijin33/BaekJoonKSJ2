#include <iostream>

using namespace std;

int main()
{
	int num1, num2;
	cin >> num1 >> num2;

	int new1 = 0;
	int new2 = 0;
	for (int i = 0; i < 3; i++)
	{
		new1 *= 10;
		new1 = new1 + num1 % 10;
		num1 /= 10;

		new2 *= 10;
		new2 = new2 + num2 % 10;
		num2 /= 10;
	}

	cout << (new1 > new2 ? new1 : new2) << "\n";

	return 0;
}