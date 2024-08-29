#include<iostream>
using namespace std;

int fact(int n){
    if(n <= 1){
        return n;
    }
    int res = 1;
    for(int i = 2;i <= n;i++){
        res *= i;
    }
    return res;
}

int main(){
    cout << fact(4);
}