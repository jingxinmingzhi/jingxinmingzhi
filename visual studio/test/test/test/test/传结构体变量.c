#include <stdio.h>
#pragma warning(disable:4996)��
//C�����нṹ���������ָ�루������������ͬ�����ṹ�������Ϊ����ʱ���Ǵ�ֵ������һ��һ�������ݣ���
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


