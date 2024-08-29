#include<iostream>
#include<bits/stdc++.h>
using namespace std;

void sieve(int n){
    vector<bool> v(n+1, true);
    // bool v[n] = {true};

    for(int i = 2;i <= n; i++){
        if(v[i]){
            for(int j = 2 * i;j <= n; j+=i){
                v[j] = false;
            }
        }
    }

    for(int i = 2;i <= n;i++){
        if(v[i]){
            cout << i << " ";
        }
    }
}

int main(){
    sieve(10);
}