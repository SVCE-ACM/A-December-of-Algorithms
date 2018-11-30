# A-December-of-Algorithms
Welcome to A December of Algorithms. This is a small collection of algorithms to implement this December. Finish it all to get a certificate :)
## Algorithms
### **December 1 - Title Here**
- **Problem**
  - Insert Problem Here
- **Example**
  ```bash
   Insert Example Here
  ```
- **Resources**
  - Insert Resources Here

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

###  **December 4 - Big factorial**
- **Problem**
  - Factorial of a non-negative integer is the multiplication of all integers smaller than or equal to n. For example factorial of 6 is 6x5x4x3x2x1 which is 720. Factorial of 100 has 158 digits. It is not possible to store these many digits even if we use long long int. The challenge in this is to implement an algorithm to find the factorial of large numbers
- **Uses**
  - Factorials are used everywhere. We use it when we have to find the numbers of ways in which objects have to be used and also the number of ways they can be arranged. It is used in probability and statistics greatly which is in turn used in a lot of data analysis. But using the normal coding languages we can only find out the factorials of whole numbers up to 13 which is not of much value in these applications hence the need for big factorial.
- **Resources**
  - **factorial(n)**:
  - Create an array ‘res[ ]’ of MAX size where MAX is number of maximum digits in output.
  - Initialize value stored in ‘res[ ]’ as 1 and initialize ‘res_size’ (size of ‘res[ ]’) as 1.
  - Do following for all numbers from x = 2 to n......
  - a) Multiply x with res[ ] and update res[ ] and res_size to store the multiplication result.
    ```bash
    multiply(res[ ], x)
    ```
  - Initialize carry as 0.
  - Do following for i = 0 to res_size – 1 .....
  - a) Find value of res[i] * x + carry. Let this value be prod.
  - b) Update res[i] by storing last digit of prod in it.
  - c) Update carry by storing remaining digits in carry.
  - Put all digits of carry in res[ ] and increase res_size by number of digits in carry

###  **December 5 - File Handling**
- **Problem**
  - Handling files is an integral part of any programming language as it helps us store the result of our operations and it also helps us perform some operation on data. There are two parts to this problem’s implementation which have to be coded as two functions. They are:
  - A function that counts how often each word appears in the text and prints:
    ```bash
    word1 count1
    word2 count2
    ```
  - A function which is similar to the above function but which prints just the top 20 most common words sorted so the most common word is first, then the next most common, and so on.
- **Uses**
  - Using file operations we can read data from a word document or an excel sheet and it can be manipulated in any way we would like.
  - E.g: We use CSV files for machine learning in python
- **Resources**
    - Files in C here : [Link](https://www.programiz.com/c-programming/c-file-input-output)
    - Files in C++ here : [Link](http://www.cplusplus.com/doc/tutorial/files/)
    - Files in Java here : [Link](https://www.tutorialspoint.com/java/java_files_io.htm)
    - Files in python here : [Link](https://www.w3schools.com/python/python_file_handling.asp)
    - An interesting video to visualise sorting : [Link](https://www.youtube.com/watch?v=kPRA0W1kECg)
