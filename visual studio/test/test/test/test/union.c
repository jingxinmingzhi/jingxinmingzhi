#include <stdio.h>
//union内部的变量共用一块内存空间
typedef union {
	int i;
	char ch[sizeof(int)];
}CHI;

int main()
{
	CHI chi;
	int i;
	chi.i = 1234;
	for (i = 0;i < sizeof(int);i++)
	{
		printf("%02hhx",chi.ch[i]);
	}
	printf("\n");
	printf("%d",sizeof(CHI));
	return 0;
}