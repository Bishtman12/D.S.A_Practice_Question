# Merging Without using extra space
A = [1, 3, 5, 10]
B = [0 ,2 ,6 ,8 ,9]
n = len(A)
m = len(B)
# 1. compare the elements in the first array with that of the second array then swap if not true. Sort the second array.
#. Repeat the process till i==n.Print A and B for the output
def merge(A,B,n,m): # Easy to understand but not optimised
    i = 0
    for i in range(n):
        if A[i] > B[0]:
            temp = A[i] # storing the larger value in temp
            A[i] = B[0] # then updating its value
            B[0] = temp # then swap complete after modifying B[j]
            # here I have to sort the second array
            j = 0
            while j<m-1: # just sorting the array here.(Takes O(n) time because only one element)
                if B[j+1] < B[j]:
                    B[j+1] , B[j] = B[j], B[j+1]
                j += 1
    return A,B
print(merge(A,B,n,m))

def get_gap(gap):
    if gap<=1:
        return 0
    return gap//2 + gap%2

def eff_merge(A,B,n,m):
    gap = n+m
    gap = get_gap(gap)
    while gap>0:
        i = 0
        while gap+i < n: # comparison in the first array.
            if A[i] > A[gap+i]:
                A[i],A[gap+i] = A[gap+i] ,A[i]
            i += 1

        # if the gap is bigger than the arr1 then first element of arr2 will always be skipped
        if gap > n:
            j = gap-n
        else:
            j = 0

        while i<n and j<m: # comparison in two arrays
            if A[i] > B[j]:
                A[i],B[j] = B[j],A[i]
            i += 1
            j += 1

        while j+gap<m:# comparison in the second array
            if B[j] > B[j+gap]:
                B[j] ,B[j+gap] = B[j+gap],B[j]
            j += 1
        gap = get_gap(gap)
    return A,B
print(eff_merge(A,B,n,m))