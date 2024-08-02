#https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem?h_l=interview&isFullScreen=true&page=1&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two

#Count sort Algorithm

# we have to retun only the frequency
def countingSort(arr):
    count =[0] *100
    for nums in arr:
        count[nums]+=1
    return count    
    