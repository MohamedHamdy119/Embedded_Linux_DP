// merge two arrays together
#include <iostream>

void Merge_Array(int arr1[], int size1 ,int arr2[],int size2,int Merg_Arr[]);

int arr1[]={1,2,3,4,5,6,7,8,9,10,11,12,13};
int arr2[]={14,15,16,17,18,19,20,21,22,23,24,25,26};
int Merg_Arr[]={};
int size1 = sizeof(arr1)/sizeof(arr1[0]);
int size2 = sizeof(arr2)/sizeof(arr2[0]);

int main(){

Merge_Array(arr1 , size1 , arr2 , size2 , Merg_Arr);

for (int i = 0; i <(size1+size2) ; i++ ) {
    std::cout << Merg_Arr[i] << " ";
}
    std::cout << std::endl; 
    return 0;
}
void Merge_Array(int arr1[], int size1 ,int arr2[],int size2,int Merg_Arr[]){
for (int i = 0 ; i < size1 ; i++ ) {
    Merg_Arr[i]=arr1[i];
}

for (int i = size1 ; i< (size1+size2) ; i++ ) {
    Merg_Arr[i]=arr2[i-size1];
}
std::cout <<"Done................"<<std::endl;
}