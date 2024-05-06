void ShowVec(const vector<int> &valList)
{
    int count = valList.size();
    for (int i = 0; i < count; i++)
    {
        cout << valList[i] << "\t";
    };
    cout << "\n";
}

void Show2Vec(const vector<vector<int>> &vallist2)
{
    int count = vallist2.size();
    for (int i = 0; i < count; i++)
    {
        cout << "\n";
        ShowVec(vallist2[i]);
    }
}