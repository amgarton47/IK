# top-down (i.e. memoization)
def word_break(s: str, word_dict: list[str]) -> bool:
    memo = {}

    def helper(s):
        if s == "" or s in word_dict:
            return True

        can_word_break = False
        for w in word_dict:
            if s.startswith(w):
                sub = s[len(w) :]
                if sub not in memo:
                    memo[sub] = helper(sub)
                can_word_break = can_word_break or memo[sub]

        return can_word_break

    return helper(s)


# bottom-up (tabulation)
# def word_break(s, words_dict):
#     pass


########TRUE##########
s = "leetcode"
wordDict = ["leet", "code"]

s = "applepenapple"
wordDict = ["apple", "pen"]

s = "catscatdog"
wordDict = ["cat", "cats", "dog"]


########FALSE##########
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = [
    "a",
    "aa",
    "aaa",
    "aaaa",
    "aaaaa",
    "aaaaaa",
    "aaaaaaa",
    "aaaaaaaa",
    "aaaaaaaaa",
    "aaaaaaaaaa",
]

s = "acccbccb"
wordDict = ["cc", "bc", "ac", "ca"]

output = word_break(s, wordDict)
print(output)


# 1. recurrence relation:
# T/F - decision problem
# can_be_broken(s) = OR (can_be_broken(s[len(w_i):]) for all i in 0...len(word_dict)


# 2. repeated work?
# cat, sand, dog, cats, and  catsanddog

#            (applepenapple)
#         |                   |
#     sanddog               anddog

# dog                        dog

#  yes, repeated work!

# 3. solve
