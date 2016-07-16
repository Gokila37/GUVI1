#include<stdio.h>
#include<conio.h>
#include<string.h>
void main()
{
char ch[20];
clrscr();
printf("enter the day:");
scanf("%s",ch);
if(((strcmp(ch,"sunday")==0)||(strcmp(ch,"saturday")==0)))
{
printf("Holiday\n");
printf("false");
}
else
{
printf("Working day\n");
printf("True");
}
getch();
