def max_sequence(arr):
    if all(num<0 for num in arr):
        return 0
    max_sum = 0
    for idx in range(len(arr)):
        run_sum = 0
        for item_n in arr[idx:]:
            run_sum += item_n
            if run_sum > max_sum:
                max_sum = run_sum

    return max_sum

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))    # 6