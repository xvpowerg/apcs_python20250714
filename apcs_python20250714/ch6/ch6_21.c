/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
int main() {
    // Write C code here
    int myArray[2][3] = {
        {1,2,3},
        {4,5,6}
    };
    printf("%d \n",myArray[0][0]);
    printf("%d \n",myArray[1][2]);
    myArray[1][1] = 99;
     printf("%d \n",myArray[1][1]);
    return 0;
}