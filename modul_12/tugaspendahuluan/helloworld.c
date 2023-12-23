#include <stdio.h>
#include <omp.h>

int main() {
    // Set the number of threads
    omp_set_num_threads(12);

    // Get the start time
    double start_time = omp_get_wtime();

    #pragma omp parallel
    {
        int thread_id = omp_get_thread_num();
        printf("Hello World from thread %d\n", thread_id);
    }

    // Get the end time
    double end_time = omp_get_wtime();

    // Calculate and print the elapsed time
    double elapsed_time = end_time - start_time;
    printf("Elapsed time: %f seconds\n", elapsed_time);

    return 0;
}
