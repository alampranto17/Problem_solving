#include<bits/stdc++.h>
using namespace std;
int majorityElement(vector<int>& nums) {
        map<int,int>m;
        for(auto u : nums)
        {
            cout<<u<<endl;
            m[u]++;
        }
            int max =0;
            int fmax=0;

       for(auto u : m)
       {
           cout<<u.first<<" "<<u.second<<endl;
        if(max<u.second)
        {
            max=u.second;
            fmax=u.first;
        }

       }
       return fmax;

    }

int main()
{

    vector<int>nums={3,2,3};

 cout<<majorityElement(nums)<<endl;
}
