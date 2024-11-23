#include<bits/stdc++.h>
using namespace std;
struct Node
{
    int data;
    struct Node *next;
    Node(int x)
    {
        data = x;
        next = NULL;
    }
};

Node* value(Node* head,int n)
{
    Node * temp =head;
    for(int i =0; i<n; i++)
    {
        int p;
        cin>>p;
        Node * newnode = new Node(p);

        if(head==NULL)
        {
            head=newnode;
            temp=head;

        }
        else
        {
            temp->next=newnode;
            temp=temp->next;
        }
    }

    return head;

}

stack<int>s;
bool isPalindrome(ListNode* head) {

    Node temp=head;
    int p(Node* temp)
    {
       if(temp==NULL)
       {
           return 0;
       }
       s.push(temp->data);
       p(temp->next);




    }








    }


int main()
{


    int n;
    cin>>n;
    Node *head =NULL;


    head =value(head,n);
    Node* temp=head;


    while(temp!=NULL)
    {
        cout<<temp->data<<" ";
        temp=temp->next;
    }

    cout<<isPalindrome(head)<<endl;













}

