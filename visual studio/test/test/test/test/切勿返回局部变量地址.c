#include <stdio.h>
//函数执行后，局部变量生命期结束。返回静态局部变量和全局变量的地址是安全的。
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
