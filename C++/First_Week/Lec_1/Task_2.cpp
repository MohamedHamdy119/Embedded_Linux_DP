//maximum number between three values
#include <algorithm>
#include <iostream>
int x,y,z;
int main(){
std::cout<<"Enter The First Number: ";
std::cin >>x;
std::cout<<"Enter The Second Number: ";
std::cin >>y;
std::cout<<"Enter The Third Number: ";
std::cin >>z;
int a=std::max({x,y,z});
std::cout<<"The Max Number is : "<<a<<std::endl;
    return 0;
}