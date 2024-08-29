#include<iostream>
using namespace std;

int power(int x, int n){
    if(n==0) return 1;
    int tmp = power(x, n/2);
    tmp *= tmp;
    if(n % 2 == 0){
        return tmp;
    }
    else return tmp * x;
}

int main(){
    cout << power(5, 2);
}