// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>

using namespace std;

vector<int> twoP(vector<int> &arr,int target){
    int left=0;
    int right=arr.size()-1;
    vector<int> result;
    
    while(left<right){
        int sum=arr[left]+arr[right];
        if(sum==target){
            result.push_back(left);
            result.push_back(right);
            return result;
        }else if(sum<target){
            left++;
        }
        else{
            --right;
        }
    }
    return result;
}

int main() {
    // Write C++ code here
    vector<int> arr={1,2,2,3};
    int target=4;
    vector<int> ans=twoP(arr,target);
    for(auto i:ans){
        cout<<i;
    }
    return 0;
}