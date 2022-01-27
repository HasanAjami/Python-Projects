
#include"fibonacci.h"

int* fibonacci(int entries) {
    int* result = new int[entries];
    
    result[0]=0;
    result[1]=1;
    for(int i=2; i < entries; i++){
        result[i]=result[i-2]+result[i-1];
    }
    return result;
}
