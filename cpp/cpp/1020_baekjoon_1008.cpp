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

// �Ǽ��� float�ε�... �Ҽ����� �� ��� ����ϰ� �ʹٸ� double�� ����Ѵ�.
// a,b <= 10�̰� ������ 10**-9���� �۾��� �ϴϱ� ���� �����ؼ� 11�ڸ����� ��� -> .precision(11)
// �Ǵ�, �Ҽ��ڸ� �����ϰ� cout << fixed; .presicion(9)