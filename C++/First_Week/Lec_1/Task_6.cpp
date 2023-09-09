//summation the digits of integer entered by user

#include <iostream>
int NO;
int sum;
int main (){

std::cout << "Enter an Integer : ";
std::cin >> NO;

while(NO!=0)
{
sum+=(NO%10);
NO/=10;
}
std::cout << "Sum of the digits is : "<<sum<<std::endl;
    return 0;
}