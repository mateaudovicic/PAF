#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;


void setOfNumbers(int array[], int a, int b)
{
    for(int i=a; i<b; i++)
    {
        cout << array[i] << " " ;
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
    for(int i=0; i<N-1; i++)
    {
        cout << new_array[i] << " " ;
    }
}

void swappingTwoElements(int array[], int a, int b)
{
    swap(array[a], array[b]);
    for(int i=0; i<10; i++)
    {
        cout << array[i] << " " ;
    }
}



/*void swappingAllElements(int list[])
{
    reverse(&list[0], &list[0] + sizeof(list));
    for (i=0; i < sizeof(list)/2; i++)
    {
        swap(list[i], list[sizeof(list) - i -1]);
    }
    for(int i=0; i<10; i++)
    {
        cout << list[i] << " " ;
    }
    cout << "\n";
}*/



int main()
{
    int array[10] = {1,2,3,4,5,6,7,8,9,10};
    setOfNumbers(array, 3, 8);
    swappingAllElements(array, 10);
    swappingTwoElements(array, 3, 4);
    return 0;
}