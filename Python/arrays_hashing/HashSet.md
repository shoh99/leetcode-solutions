# What is a HashSet

At its code, a HashSet is a data structure that stores a collection of **unique** items. 
Think of it like a club's membership list - you would't list the same name twice.

The most important properties of HashSet are:
1. **Uniqueness**: It automatically handles duplicates. If you try to add an item that's already in the set,
it simply does nothing.
2. Speed: It is incredibly fast for its main operations: adding an item, removing an item, and checking
if an item exists in the set.


The "magic" behind its speed is **hashing**. Every item added to the set is converted into a special index (hash code)
that tells the set almost exactly where to store it is memory. So, when you ask, "Is the number `42` in the set?"
it does not need to look through all the numbers. It just calculates the hash for `42` and checks that one specific spot.

An important side effect of this hashing mechanism is that **HashSets do not maintain the order** in which
you insert the items.

## Why Do We Need HashSet ?

We need HashSets to solve very common problem in programming: **efficiently checking for existence.**

Let's compare it to a regular list (or array) to see why this is so important.

Imagine you have the usernames of one million registered users, and you need to check if a new username,
`cool_user_99` is already taken.

### The List/Array Approach

If you stored the million usernames in a list, you would have to do following:
1. Start at the first username in the list. Is it `cool_user_99`? No.
2. Go to the second username. Is it `cool_user_99`? No.
3. ... continue this process.
4. In the worst case, you have to check all **one million** usernames to confirm if `cool_user_99` is available.

This is **linear search**, which has a time complexity of `O(N)`. As you list `N` grows, the time it takes to
search grows linearly with it. This is very slow for large collections.

### The HashSet Approach
If you stored the million usernames in a HashSet:
1. Tou take the username `cool_user_99` and run it through the hash function.
2. The hash function instantly gives you a memory address.
3. You go directly to that address and see if the username exists here.

This process takes roughly the same amount of time whether you have 100 users or 100 million users.
It's an `O(1)` operation on average - meaning, it takes constant time. This is incredibly fast and efficient.

So we need HashSets for situations like:
1. Finding duplicates in a collection.
2. Checking for membership: In this product ID in our inventory ? Is this word in the dictionary?
3. Databases: Ensuring a column has unique values(like user IDs or emails).
