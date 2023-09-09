//delete number in array
#include <iostream>

void Delete_Number(int arr[] , int size ,int Number);
int arr1[]={1,2,3,4,5,6,7,8,9,10,11,12,13};
int size;
int No;


int main(){

std::cout<<"Enter The Number"<<std::endl;
std::cin>>No;
size=sizeof(arr1)/sizeof(arr1[0]);

for (int i = 0; i < size; i++) {
        std::cout << arr1[i] << " ";
    }
    std::cout << std::endl;
    
Delete_Number(arr1, size , No);

for (int i = 0; i < size; i++) {
        std::cout << arr1[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}



void Delete_Number(int arr[] , int size ,int Number){
   bool flag =false;
   int fno=0;
    for (int i =0 ; i< size ; i++) {
        if (arr[i]==Number) {
        flag =true;
        fno=i;  
        break;
        }
    }
if (flag == true) {
for (int y =fno ; y< size-1 ; y++) {
        arr[y]=arr[y+1];
        }
        std::cout<<"Done.......... "<<std::endl; 
    }
else
{
std::cout<<"No,Array dosen't content "<<Number<<std::endl;    
} 

}