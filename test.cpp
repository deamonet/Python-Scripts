#include <vector>
#include <iomanip>
#include <iostream>
#include <stdio.h>
#include <typeinfo.h>
#include <string>

using namespace std;

void ShowVec(const vector<int> &valList)
{
    int count = valList.size();
    for (int i = 0; i < count; i++)
    {
        cout << valList[i] << "\t";
    };
    cout << "\n";
}

int main(void)
{
    static const int arr[] = {0, 1};
    vector<int> vec(arr, arr + sizeof(arr) / sizeof(arr[0]));
    vector<int>::const_iterator first = vec.begin();
    vector<int>::const_iterator last = vec.begin()+1;
    vector<int> subvec(first, last);
    ShowVec(vec);
    cout << "\n\n";
    ShowVec(subvec);
    cout << subvec.size();
}