// Online C++ compiler to run C++ program online
// Brute Force Approach

//Time Complexity : O(n) and Space Complexity : O(1)=stores constants in newly created temp variable

#include <iostream>
using namespace std;

int findM(int a[],int n){
    if(n<=0){
        return 0;
    }
    for(int i=1;i<n;i++){
        if(i!=a[i-1]){
            return i;
            break;
        }
    }
}

int findMXOR(int a[],int n){  // Optimal Approach using XOR operations 2^2=0 and 0^2=2
    int xor1=0;
    int xor2=0;
    int N=n-1;

    for(int i=1;i<n;i++){
        xor1=xor1^i;
        xor2=xor2^a[i-1];
    }
    xor1=xor1^n;
    return xor1^xor2;
}

int main() {
    int a[]={1,2,3,4,5,6,7,8,10};
    cout<<"Brute Force Approach : "<<findM(a,10)<<endl;
    cout<<"Optimal Approach : "<<findMXOR(a,10);
    return 0;
}