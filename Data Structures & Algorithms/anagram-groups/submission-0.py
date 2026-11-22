from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) ->List[List[str]]:

        dl = defaultdict(list)
        for i in range(len(strs)):

            c = tuple(sorted(strs[i]))

            dl[c].append(strs[i])

        return list(dl.values())

        