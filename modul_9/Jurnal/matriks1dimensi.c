#include <stdio.h>
#include <stdlib.h>

int* matrix1dimensi(int matrixc[3][4], int rows, int cols) {
    int jumlah_elemen = rows * cols;
    int *hasil = (int *)malloc(jumlah_elemen * sizeof(int));

    int count = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            hasil[count] = matrixc[i][j];
            count++;
        }
    }

    return hasil;
}

int main() {
    // Inisialisasi matriksC
    int matrixc[3][4] = {{0, 1, 2, 3}, {4, 5, 6, 7}, {8, 9, 10, 11}};
    int rows = sizeof(matrixc) / sizeof(matrixc[0]);
    int cols = sizeof(matrixc[0]) / sizeof(matrixc[0][0]);

    // Panggil fungsi matrix1dimensi
    int *hasil = matrix1dimensi(matrixc, rows, cols);

    // Tampilkan hasil
    printf("Hasil matrix1dimensi:\n");
    for (int i = 0; i < rows * cols; i++) {
        printf("%d ", hasil[i]);
    }

    // Bebaskan memori
    free(hasil);

    return 0;
}
