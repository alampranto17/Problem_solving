#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        string s;
        cin>>n>>s;
        int64_t dsh=count(s.begin(),s.end(),'-');
        int64_t und=n-dsh;
        int64_t ans= (dsh/2) * (dsh-dsh/2) * und;

        cout<<ans<<endl;

    }

}
