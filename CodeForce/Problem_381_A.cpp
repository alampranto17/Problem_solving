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

   int n;
   cin>>n;
    vector<int>v(n);
   for(int i=0;i<n;i++)
   {
    cin>>v[i];
   }

   sort(v.rbegin(),v.rend());
   for(auto u : v)
   {
       cout<<u<<endl;
   }
   int s=0;
   int d=0;
   for(int i=0;i<n;i++)
   {
       if(i%2==1)
       {
           d+=v[i];
       }
       else
       {
           s+=v[i];
       }
   }

   cout<<s<<" "<<d<<endl;


     }

