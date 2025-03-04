#include<bits/stdc++.h>
using namespace std;

   int reverse(int x) {

        stack<int>s;
        long long nums;
            if(x>0)
            {
                 nums=x;
            }else
            {

                 nums=x;
                nums*=-1;
            }



            while(nums!=0)
            {
                s.push((char)(nums%10));
                nums=nums/10;
            }






        long long number=0;
        int i=0;
      while(!s.empty())
      {
         number+= s.top()*pow(10,i);
          s.pop();
          i++;
      }



      if(INT_MAX<number || INT_MIN>number )
      {
          return 0;
      }

      return number;



    }

    int main()
    {
        int n;
        cin>>n;

        cout<<reverse(n)<<endl;


    }
