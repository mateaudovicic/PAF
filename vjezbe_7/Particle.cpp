#include <iostream>
//#include <bits/stdc++.h>
//#include <stdio.h>
#include <Particle.h>
#include <cmath>
#include <math.h>
#define _USE_MATH_DEFINES
#include <vector>
using namespace std;
#ifndef M_PI
    #define M_PI 3.14159265358979323846
#endif

Particle::Particle(double v0, double alpha0, double x0, double y0, double step)
{ 
  alpha = (alpha0 * M_PI) / 180;
  vx = v0 * cos(alpha);    
  vy = v0 * sin(alpha);
  dt = step;
  r0 = x0;
  t0 = 0.0;
  x = x0;
  y = y0;
};

void Particle::evolve()
{
  while(y >= 0)
  {
    vx += 0.;
    vy += g*dt;
    x += vx * dt;
    y += vy * dt;
    t += dt;
    //xx.push_back(x);
    //yy.push_back(y);
  }
}

double Particle::range()
{
  evolve();  
  double r = x - r0;
  cout << "Range of projectile: " << r << " m" << endl;
  return 0;
}

double Particle::totalTime()
{
  evolve();
  double T = t;
  cout << "Total time: " << T << " s" << endl;
  return 0;
}