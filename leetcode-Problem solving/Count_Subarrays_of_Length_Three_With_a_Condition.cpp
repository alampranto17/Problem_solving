#include<bits/stdc++.h>
using namespace std;

int countSubarrays(vector<int>& nums) {
int i=1;
int count=0;
        while(i<nums.size() && (i+1)<nums .size()){


                if(nums[i-1]+nums[i+1]==((nums[i]*1.0)/2))
                {
                    cerr<<nums[i-1]<<" "<<nums[i+1]<<" "<<(nums[i])<<endl;
                    count++;
                }
                i++;


        }
        return count;

    }

int main()
{

    int n;
    cin>>n;
    vector<int>nums;
    for(int i=0;i<n;i++)
    {
        int x;
        cin>>x;
        nums.push_back(x);
    }
   cout<< countSubarrays(nums)<<endl;

}
