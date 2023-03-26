#include <iostream>
#include <cmath>
using namespace std;
int memo[10000];
int isOne = -1;
int a = 0;


int main(void)
{
  int n,m;
  cin>>n>>m;
  if(n<2) return 0;
  for(int i = 0;i<m;i++)
  {
    cout<<'-';
  }
  cout<<a++;
  cout<<'\n';

  for(int j = 1;j<pow(2,m-1);j++)
  {
    memo[j] = 1;

  }
  for(int k = 2;k<=m-1;k++)
  {
    int num = 0;
    int z = 1;
    while(num<pow(2,m-1))
    {
      num = pow(2,k) * z - pow(2,k-1);
      memo[num] = k;
      z++;
    }
  }
  // for(int j = 1;j<pow(2,m-1);j++)
  // {
  //   cout<<memo[j]<<'\n';
  // }
  for(int k = 0;k<n;k++){
    for(int i = 1;i<pow(2,m-1);i++)
    {
      for(int j=0;j<memo[i];j++)
      {
        cout<<'-';
      }
      cout<<'\n';
    }
    for(int i = 0;i<m;i++)
    {
      cout<<'-';
    }
    cout<<a++;
    cout<<'\n'; 
  }

  return 0;
}