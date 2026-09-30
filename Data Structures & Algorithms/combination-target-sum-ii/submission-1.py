from collections import Counter
import copy
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        arr = sorted(candidates)
        while arr and arr[-1] > target:
            arr.pop()
        count = Counter(arr)
        arr = list(set(arr))
        def permute(arr, cur, dic, total):
            if total > target:
                return
            for key, val in dic.items():
                if val > count[key]:
                    return
            if total == target:
                output.append(cur)
                return 
            for i in range(len(arr)):
                new_dic = copy.deepcopy(dic)
                new_dic[arr[i]] += 1
                permute(arr[i:], cur + [arr[i]], new_dic, total + arr[i])
        d = defaultdict(int)
        permute(arr, [], d, 0)
        return output