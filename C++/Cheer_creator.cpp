#include <iostream>
using namespace std;

int main() {
 int n;
 cin>>n;

 if(n<1)
    cout<<"shh";
	
 else if (n>10)
	  cout<<"High Five";

 else
   for(int i = 0; i < n; i++){
     cout<<"Ra!";
   }
   return 0;
}
