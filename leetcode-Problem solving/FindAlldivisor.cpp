#include<bits/stdc++.h>
using namespace std;
#define optimize() ios_base :: sync_with_stdio(0);cin.tie(0);cout.tie(0);
// const int xm =1000;
// int arrive[xm];
// int down[xm];
// int store[xm];
const int N=1e7+9;
int arr[N];
int main()

{

for(int i =1;i<N;i++)       // all divisor
{
    for(int j=i;j<N;j+=i)
    {
        arr[j]++;
    }
}
    int n;
    cin>>n;
     long long sum=0;

    for(int i =1;i<=n;i++)
    {
        sum+=(long long)i*arr[i];
    }



cout<<sum<<endl;
}


