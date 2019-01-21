#   Codeforces
#   #532-2A   -   Roman and Browser
#   http://codeforces.com/contest/1100/problem/A
#   13/01/2019
#   Nilton G. M. Junior

#   TODO:   Doesn't work for following input:
#   20 19
#   -1 -1 1 1 -1 1 1 -1 1 1 -1 1 -1 1 1 1 -1 1 -1 1
#   Expected output is 5, yielded output is 4

# if __name__ == '__main__':
#     n, k = list(map(int, input().split()))
#     tabs = list(map(int, input().split()))
#     max_diff = 0
#     for b in range(n // k):
#         open_tabs = [tab for tab in tabs]
#         i = 0
#         while b + i * k < n:
#             open_tabs.remove(tabs[b + i * k])
#             i += 1
#         if abs(open_tabs.count(1) - open_tabs.count(-1)) > max_diff:
#             max_diff = abs(open_tabs.count(1) - open_tabs.count(-1))
#     print(max_diff)

