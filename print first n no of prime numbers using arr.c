
#include<stdio.h>
#include<math.h>
void main(){
    int n,i,j;
    int arr[1000];
    n=printf("Enter the no:");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        arr[i]=i;
    }
    for(i=2;i<=floor(sqrt(n));i++){
        for(j=i+1;j<=n;j++){
            if (j%i==0){
                arr[j]=0;
            }
        }
    }
    printf("Prime nos:\n");
    for(i=2;i<=n;i++){
        if (arr[i]!=0){
            printf("%d\t",arr[i]);
        }
    }
}