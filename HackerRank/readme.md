Logic for matrix
Ask is to find do the sum of its diagonal elemnts from right side and left side and give the difference
Lets say your matrix is [[8,9,10],[6,2,9],[5,8,6]]

So from the right side, the diagonal elements are 8, 2, 6.

From the left side, the diagonal elements are 10, 2, 5.

If you look closely, there is a pattern:
- `8 = [0][0]`, `2 = [1][1]`, `6 = [2][2]` (Here you see the value of `i` and `j` increment gradually)
- `10 = [0][2]`, `2 = [1][1]`, `5 = [2][0]` (Here `i` increments by 1 and `j` starts at `n` and decreases by 1)
  
