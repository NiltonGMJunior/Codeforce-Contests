if __name__ == "__main__":
    num_sticks = int(input()) # Number of sticks
    stick_lengths = list(map(int, input().split())) # Sticks' lengths

    min_t = 0
    min_cost = sum(stick_lengths)


    for t in range(min(stick_lengths), max(stick_lengths) + 1):
        cost = 0
        for stick_length in stick_lengths:
            if abs(stick_length - t) > 1:
                cost += abs(stick_length - t) - 1
        if cost < min_cost:
            min_cost = cost
            min_t = t

    print(min_t, min_cost)