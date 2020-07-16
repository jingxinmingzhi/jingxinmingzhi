#include <stdio.h>
#pragma warning(disable:4996)；
//C语言中结构体变量不是指针（这和数组变量不同）。结构体变量作为传参时，是传值（复制一份一样的数据）。
struct point {
	int x;
	int y;
};
struct point getStruct(struct point p);

void main()
{
	struct point p = { 0,0 };
	getStruct(p);
	printf("%d", p.x);
	printf("%d\n", p.y);
}

struct point getStruct(struct point p)
{
	scanf("%d", &p.x);
	scanf("%d", &p.y);
	printf("%d", p.x);
	printf("%d\n", p.y);
}

//struct point getStruct(void)
//{
//	struct point p;
//	scanf("%d", &p.x);
//	scanf("%d", &p.y);
//	printf("%d", p.x);
//	printf("%d\n", p.y);
//	return p;
//}


