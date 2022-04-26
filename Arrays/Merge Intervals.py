A = [[4,5],[1,5]]
def Brute_Force(A):
    A.sort(key = lambda x:x[0]) # sorting w.r.t to the keys in the array A.
    ans = []
    index = 1
    flag = False
    while index<len(A):
        if A[index-1][1] >= A[index][0]:
            ans.append((A[index-1][0],A[index][1]))
            flag = True
            index += 1
        else:
            ans.append(A[index])
            index += 1
    if flag == False:
        return A
    return ans

def optimised(A):
    A.sort(key = lambda x:x[0])
    ans = [A[0]] # [1,5]
    for start,end in A[1:]: #[4,5]
        lastEnd = ans[-1][1] # 5
        if start <= lastEnd: # 4<5
            ans[-1][1] = max(lastEnd,end) # 5
        else:
            ans.append([start,end]) # 1,5
    return ans
print(optimised(A))

print(f"Brute Force Method-->{Brute_Force(A)}")
