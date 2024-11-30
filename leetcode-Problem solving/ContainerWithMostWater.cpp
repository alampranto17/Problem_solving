//https://leetcode.com/problems/container-with-most-water/submissions/1466604616/
#include<bits/stdc++.h>
using namespace std;

int maxArea(vector<int>& height) {

        stack<int>s;
        queue<int>q;
        for(int i =0;i<height.size();i++)
        {
            s.push(height[i]);
            q.push(height[i]);
        }

        int i=0;
        int n=height.size()-1;
        int sum=0;
        while(i<n)
        {
            if(q.front()<=s.top())
            {
                int p=(q.front()*(n-i));
               sum=max(sum,p);
               q.pop();
               i++;
            }
            else
            {
                int p=(s.top()*(n-i));
                sum=max(sum,p);
               s.pop();
               n--;
            }
        }
        return sum;
    }



   int main()
    {

        vector<int>height={1,8,6,2,5,4,8,3,7};

        // for(int i =0;i<n;i++)
        // {
        //     cin>>height[i];
        // }

    cout<<maxArea(height)<<endl;
    return 0;
    }







