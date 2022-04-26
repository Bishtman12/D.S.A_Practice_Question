import random
import sys


def k_smallest_element(arr, l, r, k):
    if (0 < k <= r - l + 1):
        pos = random_partition(arr, l, r)
        if pos - l == k - 1:
            return arr[pos]
        if pos - l > k-1:
            return k_smallest_element(arr, l, pos - 1, k)
        return k_smallest_element(arr, pos + 1, r, k - pos + l - 1)
    return sys.maxsize


def swap(arr, l, r):
    arr[l], arr[r] = arr[r], arr[l]


def partition(arr, l, r):
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= pivot:
            swap(arr, i, j)
            i += 1
    swap(arr, i, r)
    return i


def random_partition(arr, l, r):
    pivot = random.randint(l, r)
    swap(arr, pivot, r)
    return partition(arr, l, r)


if __name__ == '__main__':
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3
    print("K'th smallest element is",
          k_smallest_element(arr, 0, n - 1, k))
