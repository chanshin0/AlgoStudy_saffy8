#include <iostream>
using namespace std;

int main() {
	double a, b;
	cin >> a >> b;

	//cout.precision(11);

	cout << fixed;
	cout.precision(9);

	cout << a / b;	
	return 0;
}

// 실수는 float인데... 소수점을 더 길게 계산하고 싶다면 double을 써야한다.
// a,b <= 10이고 오차가 10**-9보다 작아햐 하니까 정수 포함해서 11자리까지 출력 -> .precision(11)
// 또는, 소수자리 고정하고 cout << fixed; .presicion(9)