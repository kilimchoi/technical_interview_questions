Technical Interview Questions
=============================

**General**
- Find the most frequent integer in an array
- Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time)
- Given 2 integer arrays, determine of the 2nd array is a rotated version of the 1st array.
  
    ```Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}```
- Write fibbonaci iteratively and recursively (bonus: use dynamic programming)
- Find the only element in an array that only occurs once.
- Find the common elements of 2 int arrays
- Implement binary search of a sorted array of integers
- Implement binary search in a rotated array (ex. {5,6,7,8,1,2,3})
- Use dynamic programming to find the first X prime numbers
- Write a function that prints out the binary form of an int
- Implement parseInt
- Implement squareroot function
- Implement an exponent function (bonus: now try in log(n) time)
- Write a multiply function that multiples 2 integers without using *
- **HARD**: Given a function rand5() that returns a random int between 0 and 5, implement rand7()
- **HARD**: Given a 2D array of 1s and 0s, count the number of "islands of 1s" (e.g. groups of connecting 1s)

**Strings**
- Find the first non-repeated character in a String
- Reverse a String iteratively and recursively
- Determine if 2 Strings are anagrams
- Check if String is a palindrome
- Check if a String is composed of all unique characters
- Determine if a String is an int or a double
- **HARD**: Find the longest palindrome in a String
- **HARD**: Print all permutations of a String
- **HARD**: Given a single-line text String and a maximum width value, write the function 'String justify(String text, int maxWidth)' that formats the input text using full-justification, i.e., extra spaces on each line are equally distributed between the words; the first word on each line is flushed left and the last word on each line is flushed right

**Trees**
- Implement a BST with insert and delete functions
- Print a tree using BFS and DFS
- Write a function that determines if a tree is a BST
- Find the smallest element in a BST
- Find the 2nd largest number in a BST
- Given a binary tree which is a sum tree (child nodes add to parent), write an algorithm to determine whether the tree is a valid sum tree
- Find the distance between 2 nodes in a BST and a normal binary tree
- Print the coordinates of every node in a binary tree, where root is 0,0
- Print a tree by levels
- Given a binary tree which is a sum tree, write an algorithm to determine whether the tree is a valid sum tree
- Given a tree, verify that it contains a subtree.
- **HARD**: Find the max distance between 2 nodes in a BST.
- **HARD**: Construct a BST given the pre-order and in-order traversal Strings

**Stacks, Queues, and Heaps**
- Implement a stack with push and pop functions
- Implement a queue with queue and dequeue functions
- Find the minimum element in a stack in O(1) time
- Write a function that sorts a stack (bonus: sort the stack in place without extra memory)
- Implement a binary min heap. Turn it into a binary max heap
- **HARD**: Implement a queue using 2 stacks






**Linked Lists**
- Implement a linked list (with insert and delete functions)
- Find the Nth element in a linked list
- Remove the Nth element of a linked list
- Check if a linked list has cycles
- Given a circular linked list, find the node at the beginning of the loop. 

    ```Ex. A-->B-->C --> D-->E -->C, C is the node that begins the loop```
- Check whether a link list is a palindrome
- Reverse a linked list iteratively and recursively

**Sorting**
- Implement bubble sort
- Implement selection sort
- Implement insertion sort
- Implement merge sort
- Implement quick sort

**BSTs, Heaps, Search Algorithms, Sort Algorithms, Intersection, median, hashmap, caching system, basic algorithms** 

- Basic bitwise operations
- How do you program a min heap using Nodes
- Find the max value in an array. The array is "semi-sorted". 

    ```Ex. { 1 3 4 7 9 10 12 13 12 6 3 }```
