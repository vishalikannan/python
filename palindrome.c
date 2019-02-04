#include<stdio.h>
int main()
{
int n,r=0,z;
z=n;
while(z!=0)
{
r=r*10;
r=r+z%10;
z=z/10;
}
if(n==r)
printf("Yes");
else
printf("No");
return 0;
}
