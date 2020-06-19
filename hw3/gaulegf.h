/* gaulegf.h Gauss Legendre numerical quadrature x and w computation */
/* integrate from x1 to x2 using n evaluations of the function f(x)  */
/* usage: double x[20],w[20];            computed by gaulegf         */
/*        gaulegf( x1, x2,  x, w, n);                                */
/*        area = 0.0;                                                */
/*        for(i=1; i<=n; i++)            yes, 1..n                   */
/*          area += w[i]*f(x[i]);                                    */

void gaulegf(double x1, double x2, double x[], double w[], int n);
