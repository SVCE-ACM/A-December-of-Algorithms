<div align="left">
<h1>
    <img alt="header" src="/src/assets/Header.png" width="900" height="300"></img>
</h1>
Welcome to A December of Algorithms. This is a small collection of algorithms to implement this December. Finish them all to get a certificate :)

**Send a pull request only after completing all 31 algorithms.**

## What Do I Do?
We have a small collection of algorithms, one for every day of the month. Scroll down to take a look at them. All you need to do is fork this repository, implement all 31  algorithms and send a pull request over to us. Check out our FAQ for more information.

## Index
  - [**December 1 - Binary Search**](#december-1---binary-search)
  - [**December 2 - Similar Triangles**](#december-2---similar-triangles)
  - [**December 3 - Lucky Number**](#december-3---lucky-number)
  - [**December 4 - Fibonacci Series**](#december-4---fibonacci-series)
  - [**December 5 - The Tower of Hanoi**](#december-5---the-tower-of-hanoi)
  - [**December 6 - LCM**](#december-6---lcm)
  - [**December 7 - Are They Approximately Equal?**](#december-7---are-they-approximately-equal)
  - [**December 8 - Singular-Plural**](#december-8---singular-plural)
  - [**December 9 - Is This an URL?**](#december-9---is-this-an-url)
  - [**December 10 - Find the Determinant**](#december-10---find-the-determinant)
  - [**December 11 - Printing Matrix In Spiral Form**](#december-11---printing-matrix-in-spiral-form)
  - [**December 12 - Reversing A Singly Linked List**](#december-12---reversing-a-singly-linked-list)
  - [**December 13 - Lexicographical Arrangement**](#december-13----lexicographical-arrangement)
  - [**December 14 - Caesar Cipher**](#december-14---caesar-cipher)
  - [**December 15 - Pascal's Triangle**](#december-15---pascals-triangle)
  - [**December 16 - Find Temperature Difference Between Two Cities**](#december-16---find-temperature-difference-between-two-cities)
  - [**December 17 - Magic Squares**](#december-17---magic-squares)
  - [**December 18 - How Secure is your Password?**](#december-18---how-secure-is-your-password)
  - [**December 19 - Hashing**](#december-19---hashing)
  - [**FAQ**](#faq)

## Algorithms
### **December 1 - Binary Search**
  - **Problem**
    - Player A chooses a secret number n. Player B can guess a number x and A replies how x compares to n (equal, larger, smaller). What's an efficient strategy for B to guess n?
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


### **December 2 - Similar Triangles**
  - **Problem**
    - You have two triangles ABC and PQR on a plane. Your task is to determine whether they are similar.
    - In order for two triangles to be similar, any of these three conditions must be true      
      - The sides of triangle ABC are proportional to the sides of PQR. (SSS Rule)
      `AB/PQ = BC/QR = CA/RP`
      - Two sides of the two triangles are proportional and the angle between the sides is the same for both triangles. (SAS Rule)
      `AB/PQ = BC/QR AND angle(ABC) = angle(PQR)`
      - If any two angles of one triangle are equal to any two angles of the other triangle. (AA Rule)
      `angle(ABC) = angle(PQR) AND angle(BCA) = angle(QRP) AND angle(CAB) = angle(RPQ)`    
  - **Example**
      ```bash
      Input:
      side1 = [2, 3, 3] angle1 = [80, 60, 40]
      side2 = [4, 6, 6] angle2 = [40, 60, 80]
      Output: Triangles are similar by SSS AAA SAS
      ```
  - **Resources**
    - You just need to find the ratio between the sides of the triangle and compare the angles.
    - Remember that the input triangles may be rotated around. For the problem given above, if `side2 = [6. 6. 4]` and `angle2 = [80, 60, 40]`, the triangles are still similar.


### **December 3 - Lucky Number**
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
    - A great real-time application of Fibonacci series that’s used mostly these days as an unknown fact is the [mile to kilometre conversion & Kilometer to mile conversion](http://www.catonmat.net/blog/using-fibonacci-numbers-to-convert-from-miles-to-kilometers/)…..
    - Let’s now see the Fibonacci series :
    ```bash
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,…
    ```
  - **Resources**
    - [Video Link](https://youtu.be/wTlw7fNcO-0)


###  **December 5 - The Tower of Hanoi**
  - **Problem**
    - Let’s slowly spice things up with a simple algorithm, yet, mind-bending if you have never seen it before. Hanoi tower has a beautiful literate solution using recursion.
    - Say we have 3 towers. The first tower consists of a number of disks with the smallest ones at the top and the largest ones at the bottom. The second and third tower have no disks.
    - Your task is to move all the disks from the first tower to the third hour while following these rules:
      - Only one disk can be moved at a time.
      - You may only move a disk that is at the top of a tower. You cannot move any disk without first moving disks that are above it.
      - No disk may be placed on top of a smaller disk.
    - You have only certain fixed moves:
      - `left-right`, `left->middle`
      - `middle->left`, `middle->right`
      - `right->left`, `right->middle`
    - Your input will be a number indicating the total number of disks on the first (left) tower.    
  - **Example**
      ```bash
      > Hanoi(3)
        left => right
        left => middle
        right => middle
        left => right
        middle => left
        middle => right
        left => right
      ```
  - **Resources**
    - [The Tower of Hanoi - Visualized](https://www.mathsisfun.com/games/towerofhanoi.html)


###  **December 6 - LCM**
  - **Problem**
    - Return the least common multiple of two or more numbers.
    - Use the `greatest common divisor (GCD)` formula and the fact that `lcm(x,y) = x * y / gcd(x,y)` to determine the least common multiple.
    - **Hint:** There are multiple ways to implement GCD Take a leap and try doing it with recursion.
    - `Optional:` Allow for input of more than 2 numbers and find the comined LCM of all the numbers.
  - **Example**
    ```bash
    Input: 12, 7
    Output: 84
    Optional Input: 2, 3, 6, 12, 24
    Output: 24
    ```
  - **Resources**
    - [Greatest Common Factor]( https://www.mathsisfun.com/greatest-common-factor.html)


###  **December 7 - Are they approximately equal?**
  - **Problem**
    - Checks if two numbers are approximately equal (i.e. Closer using the concept of rounding numbers) to each other or not.
    - `Optional:` Most languages have a built in function to round a number. Can you implement the rounding function by yourself?
    - `Optional:` Add a third parameter `Tolerance level` that sets an acceptable threshold level. If the difference between the two numbers is more than the threshold value, then the output will be false.
  - **Example**
    - Without Tolerance Level:
    ```bash
    IsApproximatelyEqual(3.0, 2.5706) -> true
    ```
    - With Tolerance Level:
    ```bash
    IsApproximatelyEqual(3.0, 2.5706, 0.01) -> false as the difference is more than the Tolerance Level
    ```


###  **December 8 - Singular-Plural**
  - **Problem**
    - Returns the singular or plural form of any regular noun based on the input number.
    - Let `num` be the second integer parameter.
    - If `num` is either `-1 or 1`, return the singular form of the word. If `num` is any other number, return the plural form.
    - Also if the second arguments is a string (rather than an integer), then print the singular and plural word out of the inputs provided.
    - `Optional:` To spice things up, use a dictionary file to compare give the appropriate outputs. Therefore this will cover Irregular nouns in it too.
  - **Example**
    ```bash
    > SingularPlural("Apple", 2)
        Apples
    > SingularPlural("Apple", 1)
        Apple
    > SingularPlural("Apples", 1)
        Apple
    > SingularPlural("Apples", "Apple")
        Singular: Apple
        Plural: Apples
    > SingularPlural("Apples", "Orange")
        Invalid Input
    ```
  - **Resources**
    - [Plural Nouns: Rules and Examples](https://www.grammarly.com/blog/plural-nouns/)


###  **December 9 - Is this an URL?**
  - **Problem**
    - Returns `true` if the given string is an absolute URL, `false` otherwise.
    - **Hint:** Regular Expressions can be used to solve this problem.
  - **Example**
    ```bash
    > IsURL("https://duckduckgo.com/?q=test+string&atb=v143-2__&ia=web")
      True
    > IsURL("Martha?")
      False
    > IsURL("https://duckduckgo")
      False
    ```
  - **Resources**
    - [Regular Expressions in C++](http://www.cplusplus.com/reference/regex/)
    - [Regular Expressions in Python](https://www.tutorialspoint.com/python/python_reg_expressions.htm)
    - [Regular Expressions in Java](https://www.javatpoint.com/java-regex)


###  **December 10 - Find the Determinant**
  - **Problem**
    - Find the Determinant of any 2x2 or 3x3 input matrix. Multiply all the values in a column or row with all values in other columns or row, sum them up… and it works!
    - `Optional:` Find the determinant for a matrix of any order (4x4 and above).
  - **Example**
    ```bash
    Input Array(X):
      4  9  2
      3  5  7
      8  1  6
    determinant(X)
      360.0
    ```
  - **Resources**
    -[Matrix: Determinant](https://www.mathsisfun.com/algebra/matrix-determinant.html)


### **December 11 - Printing Matrix in Spiral Form**
  - **Problem**
    - Given a Matrix of size `M * N`, output its elements in spiral form.
    - To better understand the problem statement, consider the following matrix
    ```
    01     02     03
    04     05     06
    07     08     09
     ```
    - The Spiral form of a matrix is as below.
      ```
      01 --> 02 --> 03 --> 06 --> 09 --> 08 --> 07 --> 04 --> 05
      ```
    - Move Right, Move Down, Move Left, Move Up till you cover all elements of matrix.
  - **Uses**
    - Matrices are used much more in daily life than people would have thought or noticed.
    - Matrices find numerous applications in scientific fields and apply to practical real-life problems as well, thus making an indispensable concept for solving many practical problems.
    - [Applications of matrices in real life problems](https://www.ukessays.com/essays/mathematics/application-of-matrices-in-real-life-problems.php)
  - **Resources**
    - Matrices are represented using n-dimensional arrays where n is the order of the matrix. In this case have a 2-D matrix, so you will need to use a 2-D array. You need to use two variables to access an element of the matrix. The first variable is used to denote row while the second denotes the column. To traverse the entire matrix, you will need to use two loops.
    - [Operations on Matrices](https://www.geeksforgeeks.org/different-operation-matrices/)


### **December 12 - Reversing a Singly Linked List**
  - **Problem**
    - Given a singly linked list, output a linked list containing the same elements but in reverse order.
    - `Optional:` Complete the task without creating a new list. I.E., reverse the linked list in-place.
  - **Example**
    ```
    Input:
      10 -> 20 -> 34 -> 23 -> 889
    Output:
      889 -> 23 -> 34 -> 20 -> 10
    ```
  - **Uses**
    - There are pretty good real examples to show the usage and importance of linked-list.
    - Consider the history section of web browsers, where it creates a linked list of web-pages visited, so that when you check history (traversal of a list) or press back button, the previous node's data is fetched.
    - One commonly cited example is low level memory management (i.e. the heap as managed by `malloc` in C or new in Java, etc) is often implemented as a linked list, with each node representing a used or available (free) block of memory. These blocks may be of any size, change size (combine and split), be freed or assigned in any order, and reordered. A linked list means you can keep track of all of these "nodes" and manipulate them fairly easily.
    - Also, Hash-tables that use chaining to resolve hash collisions typically have one linked list per bucket for the elements in that bucket.
  - **Resources:**
    - [This is how linked lists work](https://www.youtube.com/watch?v=NobHlGUjV3g)


### **December 13 -  Lexicographical Arrangement**
  - **Problem**
    - Given an input string, find all possible permutations of this string. Arrange these permutations in alphabetical order and find the position at which the input string occurs.
  - **Example**
    ```
    Input:
      dac
    Possible combinations:
      acd
      adc
      cad
      cda
      dac --> Match Found at Position 5
      dca
    ```  
      - The output for this will be `5` as `dac` is present in the 5th position in the alphabetical list of permutations.
  - **Uses and Resources**
    - This question is a brain teaser and though it may not seem to have any practical application, it is used in various areas such as Crypto-Analysis and Brute-forcing cryptographic keys.

  ### **December 14 - Caesar Cipher**
  - **Problem**
    - The Caesar cipher is one of the earliest known ciphers. Simply put, it should take in an input of a 'key' and some plain text. This key will be a number from 0-25. Your task is to simply replace each character of the message with a new character. This new character is the key-th element from the old character. Check out the examples for better understanding. Also, develop a function to decrypt the given cipher when you are given the key.
    - `Optional:` The Caesar cipher is trivial for modern computers to crack, even without the key. Write a program that bruteforces the cipher. Bruteforcing means simply trying out every possible combination. So in this case, try out every possible key to decode the cipher.
  - **Example #1:**
    ```
    Input: and 3
    Encoded output: dqg
    ```
  - **Example #2:**
    ```
    Input: feel 4
    Encoded output: jiip
    ```
  - **Resources**
    - [More on the Caesar Cipher](http://practicalcryptography.com/ciphers/caesar-cipher)


### **December 15 - Pascal's Triangle**
  - **Problem**
    - Pascal's Triangle is a triangle(represented as a 2-D array) in which the ends of the rows are 1. Each of the other values is equal to the sum of the two nearest numbers in the row above.
    - The pascal’s triangle is given as:
    ```
  	                    1
                    1          1
               1          2        1
           1         3         3      1
      1       4          6         4     1
    ```
    - Up To any number of rows. The task here is to generate a pascal’s triangle for n rows and using this find `(x+y)^n`
  - **Example**
  ```
  Sample input:
  rows = 3
  Sample output:
  1       --> row 0
  11      --> row 1
  121     --> row 2
  1331    --> row 3
  Polynomial: (1x^3y^0)+(3x^2y^1)+(3x^1y^2)+(1x^0y^3)
  ```
  - **Uses**
    -  The numbers in Pascal's triangle have another name: Binomial coefficient, and they show up a bunch.
    - There is a formula for finding them, but for smaller numbers it's about as easy, or easier, to use the triangle as it is the formula.
  - **Application**
    - **Binomial Expansion**
        - What is (a+b)^4? It's a pain to do by hand.
        - It's not hard to realize your final answer will contain the terms a^4, a^3b, a^2b^2, ab^3, and b^4.
        - What is a pain is figuring out the coefficients.
        - Enter Pascal's Triangle.
        ```
        The coefficients correspond to the 5 values in the 4th row of the triangle

                                1
                          1          1
                     1          2        1
                 1         3         3      1
            1        4          6         4     1

        The polynomial is (a+b)^4 = a^4+4a^3b+6a^2b^2+4ab^3+b^4
        ```
    - **Binomial Probability Distributions**
        - If the probability of rolling a die 5 times and getting exactly 2 sixes?
        - Some might say it's (1/6)^2 (two sixes) times (5/6)^4 (four non-sixes).They'd be wrong. As it turns out, this is just the probability of one possibility, like getting two sixes first, then three non-sixes, or a six at the beginning and the end.
        - The good news is that all these possibilities have the same probability, and the bad news is we have to add them all up to find the probability of exactly 2 sixes.
        - We could just multiply if we knew how many combinations there were in total.Enter pascal's triangle (or binomial coefficients.) If you want the number of combinations that leads to 0 successes in 5 tries, you go to the first number on the 5th row of Pascal's triangle. For one you go to the 2nd, and for two you go to the 3rd.
        ```
        1   5   10   10   5   1
        ```
        - At a glance we can see the number of possibilities for 0, 1, 2, 3, 4, and 5 successes in 5 trials. To find the probability of 2 sixes, we just have to multiply (1/6)^2(5/6)^4 by 10.
  - **Resources:**
    - [More about pascals triangle and how they work](https://www.youtube.com/watch?v=YUqHdxxdbyM)


### **December 16 - Find Temperature Difference Between Two Cities**
  - **Problem**
    - It’s getting harder to turn around in tech without bumping into some reference to APIs, or application programming interfaces. In the simplest terms, applications talk to each other via APIs.
    - Usually, when we use an API to retrieve data (known as an API Call), we receive a JSON file containing data. To access this data, we will need to parse the JSON file. Depending on the language you are using, there are different ways to parse it. Just Google how to parse a JSON file in your language.
    - OpenWeatherMap is a popular service that provides satellite images, Weather data, Historical data and Soil temperature and moisture.
    - The problem is to find the current temperature difference between `London, GB` and `Chennai, Tamil Nadu, India` using the OpenWeatherMap API.
    - `Note #1:` OpenWeatherMap APIs need a valid API key to allow responses, Packages won't work if you don't provide one. You can signup for a free API key on the OpenWeatherMap website.
    - `Note #2:` API keys are private and **should not be made public**. When committing your code, please make sure you replace your original API key with a dummy key.
    - `Note #3:`Alternatively, you can look into saving your API key as an Environment Variable.
    One final alternative is to simply store the API key in a text file and add that file to your `.gitignore` file. When you need to access it, open the file using your program and retrieve the API key.


  - **Sample Output**
    ```
    Taken at 20:35 (IST), 04-12-2018
    Current Temperature difference between Chennai,TN and London,GB is 19°C
    ```
  - **Resources:**
    - [How to get your API key from OpenWeatherMap](https://openweathermap.org/appid)
    - [How to retrieve weather data for a city](https://openweathermap.org/current#name)


### **December 17 - Magic Squares**
  - **Problem**
    - A magic square of order n is an arrangement of ``n^2`` numbers, containing distinct integers from ``1`` to ``n^2``, in a square, such that the ``n`` numbers in all rows, all columns, and both diagonals sum to the same constant.
    - This constant is called the magic constant or magic sum, M, which is given by:
        ```math
        M = n(n^2+1)/2
        ```
    - Now the problem is to generate all the possible magic squares if the order of the square and magic sum is given as input.
    - Try it out for `Order = 4` and `Magic Sum = 34`
    - `Hint:` It will be helpful if you breakdown the problem. First generate one magic square. Before generating the others, look at the other squares in the example carefully, you will notice something very useful.

  - **Example**

   <img src="/src/docs/Dec17-Example.png" width="375" height="288"/>

  - **Resources**
    - [Magic Squares #1](https://mindyourdecisions.com/blog/2015/11/08/how-many-3x3-magic-squares-are-there-sunday-puzzle/)
    - [Magic Square #2](https://en.wikipedia.org/wiki/Magic_square)


### **December 18 - How Secure is your Password?**
  - **Problem**
    - Brute Force Attack is the most widely known password cracking method. This attack simply tries to use every possible ASCII printable characters (character code 32-126) combination as a password. Though brute forcing can be a little exhaustive, the likelihood of a password being cracked is made certain.
    - The problem is to use the length of the string to find the maximum time that will be taken by a system to crack a given password using Brute Force Attack. The larger the time, the stronger the password is.
    - Assume **500,000** passwords can be tested per second.
    - `Note:` That while this is a pretty cool concept, in the real world you don't really have the liberty of attempting so many different passwords on a website. You might have noticed that if you enter a wrong password enough times you may be locked out of your account. Instead hackers obtain `hashes` from data breaches. When they attempt to brute-force a password, they first hash it using the same algorithm that was used on the original password. They then compare each generated hash with a hashed password to see if they match.


  - **Optional Task**
    - `Optional #1:` Perform a check for dictionary attack before checking for brute-force by directly comparing the input password with each password in the **.txt** file in the reference.
    - `Optional #2:` To make their password tougher to crack, people often substitute letters with numbers. O becomes 0 for example. Think of other such replacements. Strengthen your dictionary attack by implementing a way to substitute these letters.

  - **Examples**
    ```
    Enter Password: h3lL0
    Maximum time taken to brute-force: 13326.48 sceonds
    ```
    ```
    Enter Password: abc
    Maximum time Taken to brute-force: Instantly
    ```

  - **Resources**
    - [1000 most commonly used password](/src/docs/Dec18-1000_most_common_passwords.txt)
    
    
### **December 19 - Hashing**
  - **Problem**
    - A hash function is any function that can be used to map data of arbitrary size to data of a fixed size. Hash functions are often used in combination with a hash table, a common data structure used for rapid data lookup.
    - Consider a simple hash function:
        ```
        int simpleHash(item) {
            return item % 10;
        }
        ```
        ```
        Input: simpleHash(77)
        Output: 7
        Input: simpleHash(3)
        Output: 3
        Input: simpleHash(908)
        Output: 8
        ```
    - As you see, each input is mapped to an output of fixed size.
    - Now, implement a hash function that takes a string of variable length and returns an integer with a fixed maximum number of digits. Try to come up with your own method of returning a fixed length hash. The simplest method would be to just use a 3-digit length of the string. 001, 042, 340 for 1, 42 and 340 characters respectively. But that's no fun.
    - **Hint:** Try something with the ASCII values of each word maybe.
    
  - **_Optional Problem_**
    - Hash functions may return the same output for various inputs. This is known as collision. There are two main collision resolution techniques:
      - [Separate Chaining](https://youtu.be/_xA8UvfOGgU)
      - [Open Addressing](https://youtu.be/Dk57JonwKNk)
    - Implement a hash table with one of the collision resolution techniques mentioned above.
    
  - **Uses**
    - As mentioned above, hash functions are often used in combination with a hash table for rapid data lookup.
    - They are also useful in cryptography. A cryptographic hash function allows one to easily verify that some input data maps to a given hash value, but if the input data is unknown, it is deliberately difficult to reconstruct it (or any equivalent alternatives) by knowing the stored hash value.
    - Cryptographic hash functions also play a crucial role in blockchains.
    
  - **Resources**
    - [Hash function – Wikipedia](https://en.wikipedia.org/wiki/Hash_function)
    - [Hash table - Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
    - [An in-depth video about cryptocurrencies, blockchain and hash functions](https://youtu.be/bBC-nXj3Ng4)
    

FAQ:
======
  #### Who can join the Challenge?
  Anyone who is passionate about coding and can dedicate a little time a day for the challenge for the next 31 days.

  #### When should I submit the pull request?
  You don't need to submit it everyday. Just submit it once you're done with all 31 algorithms.

  #### What if I'm not able to code every day?
  Not a problem. While coding every day is nice, we understand that other commitments might interfere with it. Plus its holiday season. So you don't have to solve one problem every day. Go at your own pace. One per day or 7 a week or even all 30 in a day.

  #### What language should I use to code?
  Anything! New to C? Best way to practice it. Wanna find out what all this hype about Python is? Use it! Any and all languages are welcomed. Maybe you could try using a different language for every problem as a mini-challenge?

  #### Fork? Pull request? What is all that? I don't know how to use GitHub!
  If you are new to Git or GitHub, check out this [small tutorial.](https://guides.github.com/activities/hello-world/)

  #### Where are the rest of the problems?
  Our code ninjas are hard at work preparing the rest of the problems. Don't worry, they'll be up soon.

  #### How should I complete these programs?
  We have a folder for each day of the month. Simply complete your code and move the file into that folder. Be sure to rename your file to the following format: `language_username` or `language_username_problemname`
  Some examples:
  `python_exampleUser.py`
  `c_exampleUser.c`
  **Please do not modify any existing files in the repository.**

  #### I forked the repository but some problems were added only after that. How do I access those problems?
  Not to worry! Open your nearest terminal or command prompt and navigate over to your forked repository. Enter these commands:
  ```bash
  git remote add upstream https://github.com/SVCE-ACM/A-December-of-Algorithms.git
  git fetch upstream
  git merge upstream/master
  ```
  If you're curious, the commands simply add a new remote called upstream that is linked to this repository. Then it 'fetches' or retrieves the contents of the repository and attempts to merge it with your progress.

  #### I received a merge error. What do I do?
  This shouldn't happen unless you modify an existing file in the repository. There's a lot of potential troubleshooting that might be needed, but the simplest thing to do is to make a copy of your code outside the repository and then clone it once again. Now repeat the steps from the answer above. Merge it and then add your code. Now proceed as usual. :)

  #### I'm facing difficulties with/need help understanding a particular question.
  Open up an [issue](https://github.com/SVCE-ACM/A-December-of-Algorithms/issues) on this repository and we'll do our best to help you out.M

###### [[Back to Top]](#----)
