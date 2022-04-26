# move negative numbers on one side of the array

def move(arr):
    pos_index = 0
    for i in range(len(arr)):
        if arr[i]<0:
            arr[pos_index],arr[i] = arr[i],arr[pos_index]
            pos_index += 1
    return arr
def intersection(A,B):
    ans =[]
    for i in range(len(A)):
        j = 0
        flag = True
        for j in range(len(B)):
            if A[i] == B[j]:
                flag = False
                break
        if flag == False:
            ans.append(A[i])
        i += 1
    return ans
A=[1,1,2, 3, 4, 5]
B=[1, 2, 3]
print(intersection(A,B))
def unionBuiltin(A,B):
    x = list(set(A)|set(B))
    return x
def union(a,b,n,m):
    i,j = 0,0
    ans = []
    prev = None
    while i<n and j<m:
        if A[i]<B[j]:
            if A[i] != prev:
                ans.append(A[i])
                prev = A[i]
            i += 1
        elif A[i]>B[j]:
            if B[j] != prev:
                ans.append(B[j])
                prev = B[j]
            j += 1
        elif A[i]==B[j]:
            if B[j] != prev:
                ans.append(A[i])
                prev = A[i]
            i += 1
            j += 1
    while i<n:
        if A[i] != prev:
            ans.append(A[i])
            prev = A[i]
        i += 1
    while j<m:
        if B[j] != prev:
            ans.append(B[j])
            prev = B[j]
        j += 1
    return ans

def union_unsorted(A,B):
    n = len(A)
    m = len(B)
    ans = []
    for i in range(n):
        pass

print(union(A,B,len(A),len(B)))

