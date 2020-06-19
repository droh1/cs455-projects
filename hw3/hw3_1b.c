/* test_gaulegf.c  test  gaulegf.c */
#include "gaulegf.h"
#include <stdio.h>

static double f(double p)
{
  return sin(p);
  //return p*p;
}

int main(int argc, char * argv[])
{
  int n = 8;
  double x[17];
  double w[17];
  double area;
  int i;

  printf("calling gaulegf(0.0, 1.0, x, w, 8) \n");
  gaulegf(0.0, 1.0, x, w, n);

  //for(i=1; i<=n; i++)
    //printf("x[%d]=%f, w[%d]=%f \n", i, x[i], i, w[i]);
    //your_value = your_value + w[j]*sin(x[j])
  area = 0.0;

  for(i=1; i<=n; i++)
  {
    //area += w[i]*f(x[i]);
    area = area + (w[i] * sin(x[i]));
  }
  printf("area=%f \n", area);
  printf("error=%e \n", area-(7.0/3.0));

  n = 16;
  //double x[5];
  //double w[5];
  //double area;
  //int i;

  printf("calling gaulegf(0.0, 1.0, x, w, 16) \n");
  gaulegf(0.0, 1.0, x, w, n);

  /*  for(i=1; i<=n; i++)
    printf("x[%d]=%f, w[%d]=%f \n", i, x[i], i, w[i]);
*/	
  area = 0.0;

  for(i=1; i<=n; i++)
  {
    //area += w[i]*f(x[i]);
    area = area + (w[i] * sin(x[i]));
  }
  printf("area=%f \n", area);
  printf("error=%e \n", area-(7.0/3.0));
} /* end test_gaulegf.c */
