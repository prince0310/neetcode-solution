class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)[2:]
        len_x = len(x)
        prev = "0" * (32-len_x) + x 
        desired = "0b" + prev[::-1]
        
        return int(desired,2)
        