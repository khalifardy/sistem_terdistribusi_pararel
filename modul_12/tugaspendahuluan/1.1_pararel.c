#include <stdio.h>
#include <time.h>
#include <omp.h>

int main() {
    double factor = 1.0;
    double sum = 0.0;
    double pi_approx;
    clock_t before = clock();
    int k;
    int n = 100000000;

    #pragma omp parallel for reduction(+:sum) private(factor) num_threads(15)
    for (k = 0; k < n; k++) {
        factor = (k % 2 == 0) ? 1.0 : -1.0;
        sum += factor / (2 * k + 1);
    }
    pi_approx = 4.0 * sum;

    clock_t after = clock();

    double diff = (after - before) * 1000. / CLOCKS_PER_SEC;
    printf("%f\n", pi_approx);
    printf("%f\n", diff);

    return 0;
}
