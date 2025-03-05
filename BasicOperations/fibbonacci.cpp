// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>

using namespace std;

vector<int> fibbo(int last){
    int tval=0;
    vector<int> result= {0,1};
    for(int i=0;i<=last;i++){
        tval=result[i]+result[i+1];
        result.push_back(tval);
    }
    return result;
}

int main() {
    
    vector<int> ans=fibbo(10);
    for(auto i:ans){
        cout<<i<<endl;
    }
    return 0;
}