//https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

#include<bits/stdc++.h>
using namespace std;
bool visited(string p,char a)
{
    for(int i =0;i<p.size();i++)
    {
        if(p[i]==a)
        {
            return true;
            break;
        }
    }
    return false;
}
int lengthOfLongestSubstring(string s) {
    if(s.empty())
    {
        return 0;
    }
        string finalsubstring="";
         string substring="";
         finalsubstring+=s[0];
         substring+=s[0];

        for(int i =1;i<s.size();i++)
        {

            if(!visited(substring,s[i]))
            {
               substring+=s[i];
            }
            else
            {
                substring=substring.substr(substring.find(s[i])+1);
                substring+=s[i];

            }
            if(substring!="" && finalsubstring.size()<substring.size())
            {
                finalsubstring=substring;
            }
        }


        return finalsubstring.size();

            }


    int main()
    {
        string s ;
        getline(cin,s);

       cout<< lengthOfLongestSubstring(s)<<endl;


    }



