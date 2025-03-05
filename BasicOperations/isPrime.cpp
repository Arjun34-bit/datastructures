// Online C++ compiler to run C++ program online
#include <iostream>

using namespace std;

bool isPrime(int num){
   if(num<=1){
       return false;
   }
   for(int i=2;i<=num/2;i++){
       if(num%i==0){
           return false;
       }
   }
   return true;
}

int main() {
    cout<<isPrime(4);
    return 0;
}