# A December of Algorithms
Welcome to A December of Algorithms. This is a small collection of algorithms to implement this December. Finish it all to get a certificate :)

## Index
- [**December 1 - Binary Search**](#december-1---binary-search)
- [**December 2 - Are Triangles Similar**](#december-2---are-triangles-similar)
- [**December 3 - Digit manipulation**](#december-3---fibonacci-series)
- [**December 4 - Fibonacci Series**](#december-4---fibonacci-series)
- [**December 5 - The Hanoi Tower**](#december-5---the-hanoi-tower)

## Algorithms
### **December 1 - Binary Search**
- **Problem**
  - Player A chooses a secret number n. Player B can guess a number x and A replies how does x compare to n (equal, larger, smaller). What's an efficient strategy for B to guess n?
- **Example**
    ```bash
    Say my chosen number is 38. What are you going to do? Do a binary search:
    Guess 50 (half of 0 to 100) → you’re too high.
    Guess 25 (half of 0 to 50) → you’re too low.
    Guess 37 (half of 25 to 50) → you’re too low.
    Guess 43 (half of 37 to 50) → you’re too high.
    Guess 40 (half of 37 to 43) → you’re too high.
    Guess 38 (half of 37 to 40) → spot on!
    ```
- **Resources**
  - [Binary Search](https://www.geeksforgeeks.org/binary-search/)

### **December 2 - Are Triangles Similar**
- **Problem**
  - You have two triangles A1B1C1 and A2B2C2 on a plane. Your task is to determine whether they are rather similar, i.e. if their corresponding angles have the same measurements.       
  - In order for two triangles to be rather similar, the following equations must be true:        
    ```bash
    angle(A1B1, B1C1) = angle(A2B2, B2C2)        
    angle(A1C1, C1B1) = angle(A2C2, C2B2)        
    angle(B1A1, A1C1) = angle(B2A2, A2C2)        
    ```
  - Where angle(AB, CD) refers to an angle between segments AB and CD in the triangle.        
- **Example**
    ```bash
    For coordinates = [0, 0, 0, 1, 1, 0, 0, 0, 0, -3, -3, 0], the output should be        
    areTrianglesSimilar(coordinates) = true.
    ```
- **Resources**
  - Seriously ?!?

### **December 3 - Digit manipulation**
- **Problem**
  - Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.  Given a ticket number n, determine if it's lucky or not.
- **Example**
  ```bash
  For n = 1230, the output should be isLucky(n) = true
  For n = 239017, the output should be isLucky(n) = false
  ```
- **Resources**
  - The basic functionality needed to solve this problem is extracting all the digits from a number and manipulate it according to your needs for which this [link](https://www.youtube.com/watch?v=rporZ07Tc4M) can be used.

### **December 4 - Fibonacci Series**
- **Problem**
  - In mathematics, the Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence, and characterized by the fact that every number after the first two is the sum of the two preceding ones. The problem here is to find the nth number in the series
- **Uses**
  - A great real time application of Fibonacci series that’s used mostly these days as an unknown fact are the mile to kilometer conversion & Kilometer to mile conversion…..
  - Let’s now see the Fibonacci series :
  ```bash
  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,…
  ```
- **Resources**
  - [Video Link](https://youtu.be/wTlw7fNcO-0)

###  **December 5 - The Hanoi Tower**
- **Problem**
  - Let’s slowly spice things up with a simple algorithm, yet, mind-bending if you have never seen it before. Hanoi tower has a beautiful literate solution using recursion.
  - Just think of it, we need to move the largest disk to right tower, first. For that, we need to move all but this disk to middle tower. Hence we are solving the very same problem [twice] with one less disk.
  - To move N disks from left to right:
    - a. [recursively] move N-1 disks from left to middle
    - b. move largest disk from left to right
    - c. [recursively] move N-1 disks from middle to right
- **Sample Run**
    ```bash
    > hanoi(3)
      left => right
      left => middle
      right => middle
      left => right
      middle => left
      middle => right
      left => right
    ```
