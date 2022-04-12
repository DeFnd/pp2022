class Tong7GiaiThua
{
public static void main(String args[])
{
int i=0;
int j=0;
int Ketqua=0;
for(i=1;i<=7;i++)
{
int Sn=1;
for(j=1;j<=i;j++)
{
Sn=Sn*j;
}
Ketqua=Sn+Ketqua;
}
System.out.println("Ket qua can tim la:"+""+Ketqua);
}
}

