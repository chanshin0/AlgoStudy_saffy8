// �˶� �ð�
#include <iostream>
using namespace std;

int main() {
	int h, m;
	cin >> h >> m;

	if (m < 45) {
		m = m + 60 - 45;
		h = (h == 0) ? 23 : h - 1;
	}
	else {
		m -= 45;
	}
	cout << h << ' ' << m;
	
	return 0;
}

// <<���� ǥ����>>
// (����) ? a : b;
// ������ ���̸� a��ȯ, �����̸� b��ȯ