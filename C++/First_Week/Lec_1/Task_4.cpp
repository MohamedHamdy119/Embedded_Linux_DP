//decide the letter is vowel or not
#include <algorithm>
#include <iostream>
char x;
char y[]={'a','e','i','o','u'};
bool flag =false;
int main(){
std::cout<<"Enter The Leter: ";
std::cin >>x;
x=tolower(x);
for (size_t i = 0; i < 5; i++)
{
    if(x == y[i])
    {
    flag=true;
    break;
    }
}

if(flag==true)
    {
        std::cout<<"The Letter Is Vowel "<<std::endl;
    }
else
{
  std::cout<<"The Letter Is Not Vowel "<<std::endl;  
}
    return 0;
}