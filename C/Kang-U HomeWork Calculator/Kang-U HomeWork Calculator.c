#include <stdio.h>

int main(){
	int previousHomework , thisHomework ;
	float result;

	printf("previous Homework : ~");
	scanf("%d",&previousHomework);

	printf("this Homework : ~");
    scanf("%d",&thisHomework);

    if(previousHomework > thisHomework){

    	printf("Error : (prvious Homework > this Homework)");

    }else if( previousHomework == thisHomework){

    	printf("0 page 0 sheet");

    }else{

    	result = thisHomework-previousHomework;
    	printf("%.0f page %.1f sheet",result,result /2);

    }
	getch();
	return 0;
}

