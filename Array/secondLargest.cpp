// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>
using namespace std;

int secondLargest(vector<int> arr){
    int largest=-1;
    int secondLargest=-1;
    for(int i=0;i<=arr.size();i++){
        if(arr[i]>largest){
            secondLargest=largest;
            largest=arr[i];
        }else if(arr[i]!=largest && arr[i]>secondLargest){
            secondLargest=arr[i];
        }
    }
    return secondLargest;
}

int main() {
    // Write C++ code here
    vector<int> arr={10,25,36,41,25,12,23};
    cout<<secondLargest(arr);
    return 0;
}