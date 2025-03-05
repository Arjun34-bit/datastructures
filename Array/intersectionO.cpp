#include <iostream>
#include <vector>
using namespace std;

vector<int> intersection(vector<int> a,vector<int> b){
    vector<int> result;
    int n1=a.size();
    int n2=b.size();
    int i=0;
    int j=0;

    while(i<n1 && j<n2){
        if(a[i]<b[j]){
            i++;
        }else if(a[i]>b[j]){
            j++;
        }else{
            result.push_back(a[i]);
            i++;
            j++;
        }
    }
    return result;
}

int main(){
    vector<int> ans=intersection({1,2,3,4},{1,3,4,5});
    for(int a:ans){
        cout<<a<<endl;
    }
    return 0;
}