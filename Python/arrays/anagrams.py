def anagrams(arr):
    anagram_group={}
    for a in arr:
        sorted_arr="".join(sorted(a))

        if sorted_arr in anagram_group:
            anagram_group[sorted_arr].append(a)
        else:
            anagram_group[sorted_arr]=[s]
    return list(anagram_group.values())

print(anagrams(["cab","abc","tan","van"]))