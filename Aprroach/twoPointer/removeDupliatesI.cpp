// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>

using namespace std;

int removeDup(vector<int> &arr){
    int left=0;
    for(int right=1;right<arr.size();right++){
        if(arr[right]!=arr[left]){
            left++;
            arr[left]=arr[right];
        }
    }
    return left+1;
}

int main() {
    // Write C++ code here
    vector<int> arr={1,2,2,3};
    int ans=removeDup(arr);
    // for(auto i:arr){
    //     cout<<i<<endl;
    // }
    cout<<ans;
    return 0;
}