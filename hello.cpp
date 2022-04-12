#include<iostream>
#include<string.h>
using namespace std;

struct MatHang
{
	string ten;
	int soluong;
};
struct Node
{
	MatHang info;
	Node* next;	
};
struct Queue
{
	Node *head;
	Node *tail;
};

void nhap(MatHang &x)
{
	cout<<"Nhap ten san pham: ";
    cin>>x.ten;
	cout<<"Nhap so luong:";
	cin>>x.soluong;
}
void xuat(MatHang x)
{
	cout<<"\nTen san pham: "<<x.ten;
	cout<<"\nSoluong: "<<x.soluong<<endl;
}
Node* CreateNode(MatHang x)
{
	Node*p=new Node;
	if (p==NULL)
		exit(1);
	p->info=x;
	p->next=NULL;
	return p;
}
void CreateQueue(Queue &l)
{
	l.head=NULL;
	l.tail=NULL;
}
void EnQueueQ(Queue &l, Node *p)
{
	 if(l.head == NULL)
        l.head = l.tail = p;
    else
		{
        l.tail->next = p;
        l.tail = p;
    	}
}
void InputQueue(Queue &l, int &n, MatHang a[])
{
	cout<<"\n\nNhap so luong khach hang: ";
	cin>>n;
	cout<<endl;
	for (int i=1;i<=n;i++)
		{
			cout<<"Nhap mat hang khach hang "<<i<<" muon mua :";
			cout<<"\n";
			nhap(a[i]);
			Node *p= CreateNode(a[i]);
			if (p!= NULL)
				EnQueueQ(l,p);
		}
}
void DeQueueQ(Queue &l)
{
	
	Node* p;
	if (l.head !=NULL)
		{
			p=l.head;
			l.head=l.head->next;
			delete p;
			if (l.head==NULL)
				l.tail==NULL;
		}
}
void InputSP(int &m, MatHang a[])
{
	cout<<"Nhap so luong san pham: ";
	cin>>m;
	cout<<endl;
	for (int i=1;i<=m;i++)
		{
			cout<<"Nhap san pham thu "<<i<<":";
			cout<<"\n";
			nhap(a[i]);
		}
}
void Processing(Queue &l,int &m,MatHang kho[])
{
    Node*p;
	p=l.head;
	while (p!=NULL)
		{
		  for(int i=1;i<=m;i++)
		        if (p->info.ten==kho[i].ten)
		            if (p->info.soluong<= kho[i].soluong)
		            {
		                kho[i].soluong = kho[i].soluong - p->info.soluong;
		                cout<<"\n\nXu ly thanh cong"<<endl;
		            }
		            else
		            {
		                cout<<"\n\nError, San pham khong con trong kho"<<endl;
		            }
		  DeQueueQ(l);
		  p=l.head;
		}
}
int main()
{
	int n,m;
    MatHang kho[100];
	MatHang KH[100];
	InputSP(m,kho);
	for (int i=1;i<=m;i++)
	    xuat(kho[i]);
	Queue Q;
	CreateQueue(Q);
	InputQueue(Q,n,KH);
	for (int i=1;i<=n;i++)
		xuat(KH[i]);
	Processing(Q,m,kho);
	cout<<"\n\nSo luong san pham con lai trong kho:"<<endl;
	for (int i=1;i<=m;i++)
	    xuat(kho[i]);
	return 0;
}
