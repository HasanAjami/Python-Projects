

#include"mean.h"

double mean_even_numbers(std::list<int> input) {
    
    double sum = 0;
    double n=0;
    for (auto i : input) {
        if ((i%2)==0) {
            sum=sum+i;
            n=n+1;
        }
    }
    if (n==0) {
        return 0;
    }
    else{
        return sum/n;
        
    }
    }
