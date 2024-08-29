#include<iostream>
using namespace std;

int trailed(int n){
    int num_of_zeros = 0;
    while(n % 10 == 0){
        num_of_zeros++;
        n /= 10;
    }
    return num_of_zeros;
}

int main(){
    cout << trailed(1000);
}