#include <iostream>
#include <vector>
using namespace std;
//  [0,1,2,3,4,5,6]
//  [1,2,3,4,5,6,7]  Right Shift  [5,6,7,1,2,3,4]
// [1,2,3,4]  [5,6,7]
// k=3 n=7

void rotateArrayByk(int arr[],int k,int n){
    vector<int> temp;
    for(int i=n-k;i<n;i++){
        temp.push_back(arr[i]);
        // cout<<temp[i-k-1]<<endl;
    }
    for (int j = n - 1; j >= k; j--) { 
        arr[j] = arr[j - k];          
    }

    // cout<<arr[3]<<endl;
    for(int l=0;l<k;l++){
        arr[l]=temp[l];
        // cout<<i-k-1<<endl;
    }
}

int main(){
    int arr[]={1,2,3,4,5,6,7};
    rotateArrayByk(arr,2,7);
    for(int i=0;i<7;i++){
        cout<<arr[i]<<endl;
    }
}