#include <stdio.h>
#include <math.h>

double fungsi_a(double x) {
    return 0.5 * x + 5;
}

double fungsi_b(double x) {
    return sin(x) + 1;
}

double trapesium_Rule(double start, double end, double (*fungsi)(double), double tinggi) {
    double fung = (fungsi(start) + fungsi(end)) / 2;
    double total = 0;

    while (start < end) {
        start += tinggi;
        total += fungsi(start);
    }

    return (fung + total) * tinggi;
}

double tinggi_trapesium(double start, double end, int n) {
    return fabs((end - start) / n);
}

int main() {
    // n = 10
    double t1 = tinggi_trapesium(-10, 0, 100);
    double luas_1_1 = trapesium_Rule(-10, 0, fungsi_a, t1);
    double luas_1_2 = trapesium_Rule(0, 5, fungsi_b, t1);
    printf("Hasil untuk n=10: %lf\n", luas_1_1 + luas_1_2);

    // n = 100
    double t2 = tinggi_trapesium(-10, 0, 100);
    double luas_2_1 = trapesium_Rule(-10, 0, fungsi_a, t2);
    double luas_2_2 = trapesium_Rule(0, 5, fungsi_b, t2);
    printf("Hasil untuk n=100: %lf\n", luas_2_1 + luas_2_2);

    // n = 1000
    double t3 = tinggi_trapesium(-10, 0, 1000);
    double luas_3_1 = trapesium_Rule(-10, 0, fungsi_a, t3);
    double luas_3_2 = trapesium_Rule(0, 5, fungsi_b, t3);
    printf("Hasil untuk n=1000: %lf\n", luas_3_1 + luas_3_2);

    return 0;
}
