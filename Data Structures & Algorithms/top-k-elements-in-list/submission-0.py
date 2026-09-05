class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []

        for i in nums:
            count[i] = count.get(i, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            bucket[freq].append(num)
        
        for n in range(len(nums), 0, -1):
            if len(ans) < k:
                for m in bucket[n]:
                    ans.append(m)
            else:
                break
                    
        return ans[:k]