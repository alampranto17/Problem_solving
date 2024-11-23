


#include<bits/stdc++.h>
using namespace std;
bool visited(string p)
{
    string a=p;

   for(int i= a.size()-1,j=0;i>=0;i--,j++)
   {
       if(a[i]!=p[j])
       {
           return false;
       }
   }
    return true;
}
string lengthOfLongestSubstring(string s) {

    if(s.size()==1)
    {
    return s;
    }
    string substring=s;
    string f="";
    cout<<"sub"<<endl;
    int i=0;
    int j=s.size()-1;
    while(i<=j)
    {
        cout<<i<< " " <<j<<endl;
        cout<<"sub"<<endl;
        if(visited(substring))
        {
            if(substring.size()>f.size())
            {
                f=substring;
            }
            substring=substring.substr(s[i++],s[j--]);
            cout<<"sub"<<substring<<endl;
        }
        else
        {
            substring=substring.substr(s[i++],s[j--]);
            cout<<"Sub"<<substring<<endl;
        }
    }



        return f;;

            }


    int main()
    {
        string s ="adbbcd";
       // getline(cin,s);

       cout<< lengthOfLongestSubstring(s)<<endl;







    }


