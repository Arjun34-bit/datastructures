// Online C++ compiler to run C++ program online
#include <iostream>

using namespace std;

void patterns(){
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            cout <<" * ";
        }
        cout<<""<<endl;
    }
}

void pattern2(){
    for(int i=0;i<5;i++){
        for(int j=0;j<=i;j++){
            cout <<" * ";
        }
        cout<<""<<endl;
    }
}

void pattern3(){
    for(int i=1;i<5;i++){
        for(int j=1;j<=i;j++){
            cout <<j<<" ";
        }
        cout<<""<<endl;
    }
}

void pattern4(){
    for(int i=1;i<5;i++){
        for(int j=1;j<=i;j++){
            cout <<i<<" ";
        }
        cout<<""<<endl;
    }
}

void pattern5(){
    for(int i=4;i>=0;i--){
        for(int j=0;j<=i;j++){
            cout<<" * ";
        }
        cout<<""<<endl;
    }
}

void pattern6(){
    for(int i=5;i>=1;i--){
        for(int j=1;j<=i;j++){
            cout<<j<<" ";
        }
        cout<<""<<endl;
    }
}

void pattern7(){
    for(int i=1;i<5;i++){
        for(int j=0;j<=5-i-1;j++){
            cout<<" ";
        }
        for(int j=0;j<i;j++){
            cout <<" * ";
        }
        for(int j=0;j<=5-i-1;j++){
            cout<<" ";
        }
        cout<<"         "<<endl;
    }
}

int main() {
    // Write C++ code here
    pattern7();

    return 0;
}