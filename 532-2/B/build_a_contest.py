#   Codeforces
#   #532-2B   -   Build a contest
#   http://codeforces.com/contest/1100/problem/B
#   13/01/2019
#   Nilton G. M. Junior

#   TODO:   Timeout on very large inputs - study possible methods to improv efficiency

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    tests = list(map(int, input().split()))
    test_counts = [0] * n
    output = []
    for test in tests:
        test_counts[test - 1] += 1
        if 0 in test_counts:
            output.append("0")
        else:
            output.append("1")
            test_counts = [test_count - 1 for test_count in test_counts]
    print("".join(output))
