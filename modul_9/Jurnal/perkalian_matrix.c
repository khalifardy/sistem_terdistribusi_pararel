#include <stdio.h>
#include <stdlib.h>

void perkalianMatrix(int *matrixa, int *matrixb, int ***hasil, int rows_a, int cols_a, int rows_b, int cols_b) {
    // Periksa apakah jumlah kolom matrixa sama dengan jumlah baris matrixb
    if (cols_a == rows_b) {
        // Mengalokasikan memori untuk matriks hasil
        *hasil = (int **)malloc(rows_a * sizeof(int *));
        for (int i = 0; i < rows_a; i++) {
            (*hasil)[i] = (int *)malloc(cols_b * sizeof(int));
        }

        for (int i = 0; i < rows_a; i++) {
            for (int j = 0; j < cols_b; j++) {
                (*hasil)[i][j] = 0;
                for (int k = 0; k < cols_a; k++) {
                    (*hasil)[i][j] += matrixa[i * cols_a + k] * matrixb[k * cols_b + j];
                }
            }
        }
    } else {
        printf("Jumlah kolom pada matrixa tidak sama dengan jumlah baris pada matrixb\n");
    }
}

int main() {
    int matrixa[3][3] = {{1, 2, 3}, {3, 4 , 5}, {5, 6 , 7}};
    int matrixb[3][1] = {{1},{2},{3}};
    int **hasil;

    int rows_a = sizeof(matrixa) / sizeof(matrixa[0]);
    int cols_a = sizeof(matrixa[0]) / sizeof(matrixa[0][0]);
    int rows_b = sizeof(matrixb) / sizeof(matrixb[0]);
    int cols_b = sizeof(matrixb[0]) / sizeof(matrixb[0][0]);

    perkalianMatrix(&matrixa[0][0], &matrixb[0][0], &hasil, rows_a, cols_a, rows_b, cols_b);

    // Menampilkan hasil perkalian matrix
    for (int i = 0; i < rows_a; i++) {
        for (int j = 0; j < cols_b; j++) {
            printf("%d ", hasil[i][j]);
        }
        printf("\n");
    }

    // Membebaskan memori yang dialokasikan
    for (int i = 0; i < rows_a; i++) {
        free(hasil[i]);
    }
    free(hasil);

    return 0;
}
