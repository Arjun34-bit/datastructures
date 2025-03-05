// Online C++ compiler to run C++ program online
#include <iostream>

using namespace std;

int fact(int num){
    int mul=1;
    for(int i=1;i<=num;i++){
        mul*=i;
    }
    return mul;
}

int main() {
    cout<<fact(10);
    return 0;
}