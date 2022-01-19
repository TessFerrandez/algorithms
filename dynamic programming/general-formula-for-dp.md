# General formula for dynamic programming

Based on the awesome post [From good to great. How to approach most of DP problems](https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.)

1. Find a recursive relationship
2. Write the recursive function (without worrying about how long time it takes) (top-down)
3. Add memoization/cache to cache the result of the recursive function (top-down)
4. Build an iterative solution (same as the recursive but bottom-up) - building up an array/matrix with solutions for each subproblem
5. Optimize the memory usage of the iterative solution (bottom-up) by figuring out if we can use less variables
