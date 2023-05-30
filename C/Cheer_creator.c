#include <stdio.h>

int main() {
	int n;
  scanf("%d",&n);

  if(n<1)
	    printf("shh");
	
  else if (n>10)
	    printf("High Five");

  else
     for(int i = 0; i < n; i++){
         printf("Ra!");
     }
     return 0;
}
