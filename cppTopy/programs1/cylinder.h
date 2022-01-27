

#ifndef CYLINDER_H
#define CYLINDER_H

#include "circle.h"

class Cylinder : public Circle {
 public:
  Cylinder(double radius, double height);
  double volume();

 private:
  double m_height;
};


#endif  //  CYLINDER_H
