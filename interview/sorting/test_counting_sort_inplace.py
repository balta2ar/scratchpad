import random


print('TEST')

def counting_sort_inplace(numbers, K):
    #K = 3 #10 * 56
    counts = [0] * K
    print('AAA', numbers)

    for x in numbers:
        counts[x] += 1
    # print('COUNTS 1', counts)
    current_sum = 0
    last_count = None
    for i, x in enumerate(counts):
        counts[i], current_sum = current_sum, current_sum + counts[i]
        last_count = x
    orig_counts = counts[:]
    expected_counts = counts[1:] + [counts[-1] + last_count]
    # print('COUNTS START', counts)
    # print('EXPECTED COUNTS', expected_counts)
    # print('NUMBERS START', numbers)

    def is_processed(i, bucket):
        # print('IS_PROCESSED', i, bucket)
        low = orig_counts[bucket]
        high = counts[bucket]
        # print('IS_PROCESSED', low, i, high)
        return low <= i < high

    def swap(i, j):
        # print('SWAP', i, j)
        numbers[i], numbers[j] = numbers[j], numbers[i]

    for i, _ in enumerate(numbers):

        while not is_processed(i, numbers[i]):
            bucket = numbers[i]
            new_index = counts[bucket]
            swap(i, new_index)
            counts[bucket] += 1
            # print('NUMBERS', numbers)
            # print('COUNTS', counts)

    assert expected_counts == counts
    assert sorted(numbers) == numbers
    print('BBB', numbers)

    return counts


def test_counting_sort_inplace(n_iterations, max_K, max_N):
    random.seed()
    for i in range(n_iterations):
        N = random.randint(1, max_N-1)
        numbers = [random.randint(0, max_K-1) for _ in range(N)]
        counting_sort_inplace(numbers, max_K)


test_counting_sort_inplace(10000, 10, 10)


#numbers = [1, 1, 1, 0, 0, 0]
#numbers = [1, 1, 1, 0, 2, 2, 0, 2, 2, 0, 1, 1]
#numbers = [1, 1, 2, 0]
#numbers = [1, 2, 2, 0, 2, 0, 1, 1] # there was index error
#numbers = [1, 0, 2, 0, 2, 0, 1]
# print('BEFORE', numbers)
#counts = counting_sort_inplace(numbers, 3)
# print('AFTER', numbers)
# print('COUNTS', counts)

# print('DONE')
