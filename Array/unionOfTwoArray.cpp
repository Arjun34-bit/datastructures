// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>
using namespace std;

//[1,1,2,3,4,4,5]  [1,2,2,2,3,5,5,6]  => [1,2,3,4,5,6]
vector<int> unionOfTwoArray(vector<int> a,vector<int> b){
    vector<int> unionArr;
    int n1=a.size();
    int n2=b.size();
    int i=0;
    int j=0;
    
    while(i<n1 && j<n2){
        if(a[i]<=b[j]){ 
            if(unionArr.size()==0 || unionArr.back()!=a[i]){
                unionArr.push_back(a[i]);
            }
            i++;
        }else{
            if(unionArr.size()==0 || unionArr.back()!=b[j]){
                unionArr.push_back(b[j]);
            }
            j++;
        }
    }
    
    while(j<n2){
        if(unionArr.size()==0 || unionArr.back()!=b[j]){
                unionArr.push_back(b[j]);
        }
        j++;
    }
    while(i<n1){
        if(unionArr.size()==0 || unionArr.back()!=a[i]){
                unionArr.push_back(a[i]);
        }
        i++;
    }
    return unionArr;
}

int main() {
    vector<int> a={1,1,2,3,4,4,5};
    vector<int> b={1,2,2,2,3,5,5,6};
    vector<int> ans=unionOfTwoArray(a,b);
    for(int i:ans){
        cout<<i<<endl
        ;
    }
    return 0;
}