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

   int s=0;
   int d=0;
   int left=0;
   int right=v.size()-1;
   bool turn= true;
  while(left<=right)
   {
       cerr<<v[left]<<" "<<v[right]<<endl;
       cerr<<"turn "<<turn<<endl;
       if(v[left]>v[right])
       {

           if(turn)
           {
               cerr<<"s "<<v[left]<<endl;
               s+=v[left];
           }
           else
           {
               cerr<<"d "<<v[left]<<endl;
               d+=v[left];

           }
           left++;

       }
       else
       {
            if(turn)
           {
               cerr<<"s "<<v[right]<<endl;
               s+=v[right];
           }
           else
           {
               cerr<<"d "<<v[right]<<endl;
               d+=v[right];

           }
           right--;
       }
       turn=!turn;

   }

   cout<<s<<" "<<d<<endl;


     }

