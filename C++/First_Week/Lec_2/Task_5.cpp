// ﬁnd the even and odd numbers in the array
#include <iostream>
#include <string>

void od_ev_find(int arr[],int size);

int arr1[]={1,2,3,4,5,6,7,8,9,10,11,12,13};
int size = sizeof(arr1)/sizeof(arr1[0]);

int main (){
od_ev_find(arr1, size);
    return 0;
}

void od_ev_find(int arr[],int size){
    std::string oddnu="";
    std::string evennu="";

for (int i=0;i<size;i++){
    if(arr[i]%2 == 0)
    {
        evennu += (std ::to_string(arr[i])+" "); 
    }

    else if(arr[i]%2 != 0)
    {
        oddnu += (std ::to_string(arr[i])+" "); 
    }

}    
std::cout<<"The Even Numbers is: "<<evennu<<std::endl;
std::cout<<"The Odd Numbers is: "<<oddnu<<std::endl;
}
