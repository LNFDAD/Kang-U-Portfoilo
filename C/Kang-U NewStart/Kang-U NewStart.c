#include <stdio.h>

int main(){
	int pickone;
    printf("I start my activities\n\n");
    printf("Pick one!\n");
    printf(" 1. [ My name ] \n 2. [ My E-mail ] \n 3. [ My birthday ] \n 4. [ My Home-town ] \n");
    scanf("%d",&pickone);
    if(pickone == 1){
    	printf("My name is Kangyoo");
    }else if(pickone == 2){
    	printf("My E-mail is e.kangyoo@gmail.com ");
    }else if(pickone == 3){
    	printf("My birthday is March 9th");
    }else if(pickone == 4){
    	printf("My Home-town is Korea");
    }else if (pickone != 1 && pickone != 2 && pickone != 3 && pickone != 4){
    	printf("Error");
    }
    getch();
	return 0;
}