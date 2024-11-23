//https://leetcode.com/problems/zigzag-conversion/
#include<bits/stdc++.h>
using namespace std;
 string convert(string s, int numRows) {
        vector<string>arr(numRows);
        if(numRows==1)
        {
            return s;
        }
            int d=1;
            bool f1=false;
            for(int j=0,i=0;j<numRows;j=j+d,i++)
            {
                if(i==s.size())
                {
                    break;
                }
                arr[j]+=s[i];
                if(j==numRows-1 || (f1 && j==0) )
                {
                    
                    if(d==1)
                    {
                        f1=true;
                        d=-1;
                    }
                    else
                    {
                        d=1;
                        f1=false;
                    }
                }

            }
                string p="";
            for(auto u : arr)
            {
                p+=u;
            }

            return p;
    }

    int main()
    {
        int numRows;
        cin>>numRows;
        cin.ignore();
        string s;
        cin>>s;

      cout<< convert(s,numRows)<<endl;






    }