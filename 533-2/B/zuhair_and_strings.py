import re

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    s = input()

    pattern = r'([a-z])(\1{' + str(k - 1) + r'})'
    matches = re.findall(pattern, s)
    level = 0
    for match in matches:
        if matches.count(match) > level:
            level = matches.count(match)
    print(level)