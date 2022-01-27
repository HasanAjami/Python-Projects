#include "fraction.h"

Fraction::Fraction(int num, int denom):m_num(num),m_denom(denom) {}

int Fraction::get_num() {
    return m_num;
}

int Fraction::get_denom() {
    return m_denom;
}


Fraction Fraction::operator+(Fraction rhs) {
        int num = m_num*rhs.m_denom+rhs.m_num*m_denom;
        int denom = m_denom*rhs.m_denom;
        return Fraction(num,denom);
}
        
        
