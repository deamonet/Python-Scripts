#include <iostream>
#include <stdio.h>
#include <iomanip>

using namespace std;

int main(){
    float s;
    int n;
    while(cin>>s>>n){
        double res = 1;
        while(n != 0){
        res = res * (double)s;
        --n;
        };
        cout<<std::fixed<<res<<endl;
    };
    return 0;
};
