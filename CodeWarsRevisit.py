
### 1

def find_even_index(arr):
    for index in range(len(arr)):
        if sum(arr[:index]) == sum(arr[index+1:]):
            return index
    return -1

    # Possibly O(n^2) or quadratic time complexity because we are performing 2 functions
    # on a list while also moving through a list within a for loop


    def find_even_index(lst):
    left_sum = 0
    right_sum = sum(lst)
    for i, a in enumerate(lst):
        right_sum -= a
        if left_sum == right_sum:
            return i
        left_sum += a
    return -1

    # This solution is linear because it goes through the for loop 1 time
    # and does its math at the same time instead of having to check multiple positions
    # like the first solution

   
### 2

    def parts_sums(ls):
    sums, index = [], 0
    max_sum = sum(ls)
    remaining_sum = 0
    sums.append(max_sum)
    while index < len(ls):
        remaining_sum += ls[index]
        sums.append(max_sum - remaining_sum)
        index += 1
    return sums

    # This solution has linear time complexity because it only loops over the list once
    # However it can still be made more efficient by reducing the number of calculations
    # Needed to solve the problem




  def parts_sums(ls):
    total_sum = sum(ls)
    partial_sum = 0
    sums = [total_sum]

    for num in ls:
        partial_sum += num
        sums.append(total_sum - partial_sum)

    return sums

    # This solution reduces the over all number of calculations while maintaining linear time


## 3

def cakes(recipe, available):
    
    total = {}
    for key in recipe.keys():
        if key in available.keys():
            total[key]=available[key] // recipe[key]
        else:
            return 0
    return min(total.values())
	#0(n)
	

    # removing the .keys and min gets us to true o(n) and allows the computer
    # to do less work even while having a smilar time and space complexity


def cakes(recipe, available):
    count = float('inf')
    for key in recipe:
        if key in available:
            if available[key] // recipe[key] <= count:
                count=available[key] // recipe[key]
        else:
            return 0
    return count