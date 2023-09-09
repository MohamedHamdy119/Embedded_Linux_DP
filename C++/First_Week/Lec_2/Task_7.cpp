//Use lambda functions to sort an array of integers in ascending and descending order
#include <algorithm>
#include <iostream>

int arr[]={3,5,1,9,2,6,10,8,4,7,13,12,11};
int size = sizeof(arr)/sizeof(arr[0]);
int main (){
    auto Sort_Arr=[]( int Arr[],int size )
{
std::sort(Arr,Arr+size);

std::cout <<"descending is: " ;
for (int i = 0; i < size; i++) {
        std::cout << Arr[i] << " ";
    }
    std::cout << std::endl;

std::cout <<"ascending is: " ;
for (int i = (size-1); i >= 0; i--) {
        std::cout << Arr[i] << " ";
    }
    std::cout << std::endl;
};

Sort_Arr(arr, size);
    return 0;
}
