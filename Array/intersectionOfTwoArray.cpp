//Brute Force Approach
#include <iostream>
#include <vector>
using namespace std;

vector<int> intersection(vector<int> a,vector<int> b){
    vector<int> inter;
    int v[]={};
    int n1=a.size();
    int n2=b.size();
    int i=0;
    int j=0;

    for(i;i<n1;i++){
        for(j;j<n2;j++){
            if(a[i]==b[i] && v[j]==0){
                inter.push_back(a[i]);
                v[i]=1;
                break;
            }
            if(b[j]>a[i]) break;
        }
    }

    return inter;

}


int main(){
    vector<int> ans=intersection({1,2,3,4},{1,1,2,4});
    for(int a:ans){
        cout<<a<<endl;
    }
    return 0;
}
