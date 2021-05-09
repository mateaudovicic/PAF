class Particle 
  {  
    private:
        double t, x, y, vx, vy;  
        double dt;
        double g = -9.81;
        double r0, t0;
        double alpha;

        void evolve();

    public:
        Particle(double v0, double alpha, double x0, double y0, double step = 0.001);
        double range();
        double totalTime();
  };