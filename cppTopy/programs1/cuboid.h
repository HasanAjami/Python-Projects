

#ifndef CUBOID_H
#define CUBOID_H

#include "square.h"

class Cuboid : public Square {
 public:
  Cuboid(double edge_length, double height);
  double volume();

 private:
  double m_height;
};


#endif  // CUBOID_H
