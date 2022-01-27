

class Fraction {
 public:
    Fraction(int num, int denom);
    int get_num();
    int get_denom();
    Fraction operator+(Fraction rhs);
 private:
    int m_num;
    int m_denom;
};
