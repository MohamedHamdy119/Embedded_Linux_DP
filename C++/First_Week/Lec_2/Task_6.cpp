//Write a lambda function to calculate the square of a given number
#include <iostream>

int Number;

int main (){
    auto sqrtno=[]( int no )
{
    return no*no;
};
    std::cout<<"Enter The Number "<<std::endl;
    std::cin>>Number;
    std::cout<<"square of the number is : "<<sqrtno(Number)<<std::endl;

    return 0;
}
