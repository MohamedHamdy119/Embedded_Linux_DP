//multiplication table
#include <iostream>

int main (){

std::cout<<"Multiplication Table is :"<<std::endl;
for (int i=1 ; i<=12 ; i++) {
    for (int y=1; y<=12 ; y++) {
        std::cout<<i<<" * "<<y<<" = "<<i*y<<std::endl;
    }
}
    return 0;
}