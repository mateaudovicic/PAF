#include <iostream>
#include <cmath>
using namespace std;

// 1. zadatak

void lineEquation(double x1, double y1, double x2, double y2)
{
    double k;
    k = (y2 - y1) / (x2 - x1);
    cout << "The equation of a straight line: y - " << y1 << " = " << k << "(x - " << x1 << ")" << endl;
}


// 2. zadatak

void pointCircle(double p, double q, double r, double x, double y)
{
    double d;
    d = sqrt(pow((x - p), 2.0) + pow((y - q), 2.0));
    if (d > r)
    {
        cout << "The point is not in the circle." << endl;
    }
    else if (d <= r)
    {
        cout << "The point is in the circle." << endl;
    }
}


// 3. zadatak

void setOfNumbers(int array[], int a, int b)
{
    for(int i=a; i<b; i++)
    {
        cout << array[i] << " ";
    }
    cout << "\n";
}

void swappingAllElements(int array[], int N)
{
    int new_array[N];
    for(int i=N-1; i>=0; i--)
    {
        new_array[N-1 - i]=array[i] ;
    }
    for(int i=0; i<N; i++)
    {
        cout << new_array[i] << " ";
    }
    cout << "\n";
}

void swappingTwoElements(int array[], int a, int b)
{
    swap(array[a], array[b]);
    for(int i=0; i<10; i++)
    {
        cout << array[i] << " ";
    }
    cout << "\n";
}


// 4. zadatak

void twoEquationsSolver(double a1, double b1, double c1, double a2, double b2, double c2)
{
    cout << a1 << "x + " << b1 << "y = "<< c1 << endl;
    cout << a2 << "x + " << b2 << "y = " << c2 << endl;

    double x;
    x = (b1 * c2 - b2 * c1) / (a2 * b1 - a1 * b2);
    double y;
    y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1);

    cout << "x = " << x << endl;
    cout << "y = " << y << endl;
}

int main()
{
    lineEquation(9.0, 8.0, 7.0, 5.0);    // 1. zadatak

    pointCircle(5.0, 4.0, 3.0, 2.0, 2.0);   // 2. zadatak

    int array[10] = {1,2,3,4,5,6,7,8,9,10};   // 3. zadatak
    setOfNumbers(array, 3, 8);
    swappingAllElements(array, 10);
    swappingTwoElements(array, 3, 4);
    
    twoEquationsSolver(1.0, 2.0, 3.0, 4.0, 5.0, 6.0);  // 4. zadatak

    return 0;
}