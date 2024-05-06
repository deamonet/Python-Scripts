#include <vector>
#include <iomanip>
#include <iostream>
#include <stdio.h>
#include <typeinfo.h>

using namespace std;

void ShowVec(const vector<int>& valList){
    int count = valList.size();
    for (int i = 0; i < count;i++){
        cout << valList[i] << "\t";
    };
    cout<<"\n";
}

void Show2Vec(const vector<vector<int>>& vallist2){
    int count = vallist2.size();
    for(int i=0; i < count;i++){
        cout<<"\n";
        ShowVec(vallist2[i]);
    }
}



int main(){
    vector<int> nums;
    for(int i=0;i<3;i++){
        nums.push_back(i);
        cout<<nums[i]<<",";
    };

    cout<<"\n\n";
    ShowVec(nums);
    nums.clear();
    if(nums.empty()){cout<<"yes";}
    else{cout<<"no";};

    for(int i=0;i<3;i++){
        nums.push_back(i);
        cout<<nums[i]<<",";
    };

    cout<<"\n\n";
    ShowVec(nums);


}