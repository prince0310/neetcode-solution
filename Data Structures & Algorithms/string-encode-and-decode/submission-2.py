class Solution:

    def encode(self, strs: List[str]) -> str:
        temp= ""
        for string in strs:
            temp += string
            temp += ",/"
        return temp

    def decode(self, s: str) -> List[str]:
        return s.split(",/")[:-1]
