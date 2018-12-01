# A December of Algorithms
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
- [**December 7 - Are they approximately equal?**](#december-7---are-they-approximately-equal)
- [**December 8 - Singular-Plural**](#december-8---singular-plural)
- [**December 9 - Is this an URL?**](#december-9---is-this-an-url)
- [**December 10 - Find the Determinant**](#december-10---find-the-determinant)
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
  - Without Tolerance Level:
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
## FAQ:
#### Who can join the Challenge?
Anyone who is passionate about coding and can dedicate a little time a day for the challenge for the next 31 days.

#### When should I submit the pull request?
You don't need to submit it everyday. Just submit it once you're done with all 31 algorithms.

#### What if I'm not able to code every day?
Not a problem. While coding every day is nice, we understand that other commitments might interfere with it. Plus its holiday season. So you don't have to solve one problem every day. Go at your own pace. One per day or 7 a week or even all 30 in a day.

#### What language should I use to code?
Anything! New to C? Best way to practice it. Wanna find out what all this hype about Python is? Use it! Any and all languages are welcomed. Maybe you could try using a different language for every problem as a mini-challenge?

#### Fork? Pull request? What is all that?
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
