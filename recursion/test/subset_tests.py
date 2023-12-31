tests = [
    {"input": ([2, 4, 8], 6), "output": True},
    {"input": ([2, 4, 6], 5), "output": False},
    {"input": ([0], 0), "output": True},
    {"input": ([1], 0), "output": False},
    {"input": ([50], 50), "output": True},
    {"input": ([-50], 5), "output": False},
    {"input": ([10, 20], 0), "output": False},
    {"input": ([-10, 10], 0), "output": True},
    {"input": ([-5, -10], -15), "output": True},
    {"input": ([8, -11], 8), "output": True},
    {"input": ([-2, 2, 1, 2, 3], 0), "output": True},
    {"input": ([-3, -3, -3, -3], -12), "output": True},
    {"input": ([-2, -3, 1], -4), "output": True},
    {"input": ([-2, -3, 1], -8), "output": False},
    {"input": ([1, 2, 3, 4, 5], 5), "output": True},
    {
        "input": ([-2, -1, 3, -1, -1, -3, 2, 1, -1, 1, -4, -2, 3, 0, 4, 2, -4, -4], 16),
        "output": True,
    },
    {
        "input": ([0, 0, 2, 2, 1, 0, -2, 3, -1, -1, 4, 1, 2, -2, 0, -4, 1, -1], -22),
        "output": False,
    },
]
