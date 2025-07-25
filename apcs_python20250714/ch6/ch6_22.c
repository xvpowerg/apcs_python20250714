/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
int main(){
    
    int myArray[2][3]={
        {1,2,3},
        {4,5,6}
    };
    int i = 0;
    int k = 0;
    for (i = 0; i < 2; i++){
        for (k = 0;k < 3;k++){
            printf("%d ",myArray[i][k]);
        }
        printf("\n");
    }
    
    
    return 0;
}