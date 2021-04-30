#include <iostream>

int main() {
    for(int i=1; i<3; i++)
    {
        std::cout << "Hello world for the " << i << ". time!" <<std::endl;
    }

    int list[6] = {1,2,3,4,5,6};
    for (int i=0; i<6; i++)
    {
        std::cout << list[i] << " ";
    }
    std::cout << std::endl;

    std::string names[3] = {"Jure", "Mate", "Sime"};
    for(int i= 0; i<3; i++)
    {
        std::cout << names[i] << " ";
    }
    std::cout << std::endl;
    std::cout << names << " ";
    return 0;
}