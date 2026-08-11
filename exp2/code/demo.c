#include <stdio.h>

int main() {
    int y;
    printf("Enter the Year: ");
    if (scanf("%d", &y) != 1) {
        printf("Invalid input\n");
        return 1;
    }
    
    if (y % 4 == 0) {
        if (y % 100 == 0) {
            if (y % 400 == 0)
                printf("%d is a Leap Year\n", y);
            else
                printf("%d is not Leap Year\n", y);
        } else
            printf("%d is a Leap Year\n", y);
    } else
        printf("%d is not Leap Year\n", y);
        
    return 0;
}
