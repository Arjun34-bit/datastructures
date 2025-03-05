#include <iostream>
#include <vector>
using namespace std;

int removeDuplicate(int a[],int n){
    int i=0;
    for(int j=1;j<n;j++){
        if(a[j]!=a[i]){
            a[i+1]=a[j];
            i++;
        }
    }
    return i+1;
}

int main(){
    int a[]={1,2,2,3,3,4,5};
    int n=removeDuplicate(a,7);
    for(int i:a){
        cout<<i<<endl;
    }
    cout<<"No. of Unique Elements : "<<n;
    return 0;
}