def can_sum(target_sum, numbers, memo=None):
    # check if list of integers in numbers can add up to target_sum
    # all numbers in list can be re-used as often as needed
    assert isinstance(target_sum, int)
    assert isinstance(numbers, list) or isinstance(numbers, tuple)
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers, memo) is True:
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False


if __name__ == '__main__':
    print(can_sum(3, [2, 4]))
