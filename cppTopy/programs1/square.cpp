

#include "square.h"

int* sum_of_squares(int entries) {
    int* result = new int[entries];
    result[0]=0;
    for (int i=1; i < entries; i++) {
        result[i]=result[i-1]+(i*i);
    }
    return result;
}
