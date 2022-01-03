def best_sum(target_sum, numbers, memo=None):
    # find smallest list of numbers to match target
    # can re-use numbers in list

    assert isinstance(target_sum, int)
    assert isinstance(numbers, tuple) or isinstance(numbers, list)
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_result = None
    result = None

    for num in numbers:
        remainder = target_sum - num
        result = best_sum(remainder, numbers, memo)
        if result is not None:
            combination = result.copy()
            combination.append(num)  # this adds extra values when not needed???
            if shortest_result is None or len(combination) < len(shortest_result):
                shortest_result = combination.copy()

    # if shortest_result is not None:
    #     memo[target_sum] = shortest_result.copy()
    # else:
    #     memo[target_sum] = None
    memo[target_sum] = shortest_result
    return memo[target_sum]


if __name__ == '__main__':
    print(f'{best_sum(100, [1, 2, 5, 25])}  # expected [25, 25, 25, 25]')
    print(f'{best_sum(8, [3, 7])}  # expected is None')
