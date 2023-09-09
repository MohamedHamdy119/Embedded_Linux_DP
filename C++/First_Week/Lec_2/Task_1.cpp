//create a function to ﬁnd the maximum number of array
#include <iostream>
int Find_Max(int arr[],int size);
int Find_Max(int arr[],int size){
    int maxNo=0;
for (int i=0 ; i<size ; i++) {
    if (arr[i]>maxNo) {
        maxNo=arr[i];
        }
}
return maxNo;
}
int arr1[10]={1,2,3,4,5,6,7,8,9,10};
int arr2[]={100,5544,569981,484,84,964487,44848,8,7878,48488,8787,848,887,747,9,7,89,8,977};
int main(){
int size=sizeof(arr1)/sizeof(arr1[0]);
int maxNo=Find_Max(arr1,size);
std::cout<<"The max No is : "<<maxNo<<std::endl;
size=sizeof(arr2)/sizeof(int);
maxNo=Find_Max(arr2,arr2[0]);
std::cout<<"The max No is : "<<maxNo<<std::endl;


    return 0;
}