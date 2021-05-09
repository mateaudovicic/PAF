#include <iostream>
#include <cmath>
#include <math.h>
#define _USE_MATH_DEFINES
#include <vector> 
#include <fstream>
using namespace std;

class HarmonicOscillator
{
    private:                 
        double m, k, x0, v0, dt, T; 
        double a; 
        vector< double > vec_xx;
        vector< double > vec_vv;
        vector< double > vec_aa;
        vector< double > vec_tt;
        double t;

    public:
        HarmonicOscillator(double m_, double k_, double x0_, double v0_, double dt_, double T_)
        {
            m = m_;
            k = k_;
            x0 = x0_;
            v0 = v0_;
            dt = dt_;
            T = T_;
            t = 0;
        }

        double oscillate()
        {   
            while(t < T)
            {
                t += dt;
                a = -(k/m) * x0;
                v0 += a * dt;
                x0 += v0 * dt;
                vec_aa.push_back(a);
                vec_vv.push_back(v0);
                vec_xx.push_back(x0);
                vec_tt.push_back(t);
            }

        ofstream fw;
        fw.open("vectors.txt", ios_base::app);

        if (fw.is_open())           
        {    
            int l1 = sizeof(vec_xx);   
            for (int i = 0; i < l1; i++)
            {  
                fw << vec_xx.at(i);
                fw << " ";
            }
            
        fw << "\n";

            int l2 = sizeof(vec_vv);
            for (int j = 0; j < l2; j++) 
            {  
                fw << vec_vv.at(j);
                fw << " ";
            }

        fw << "\n";

            int l3 = sizeof(vec_aa);
            for (int k = 0; k < l3; k++) 
            {  
                fw << vec_aa.at(k);
                fw << " ";
            }

        fw << "\n";

            int l4 = sizeof(vec_tt);
            for (int l = 0; l < l4; l++) 
            {  
                fw << vec_tt.at(l);
                fw << " ";
            }

        fw.close();
        }

        return 0;

        }
};

int main()
{
    HarmonicOscillator ho(10.0, 0.5, 0.0, 30.0, 0.01, 5.0);
    ho.oscillate();
    return 0;
}