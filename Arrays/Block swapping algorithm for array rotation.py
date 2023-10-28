Here, in this page we will discuss the program for Block swap Algorithm in Python. It is one of the most efficient algorithms used for array rotation. Now, let’s discuss about block swap algorithm and a program to rotate an array using the same algorithm.

Block swap algorithm in python
In this section we will learn about basic knowledge which we need to know before coding the above Program. So we must have knowledge of what is an array? 

What is an array?
An array is a data structure, it is collection of similar data elements which is stored at contiguous memory locations in which each data element can be accessed directly by only using its index number.
 
About Python language:-
Python is a popular programming language. Python is a high level language that will make a programmer focus on what to do instead of how to do.
Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale 
 
How to declare an array?
To declare an array in C,a programmer specifies the type of the elements and the number of elements required by an array as follows − This is called a single-dimensional array. The arraySize must be an integer constant greater than zero and type can be any valid C data type. For example, to declare a 10-element array called balanceof type double, use this statement − Here balanceis a variable array which is sufficient to hold up to 10 double numbers
Method Discussed :
Method 1 : Recursive Way
Method 2 : Iterative Way

-------------------------------------------------------------------------------Method 1 :-------------------------------------------------------------------------------

Declare two arrays A and B,
Copy all the elements from index 0 to (d-1) to A[] and from index d to n-1 to B[].
Run a loop till size of array A is equal to size of B[].
If A is longer, divide A into Al and Ar such that Al is of same length as B Swap Al and B to change AlArB into BArAl.
Now B is at its final place, so recur on pieces of A. 
Finally when A and B are of equal size, block swap them.

Method 1 : Code in Python

//Write a program for block swap algorithm in Java
import java.util.*;
 
class Main
{

    public static void leftRotate(int arr[], int d, int n)
    {
        leftRotateRec(arr, 0, d, n);
    }
 
    public static void leftRotateRec(int arr[], int i, int d, int n)
    {

        if(d == 0 || d == n)
            return;
         
        if(n - d == d){
            swap(arr, i, n - d + i, d);
            return;
        }
        
        if(d < n - d){
            swap(arr, i, n - d + i, d);
            leftRotateRec(arr, i, d, n - d);    
        }
        else{
            swap(arr, i, d, n - d);
            leftRotateRec(arr, n - d + i, 2 * d - n, d);
        }
    }
 
    public static void swap(int arr[], int fi, int si, int d){
        int i, temp;
        
        for(i = 0; i < d; i++){
            temp = arr[fi + i];
            arr[fi + i] = arr[si + i];
            arr[si + i] = temp;
        }
    }
 
    public static void main (String[] args){
        int arr[] = {10, 20, 30, 40, 50, 60, 70};
        leftRotate(arr, 2, 7);
    
        for( int i = 0; i < 7; i++)
            System.out.print(arr[i] + " ");
    }
}
Output
30 40 50 60 70 10 20

-------------------------------------------------------------------------------Method 2 :-------------------------------------------------------------------------------

In this method we implement the iterative approach for the algorithm.

Method 2 : Code in Python
#Write a program for block swap algorithm in Python

def leftRotate(arr, d, n):
    if(d == 0 or d == n):
        return;
    i = d
    j = n - d
    while (i != j):
        if(i < j):
            swap(arr, d - i, d + j - i, i)
            j -= i
        else:
            swap(arr, d - i, d, j)
            i -= j
    swap(arr, d - i, d, i)

 
def swap(arr, fi, si, d):
    for i in range(d):
        temp = arr[fi + i];
        arr[fi + i] = arr[si + i];
        arr[si + i] = temp;
 
# Driver Code
arr = [10, 20, 30, 40, 50, 60, 70]
leftRotate(arr, 2, 7)

for i in range(7):
    print(arr[i], end = " ")
Output
30 40 50 60 70 10 20
