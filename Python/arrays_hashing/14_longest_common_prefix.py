from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    elif len(strs) == 1:
        return strs[0]

    prefix = strs[0]

    for i in range(1, len(strs)):
        current_word = strs[i]

        while not current_word.startswith(prefix):
            prefix = prefix[0:len(prefix) - 1]

            if len(prefix) == 0:
                return ""
    return prefix

if __name__ == "__main__":
    strs =["cir","car"]

    res = longestCommonPrefix(strs)

    print(res)
