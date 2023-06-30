def string_transformation(words, start, stop):
    all_words = list(set([start] + [stop] + words))

    print(all_words)
    adj_list = [[] for _ in range(len(all_words))]

    for i in range(len(all_words)):
        pass


def is_one_off(w1, w2):
    num_diff = 0

    for i in range(len(w1)):
        num_diff += 1 if w1[i] != w2[i] else 0

    return num_diff == 1


# bat -> cat, hat, bad,
# cat -> hat, bat
# bad -> bat, had
# had -> hat, bad
# hat -> cat, bat had


input = {"words": ["cat", "hat", "bad", "had"], "start": "bat", "stop": "had"}

words, start, stop = input["words"], input["start"], input["stop"]
output = string_transformation(words, start, stop)
# print(output)


print(is_one_off("bad", "bad"))
