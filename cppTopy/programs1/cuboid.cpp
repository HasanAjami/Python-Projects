

#include "cuboid.h"

Cuboid::Cuboid(double edge_length, double height):Square(edge_length), m_height(height) {}

double Cuboid::volume() {
    return base_area()*m_height;
}


