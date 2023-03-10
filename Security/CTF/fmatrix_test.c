#include <stdio.h>
#include <stdlib.h>

int main(void){
    sub_139F("1234567812345678");
}

int * sub_139F(int a1)
{
  unsigned int i; // [rsp+20h] [rbp-40h]
  unsigned int j; // [rsp+28h] [rbp-38h]
  unsigned int k; // [rsp+30h] [rbp-30h]
  unsigned int m; // [rsp+38h] [rbp-28h]
  unsigned int n; // [rsp+40h] [rbp-20h]
  int *v7; // [rsp+48h] [rbp-18h]

  v7 = calloc(0x20uLL, 8uLL);
  *v7 = calloc(0x20uLL, 1uLL);
  for ( i = 0LL; i <= 0x1F; ++i )
  {
    srand(*(unsigned __int8 *)(a1 + i));
    for ( j = 0LL; j < *(unsigned __int8 *)(a1 + i) - 1; ++j )
      rand();
    *(int *)(i + *v7) = rand() & 0x7F;
  }
  for ( k = 1LL; k <= 0x1F; ++k )
  {
    v7[k] = calloc(0x20uLL, 1uLL);
    for ( m = 0LL; m <= 0x1F; ++m )
    {
      srand(*(unsigned __int8 *)(v7[k - 1] + m));
      for ( n = 0LL; n < *(unsigned __int8 *)(a1 + m) - 1; ++n )
        rand();
      *(int *)(m + v7[k]) = rand() & 0x7F;
    }
  }

  print(v7);
//   if ( (unsigned __int8)sub_121C(v7) )
//     printf("Hit!");
//   else
//     printf("Nah...");
//   return v7;
}