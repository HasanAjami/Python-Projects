

#include "binary.h"
#include <cmath>

int binary_to_int(std::vector<int> binary) {
    int sum=0;
    int count=0;
    for(int i : binary) {
        
        sum+=std::pow(2,count)*i;
        count=count+1;
    }
    return sum;
}
