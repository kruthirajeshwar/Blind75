class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        enc = "!@#$%".join(strs)
        return enc
            
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        dec = s.split("!@#$%")
        return dec
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
