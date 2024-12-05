#include<bits/stdc++.h>
using namespace std;
#define optimize() ios_base :: sync_with_stdio(0);cin.tie(0);cout.tie(0);
// const int xm =1000;
// int arrive[xm];
// int down[xm];
// int store[xm];


int main()
{
   optimize();

   int s,n;
   cin>>s>>n;

   vector<pair<int,int>>v;

   for(int i =0;i<n;i++)
   {
       int x,y;
       cin>>x>>y;
       v.push_back(make_pair(x,y));

   }
   sort(v.begin(),v.end());


    bool flag=false;
   for(int i =0;i<n;i++)
   {
    if(s>v[i].first)
    {
      s+=v[i].second;
      flag=true;
    }
    else
    {
        flag= false;
        break;
    }
   }

   if(flag)
   {
    cout<<"YES"<<endl;
   }
   else
   {
    cout<<"NO"<<endl;
   }


     }

