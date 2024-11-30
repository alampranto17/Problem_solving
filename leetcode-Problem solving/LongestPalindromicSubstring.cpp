


#include<bits/stdc++.h>
using namespace std;
bool ispal(string s )
{
    for(int i =0,j=s.size()-1;i<s.size()/2;i++,j--)
    {
        if(s[i]!=s[j])
        {
            return false;
        }

    }
    return true;
}

    string longestPalindrome(string p) {

        string a="";
        for(int i =0;i<p.size();i++)
        {
            string s="";
            for(int j=i;j<p.size();j++)
            {
                    s+=p[j];
                if(ispal(s))
                {
                    if(a.size()<s.size())
                    {
                        a=s;
                    }

                }
            }
        }


    return a;

    }


    int main()
    {
        string s;
       getline(cin,s);

       cout<<longestPalindrome(s)<<endl;







    }


