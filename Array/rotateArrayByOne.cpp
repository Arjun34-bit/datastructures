// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
void rotateArrayByOne(int arr[],int n){
    int temp=arr[0];
    for(int i=1;i<n;i++){
        arr[i-1]=arr[i];
    }
    arr[n-1]=temp;
}


int main() {
    // Write C++ code here
    // std::cout << "Hello world!";
    int arr[]={1,2,3,4,5};
    rotateArrayByOne(arr,5);
    for(int i=0;i<5;i++){
        cout<<arr[i]<<endl;
    }

    return 0;
}