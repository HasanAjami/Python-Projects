
#include "circle.h" 

Circle::Circle(double radius):m_radius(radius) {}

double Circle::base_area() {
    return M_PI*m_radius*m_radius;
}
