numbers = [1,2,4,6,57,5,45,75,68,86,9,3,4,6,12]

def dfs(arr, lo, hi):
    if lo >= hi: 
        return 
    pivot = partition(arr, lo, hi) 
    dfs(arr, lo, pivot -1)
    dfs(arr, pivot +1 , hi) 


def partition(arr, lo, hi):
    pivot = arr[hi]
    idx = lo - 1
    i = lo 

    while i < hi: 
        if arr[i] <= pivot: 
            idx += 1
            tmp = arr[i]
            arr[i] = arr[idx] 
            arr[idx] = tmp
        i +=1
    idx +=1 
    arr[hi] = arr[idx]
    arr[idx] = pivot
    return idx

def quicksort(array): 
    dfs(array, 0, len(array)-1)

print(numbers) 
quicksort(numbers) 
print(numbers) 
