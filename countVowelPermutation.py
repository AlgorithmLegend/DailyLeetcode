class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = int(10**9+7)
        kind = 5
        pre = [1]*kind
        cur = [0]*kind
        for _ in range(n-1):
            cur[0]=pre[1]
            cur[1]=pre[0]+pre[2]
            cur[2]=sum(pre)-pre[2]
            cur[3]=pre[2]+pre[4]
            cur[4]=pre[0]
            pre = [i%mod for i in cur]
        return sum(pre)%mod
        
