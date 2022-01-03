def how_sum(target_sum, numbers, memo=None):
    # return a list of numbers which matches the sum of target_sum
    # or return null value (None in python)

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

    result = None

    for num in numbers:
        remainder = target_sum - num
        result = how_sum(remainder, numbers, memo)
        if result is not None:
            result.append(num)
            memo[target_sum] = result
            return result

    memo[target_sum] = None
    return None
