#include<stdio.h>
#include<stdlib.h>


int MouseOn(void)
{
	_AX = 0x033;
	geninterrupt(0x33);
	int p = _CX;
}

void main()
{
	while(1)
		printf("%d",&MouseOn());
}
