//https://leetcode.com/contest/weekly-contest-426/problems/smallest-number-with-all-set-bits/

#include<bits/stdc++.h>
using namespace std;

 int smallestNumber(int n) {
        int i =0;

        while((n>=pow(2,i)))
            {

                i++;
            }
            return pow(2,i)-1;

    }

int main()
{
    int n;
    cin>>n;
    cout<<smallestNumber( n)<<endl;
}
