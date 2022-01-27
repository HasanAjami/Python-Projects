

#include "cylinder.h"

Cylinder::Cylinder(double radius, double height):Circle(radius),m_height(height) {}

double Cylinder::volume() {
    return M_PI*m_radius*m_radius*m_height;
}


