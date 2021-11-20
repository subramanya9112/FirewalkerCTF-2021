class XOR:
    def __init__(self):
        # self.key = bytes("HTB{", encoding='utf-8')
        self.key = b'[\x1e\xb4\x9a'
        print(len(self.key))

    def encrypt(self, data: bytes) -> bytes:
        xored = b''
        for i in range(len(data)):
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
        return xored

    def decrypt(self, data: bytes) -> bytes:
        print(len(data))
        return self.encrypt(data)


crypto = XOR()
print(crypto.decrypt(bytes.fromhex("134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9")))
