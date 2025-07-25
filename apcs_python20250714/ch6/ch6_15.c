/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
int main() {
    // Write C code here
    int action =2;
    if ( action == 1){
        
        printf("Play");
    }else if(action == 2){
        printf("Stop");
    }else if(action == 3){
        printf("Exit");
    }else{
        printf("Error");
    }
 
    
    return 0;
}