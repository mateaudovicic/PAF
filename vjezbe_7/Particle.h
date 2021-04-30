class Particle 
  {  
    private:

        double t, x, y, vx, vy;  
        double dt;
        double g = -9.81;
        double r0, t0;
        double alpha;
        //vector< double > xx;  - error: 'vector' does not name a type; did you mean 'perror'?
        //vector< double > yy;

        void evolve();

    public:
        Particle(double v0, double alpha, double x0, double y0, double step = 0.001);
        //~Particle(); ne radi ako ga otkomentiram  - undefined reference to...

        double range();
        double totalTime();
  };