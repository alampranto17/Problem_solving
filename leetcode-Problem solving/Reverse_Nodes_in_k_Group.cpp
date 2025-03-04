#include<bits/stdc++.h>
using namespace std;

 struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
  };

  ListNode* insertlist(ListNode* head ,int x)
  {
      ListNode* newnode=new ListNode(x);
      if(head==NULL)
      {
          head=newnode;
      }
      else
      {
          ListNode* temp=head;
          while(temp->next!=NULL)
          {
              temp=temp->next;
          }
          temp->next=newnode;
      }
      return head;
  }
  ListNode* reverseKGroup(ListNode* head, int k) {


    }




int main()
{
    int n;
    cin>>n;
    ListNode* head= NULL;

    for(int i =0;i<n;i++)
    {
        int x;
        cin>>x;
        head=insertlist(head,x);
    }
    ListNode* temp=head;

    while(temp!=NULL)
    {
        cout<<temp->val<<" ";
       temp= temp->next;
    }



}
