#include <stdio.h>
//����ִ�к󣬾ֲ����������ڽ��������ؾ�̬�ֲ�������ȫ�ֱ����ĵ�ַ�ǰ�ȫ�ġ�
int* f()
{
	int i = 12;
	return &i;
}int g()
{
	int k = 24;
	printf("k=%d\n", k);
}
int main()
{
	int* p = f();
	printf("*p=%d\n",*p);
	g();
	printf("*p=%d\n", *p);
}
