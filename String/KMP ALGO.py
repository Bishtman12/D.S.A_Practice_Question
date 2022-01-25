def kmp(pattern, text):
    lps = [0] * len(pattern)
    i, j = 0, 0
    count = 0
    lps = lpsarr(pattern, lps)
    print(lps)
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j!= 0 :
                j = lps[j-1]
            else:
                i += 1
        if j == len(pattern):
            count += 1
            print(f"Starting Index {i-j}")
            j = lps[j-1]
    if count != 0 :
        return f"Total Matches Found {count}"
    else:
        return "No Match Found"

def lpsarr(pattern, lps):
    i = 0
    j = 1
    lps[0] = 0
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            lps[j] = i + 1
            j += 1
            i += 1
        else:
            if i != 0:
                i = lps[i-1]
            else:
                lps[i] = 0
                j += 1
    return lps

A = "onionionspl"
B = "onions"
print(kmp(B,A))