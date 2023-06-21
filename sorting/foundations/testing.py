import random


def test(sorting_func):
    num_test_cases = 100
    input_size = 50
    all_passed = True

    print(f"Running {num_test_cases} tests of input size {input_size}.")
    for n in range(num_test_cases):
        inp = [0] * input_size
        for i in range(len(inp)):
            inp[i] = random.randint(0, 100)

        expected = list(sorted(inp))
        result = sorting_func(inp)
        if result == expected:
            print(f"Test {n} passed.")
        else:
            all_passed = False
            print(f"Test {n} failed.")
            print(f"Input: {inp}, expected: {expected}, result: {result}")
    if all_passed:
        print("All test cases were passed.")
