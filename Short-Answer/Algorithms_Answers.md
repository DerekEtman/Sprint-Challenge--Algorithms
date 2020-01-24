#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(1) - where 1 is a, we're simple math functions which take as fast as looking up  

   n = 1
   a = 0
    while (0 < 1 * 1 * 1)
    a = 0 + 1 * 1


b)O(n^2) 
    The functions time is directly proportional to the for & while loop. 

c)O(n) - where n is bunnies
    bunnyears is called n-1 each time, which would also be O(n) 

## Exercise II

building = n
eggs = inf
 find floor = f

Problem : Find the highest floor in which we can drop an egg and not break it, using the least amount of eggs to figure it out.

First pass solution:
    I think we'd want to take a binary approach
    we'd have f(floor) too represent the our highest floor

    splitting up floors into 2 arrays (lower floors & upper floors) testing the mid floor, 
        if the egg breaks at the mid floor 
        switch to lower floor and repeat the process, 

        if the egg doesnt break, 
        f = current floor
        switch to the upper floors and repeat the process halving until we reach the max floor.

        return f
    


