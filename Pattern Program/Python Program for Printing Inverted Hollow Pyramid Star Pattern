
Print Inverted Hollow Pyramid Star Pattern
Let’s look at the program for hollow inverted right triangle star pattern in python.

Enter the Number: 7
 *************
  *         *
   *       *
    *     *
     *   *
      * *
       *
star
Hollow inverted right triangle star pattern in python
Working:
Step 1. Start
Step 2. Take number of rows as input from the user and stored it into num.
Step 3. Run a loop ‘i’ number of times to iterate through all the rows which is Starting from i=0 to num. 
Step 4. Run a nested loop inside the main loop for printing spaces which is starting from j=0 to i.
Step 5. Run a nested loop inside the main loop for printing stars which is starting from j=num*2 to (num*2 – (2*i – 1))+1.
Step 6. Inside the above loop print stars only if i == 1 or j == 1 or j ==(num*2 -(2*i-1)) in all other cases print a blank space.
Step 7. Move to the next line by printing a new line using print() function.
Step 8. Stop
Python Program:
Run
num = int(input("Enter the Number: "))

for i in range(1, num+1):
    for j in range(0, i):
        print(" ", end="")

    for j in range(1, (num*2 - (2*i - 1))+1):
        if i == 1 or j == 1 or j ==(num*2 -(2*i-1)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
Output
Enter the Number: 7
 *************
  *         *
   *       *
    *     *
     *   *
      * *
       *

Process finished with exit code 0
