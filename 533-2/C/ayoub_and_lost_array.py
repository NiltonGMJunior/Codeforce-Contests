
if __name__ == "__main__":
    n, l, r = list(map(int, input().split()))
    
    count = 0
    arr = [l] * n

    for ind in range(0, n):
        if sum(arr) % 3 == 0:
            count += 1
        
        if arr[n - 1 - ind] < r:
            arr[n - 1 - ind] += 1
        else:
            arr
            continue
