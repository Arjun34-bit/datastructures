//Optimal Solution

#include <iostream>
#include <vector>
using namespace std;


 int largestE(int a[],int n){
    int temp=a[0];
    for(int i=1;i<n;i++){
        if(a[i]>temp){
            temp=a[i];
        }
    }
    return temp;
}
//Time Complexity : O(n) and Space Complexity : O(1)=stores constants in newly created temp variable

int main() {
    int a[]={1,2,7,4,5};
    int result=largestE(a,5);
    cout<<result;
    return 0;
}