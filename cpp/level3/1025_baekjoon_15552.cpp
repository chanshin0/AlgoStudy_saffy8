#include <iostream>
using namespace std;

int main() {
	// tc�� ���Ƽ� ������� ������ �ؾ��� ��
	ios::sync_with_stdio(false); cin.tie(NULL);

	int t, a, b;
	cin >> t;
	for (t; t > 0; t -= 1) {
		cin >> a >> b;
		cout << a + b << "\n";
	}
	return 0;
}

//--------------------------------------------------------

// sanf, printf ���
#include <iostream>
using namespace std;

int main() {
	int t, a, b;
	scanf("%d", &t);

	for (t; t > 0; t -= 1) {
		scanf("%d%d", &a, &b);
		printf("%d\n", a + b);
	}

	return 0;
}
