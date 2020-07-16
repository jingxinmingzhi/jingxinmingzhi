//typedef struct data {
//	int month;
//	int day;
//	int year;
//}myday;
//myday day;
//myday* p = &day;
#include <stdio.h>
#pragma warning(disable : 4996)
struct point {
	int x;
	int y;
};
struct point* getStruct(struct point*);
void output(struct point);
void print(const struct point *p);
int main(){
	struct point y = { 0,0 };
	getStruct(&y);
	output(y);
	output(*getStruct(&y));
	print(getStruct(&y));
	getStruct(&y)->x = 0;
	*getStruct(&y) = (struct point){ 1,2 };
};
struct point* getStruct(struct point* p)
{
	scanf("%d", &p->x);
	scanf("%d", &p->y);
	printf("%d", p->x);
	printf("%d\n", p->y);
}

void output(struct point p)
{
	printf("%d,%d", p.x, p.y);
}

void print(const struct point* p)
{
	printf("%d,%d", p->x, p->y);
}



