A Harshad number is a positive integer that is divisible by the sum of the digits of the integer. It is also called the Niven number.

For Example : 153
Sum of digits = 1 + 5 + 3 = 9

153is divisible by 9 so 153 is a Harshad Number.
Harshad Number
Algorithm:-
For input num

Initialize a variable sum = 0
Extract each digit of num
Add each digit to sum variable
If at the end num is completely divisible by sum
Then its a harshad’s number
Harshad number in C++
Related Pages
Strong number

Perfect number

Automorphic number

Abundant number

Friendly pair

Code in C++

#include <iostream>
using namespace std;

int checkHarshad(int num){
    
    int sum = 0;
    int temp = num;
    
    while(temp != 0){
        sum = sum + temp % 10;
        temp /= 10;
    }
    
    // will return 1 if num is divisible by sum, else 0
    return num % sum == 0;
}

int main ()
{
    int n = 153;
    
    if(checkHarshad(n))
        cout << n << " is a Harshad's number";
    else
        cout << n << " is not a Harshad's number";

    return 0;
}
// Time complexity: O(N)
// Space complexity: O(1)
// Where N is the number of digits in number
Prime Course Trailer

Related Banners
Output

Enter number: 71
71 is not a harshad number
