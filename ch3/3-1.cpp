/*
Program 1 Chapter 3 
Name: Three in One
Descrption: Desribe how you could use a single array to implemented three stacks 
Runtime: 
Date: 4/3/2019
*/

#include <iostream>
#include <array>
using namespace std;




//take in the array number and the item to push 
void push(int arrayNum, int value)
{
    cout << "hi" << endl;
}



int main()
{
    
    array<int,15>myarray; 
    for (int i=0; i<15; i++)
    {
        myarray[i] = 0;
    }

    int size = myarray.size();
    int numArrays = size/3;
    cout << "size of segments: " << numArrays << endl;
    int arr1 = numArrays;
    int arr2 = numArrays*2;
    int arr3 = numArrays*3;
    cout << arr1 << " " << arr2 << " " << arr3 << endl;
    myarray[0] = 1;


    for (int i=0; i<15; i++)
    {
        cout << myarray[i] << " " <<  endl;
    }
    return 0;
}




