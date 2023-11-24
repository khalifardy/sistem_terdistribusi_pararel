#include <stdio.h>
#include <math.h>

double rumus(int k) {
    int pembilang = 2 * k + 1;
    return pow(-1, k) / (double)pembilang;
}

double pi_taksiran(int n) {
    double total = 0;
    for (int i = 0; i <= n; i++) {
        total += rumus(i);
    }
    return 4 * total;
}

int main() {
    // n = 10
    printf("Taksiran Pi untuk n = 10: %lf\n", pi_taksiran(10));

    // n = 100
    printf("Taksiran Pi untuk n = 100: %lf\n", pi_taksiran(100));

    // n = 1000
    printf("Taksiran Pi untuk n = 1000: %lf\n", pi_taksiran(1000));

    return 0;
}
