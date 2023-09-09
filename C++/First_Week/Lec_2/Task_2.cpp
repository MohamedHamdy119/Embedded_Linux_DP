//create a function to search to the number in the array which number is taken from user
#include <iostream>

void Find_Number(int arr[],int size, int Number);
int arr1[]={1,2,3,4,5,6,7,8,9,10,11,12,13};
int size;
int No;

int main() 
{
std::cout<<"Enter The Number"<<std::endl;
std::cin>>No;
size=sizeof(arr1)/sizeof(arr1[0]);
Find_Number(arr1,size,No);
    return 0;
}
void Find_Number(int arr[],int size, int Number){
  bool flag =false;
    for (int i =0 ; i< size ; i++) {
        if (arr[i]==Number) {
        flag =true;  
        break;
        }
    }
if (flag == true) {
std::cout<<"Yes,Array contents "<<Number<<std::endl;
}
else
{
std::cout<<"No,Array dosen't content "<<Number<<std::endl;    
}
}