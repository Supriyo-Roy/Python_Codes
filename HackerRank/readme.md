Logic for matrix
Ask is to find do the sum of its diagonal elemnts from right side and left side and give the difference
Lets say your matrix is [[8,9,10],[6,2,9],[5,8,6]]

so from right side the duiginal elemnts are 8,2,6
so from left side the diagonal elemts are 10,2,5

If you look closely , there is a pattern 8 = [0][0] , 2=[1]j[1], 6=[2]j[2] (Here you see the value of i and j is increment gradually)
                                         10 = [0][2], 2=[1][1], 5=[2][0] (here i increments by 1 and j starts at n and decreases by 1)