def get_words_from_phone_number(phone_number):
    mapping = {
        1: [""],
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
        0: [""],
    }

    ret = []
    helper("", mapping, phone_number, ret)
    return ret


def helper(slate, mapping, phone_number, ret):
    if len(phone_number) == 0:
        ret.append(slate)
        return
    else:
        n = phone_number[0]
        for x in mapping[int(n)]:
            print("hi")
            helper(slate + x, mapping, phone_number[1:], ret)


ex = "1234567"

print(get_words_from_phone_number(ex))
