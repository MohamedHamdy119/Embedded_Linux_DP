//change from decimal to binary and vice versa
#include <iostream>
#include <bitset>

short x ;
int main(){
std::cout<<"Enter a decimal number: ";
std::cin>>x;
std::bitset<8> Bi_Rep(x);  
std::cout<<"Binary representation: "<<Bi_Rep<<std::endl;
//***********************************************************
std::cout<<"Enter a binary number: ";
std::bitset<8> x;
std::cin>>x;
std::cout << "Decimal representation: " <<x.to_ulong()<<std::endl;

  return 0;
}