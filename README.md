# Average Numbers:
### This is a Python Program to Calculate the Average of Numbers in a Given List.

## Problem Description:
### The program takes the elements of the list one by one and displays the average of the elements of the list.

## Problem Solution: 
- Take the number of elements to be stored in the list as input.
- Use a for loop to input elements into the list.
- Calculate the total sum of elements in the list.
- Divide the sum by total number of elements in the list.
- Exit.

## Program Explanation:
- User must first enter the number of elements which is stored in the variable n.
- The value of I ranges from 0 to the number of elements and is incremented each time after the body of the loop is executed.
- Then, the element that the user enters is stored in the variable element.
- a.append(elem) appends the element to the list.
- Now the value of i is incremented to 2.
- The new value entered by the user for the next loop iteration is now stored in elem which is appended to the list.
- The loop runs till the value of i reaches n.
- sum(a) gives the total sum of all the elements in the list and dividing it by the total number of elements gives the average of elements in the list.
- round(avg,2) rounds the average upto 2 decimal places.
- Then the average is printed after rounding.
