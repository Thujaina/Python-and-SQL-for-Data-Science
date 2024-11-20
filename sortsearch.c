#include <stdio.h>

int main() {
    int arr[10], n, ser, i, lower, upper, mid, flag = 0;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    printf("Enter %d elements: ", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Bubble Sort (you can use a more efficient sorting algorithm if needed)
    for (i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    printf("\nSorted array: ");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    printf("\nEnter the element to be searched: ");
    scanf("%d", &ser);

    lower = 0;
    upper = n - 1;

    while (lower <= upper) {
        mid = (lower + upper) / 2;

        if (ser == arr[mid]) {
            flag = 1;
            break;
        } else if (ser < arr[mid]) {
            upper = mid - 1;
        } else {
            lower = mid + 1;
        }
    }

    if (flag == 1) {
        printf("\nElement found at position %d\n", mid);
    } else {
        printf("\nElement not found\n");
    }

    return 0;
}

#output

Enter the number of elements: 5
Enter 5 elements: 89 45 12 67 3

Sorted array: 3 12 45 67 89 
Enter the element to be searched: 67

Element found at position 3

Process finished.
