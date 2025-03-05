#include <iostream>

using namespace std;

void print12_1(){
    for(int i=0;i<=5;i++){
        for(int j=1;j<=i;j++){
            cout<<j;
        }
        cout<<endl;
    }
}


void print12(){
    int len=5;
    for(int i=0;i<=5;i++){
        for(int j=1;j<=len;j++){
            cout<<j;
        }
        len=len-1;
        cout<<endl;
    }
}

void print_space(){
    int len=5;
    for(int i=0;i<=len;i++){
        for(int k=1;k<=len-i;k++){
            cout<<" ";
        }
        for(int j=1;j<=i;j++){
            cout<<j;
        }
        cout<<endl;
    }
}

void print_space_1(){
    int len=5;
    for(int i=0;i<=len;i++){
        for(int k=0;k<=i;k++){
            if(k>0){
                cout<<" ";
            }
        }
        for(int j=1;j<=len-i;j++){
            cout<<j;
        }
        cout<<endl;
    }
}


void print_pattern_7(){
    int len=5;
    for(int i=0;i<=len;i++){
        for(int k=0;k<=len-i;k++){
            cout<<" ";
        }
        for(int j=1;j<=i;j++){
            cout<<"*";
            cout<<" ";
        }
        cout<<endl;
    }
}

void print_pattern_10(){    
    int len=5;
    for(int i=0;i<=len;i++){
        for(int k=0;k<=len/2;k++){

            cout<<" ";

        }
        cout<<"*";
        for(int l=len/2;l<=len;l++){

            cout<<" ";

        }
        cout<<endl;
    }
}

int main(){
    print12_1();
    print12();
    cout<<"Patterns on Right Side"<<endl;
    print_space();
    cout<<"Left Right Angle triangle"<<endl;
    print_space_1();
    cout<<"Seventh Pattern"<<endl;
    print_pattern_7();
    cout<<"Tenth Pattern"<<endl;
    print_pattern_10();
    return 0;
}