- Write a code that accepts integers as arrays and outputs the multiplication result as an array.
- Write a code that takes the coordinates of multiple rectangles as input and returns as output the coordinates of the rectangle that is the intersection of all the rectangles.
- Typical low level CS questions about sorting algorithms and operational cost.
- Median finding algorithm - find the median of 'n' numbers and a little bit of binary search tree implementation
- Find the largest rectangle with all 0s in an matrix with only 0 and 1.
- Convert char string to integer. 
- Find occurrences of a number in sorted array (allow duplicates). 
- If integer array used to store big integers (one integer store one digit), implement arithmetic operations.
- How to build a heap?
- What is the optimized version of the knn algorithm?
- Write a recursive function to calculate pascal's pyramid numbers. 
- A question related to binary search, which is a kind of weak spot and I always avoid using it.
- Explain Singleton structure, how to create
- Given k sorted pivots, write procedure partition in quicksort
- Find the median of three numbers.
- Generate all balanced parentheses combinations of given length.
- The second question asked, how to find two missing integers in an unsorted array
- Given an array of characters in it, how would you reverse it?
- Write a program to comparing two array, one being very large
- To generate a fibonacci number sequence, and discuss its time and space complexity
- To merge two sorted integer arrays.
- Returning the n-th element of a linked list.
- How to randomly select a number with equal probability from an array with unknown size?
 Write an algorithm to find the 3rd highest number from an array of random integers
- Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array. Sorted in increasing order

    ```Input: find 5 in (15, 16, 19, 20, 25, 1, 3, 4, 5, 6, 10, 14) Output 8```

**Uncategorized**
- Given a max-heap, how do I find the top k items?
- Find the border length created from a conglomeration of various 2D rectangles.
- Write a minPeak function for a stack (function that returns the minimum element in the stack).
- Find the nth fib number
- Design a function in your favorite programming language to convert a camelCase string to all lowercase.
- Implement a hashset
- Given a corpus of valid words, design a function that takes a word as input and outputs all valid anagrams of that word. 
- Given an input of a 3D matrix of ones and zeros, count the number of contiguous 1-filled regions (as separated by 0-filled regions), as well as the size of the largest one (I think; doesn't really change the problem much).
- You have two sets. How would you know that they converge.
- Given a bag of nuts and a bag of bolts, each having a different size within a bag but exactly one match in the other bag, give a fast algorithm to find all matches
- Preorder traversal without recursion
- Find the largest possible difference in an array of integers, such that the smaller integer occurs earlier in the array.
- How to find if n numbers in a list sum up to an integer k?
- Find largest palindrome in string
- Make an anagram solver that returns all valid dictionary words given a set of characters.
- Sort a string by the order it's characters appear in another string
- Given a value k and an array , design an efficient algorithm that should output the number of pairs that sum up to k.
- How do you find three numbers that sum to 0? (in a list). Now can you do it under O(n^3)?
- Given a Fibonacci number, tell us which index it occurs at.
- Describe an algorithm that would find n numbers in a list that sum to 0.
- Given an array of n unsorted ints, with the condition that each number is at most k positions away from its final sorted position, give an efficient sorting algorithm
- Give an efficient solution for subset sum.
- Given two (i,j) coordinates of a cell in two dimensional matrix. These coordinates are the lower left and upper right corner of a rectangle contained within the matrix. Sum all the elements in the matrix. Time and space?
- String has all unique characters
- Two strings to see if one is a permutation
- Remove dups from an unsorted linked list
- Find kth algorithm of singly linked list
- Delete a node in the middle of a singly linked list given access to that node
- Write code to partition a linked list around a value x such that all nodes less than x come before all nodes greater than or equal to x
- Single array to implement three stacks
- Stack with min element
- Towers of Hanoi
- Queue using two stacks
- Sort a stack in ascending order using at most one additional stack to hold items but you may not copy the elements into any other data structure
- Function to see if a tree is balanced
- Graph algorithm, route between two nodes
- Create bst from sorted array with minimal height
- Binary tree is a bst
- A child is running up a staircase with n steps, and cah hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs
- Two sorted arrays, A has a large enough buffer at the end to hold B, merge B into A in sorted order
- Write a method to sort an array of strings so that all the anagrams are next to each other
- Find an element in a sorted array that has been rotated an unknown number of times
- Implement a method that returns true if the edit distance between two strings is less than 2 (1 or 0) or false otherwise
