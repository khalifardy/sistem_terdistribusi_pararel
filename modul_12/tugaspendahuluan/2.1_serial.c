#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <omp.h>

int main() {
    srand(time(NULL));
    double x;
    double y;
    long long int number_in_circle = 0;
    long long int number_of_tosses = 100000000;
    long long int toss = 0;
    double pi_estimate;
    double distance_squared;
    clock_t before = clock();

    #pragma omp parallel for private(x, y, distance_squared) reduction(+:number_in_circle) num_threads(4)
    for (toss = 0; toss < number_of_tosses; toss++) {
        // random x, y between -1 and 1
        x = (rand() / (double)(RAND_MAX)) * 2 - 1;
        y = (rand() / (double)(RAND_MAX)) * 2 - 1;

        distance_squared = x * x + y * y;
        if (distance_squared <= 1) {
            number_in_circle++;
        }
    }
    clock_t after = clock();

    double diff = (after - before) * 1000. / CLOCKS_PER_SEC;
    pi_estimate = 4.0 * number_in_circle / (double)number_of_tosses;
    printf("%f\n", pi_estimate);
    printf("%f\n", diff);

    return 0;
}
