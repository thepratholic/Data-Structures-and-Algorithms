class Solution:
    def toh(self, n, fromm, to, aux):
        # Your code here
        
        if n == 1:
            print(f"move disk 1 from rod {fromm} to rod {to}")
            return 1
            
        else:
            ans = 0
            ans += self.toh(n-1, fromm, aux, to)
            ans += 1
            print(f"move disk {n} from rod {fromm} to rod {to}")
            ans += self.toh(n-1, aux, to, fromm)
            return ans