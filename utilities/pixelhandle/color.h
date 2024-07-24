#ifndef COLOR_H
#define COLOR_H

#include "vec3.h"

using color = vec3;

// #define EN_ANTIALIASING
inline double linear_to_gamma(double linear_component)
{
    if (linear_component > 0)
        return sqrt(linear_component);

    return 0;
}

#ifdef EN_ANTIALIASING 
    #include "antialiasing.h"
#endif

#ifndef EN_ANTIALIASING 
    #include "noaliasing.h"
#endif

#endif