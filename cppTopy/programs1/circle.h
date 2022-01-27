

#ifndef CIRCLE_H
#define CIRCLE_H

#include <cmath>

class Circle {
 public:
  Circle(double radius);
  double base_area();

 protected:
  double m_radius;
};


#endif  //  CIRCLE_H
