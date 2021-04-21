import time
from hashlib import sha256

class Blockchain:
    def __init__(self):
        self.chain = []
        self.chain.append(Block(0, "Genisis"))

    def AddBlock(self, bNew):
        bNew.prevHash = self.chain[-1].hash
        bNew.MineBlock(5)
        return

class Block:
    def __init__(self, index, data):
        self.data = data
        self.index = index
        self.nonce = -1
        self.time = str(time.time())
        self.prevHash = ""
        self.hash = ""

    def CalculateHash(self):
        hash = sha256()
        hash.update(bytes(self.index))
        hash.update(bytes(self.time, "utf-8"))
        hash.update(bytes(self.data, "utf-8"))
        hash.update(bytes(self.nonce))
        digest = hash.hexdigest()
        #print(digest)
        return digest

    def MineBlock(self, difficulty):
        compStr = ""
        for i in range(difficulty) :
            compStr = compStr+'0'
        print(compStr)
        while True:
            self.nonce += 1;
            self.hash = self.CalculateHash()
            #print(self.hash[0:difficulty])
            if (self.hash[0:difficulty] == compStr):
                break
        print("Block mined:\t{}\nNonce:\t{}".format(self.hash, self.nonce))

def main():
    blockchain = Blockchain()
    blockchain.AddBlock(Block(1, "some data"))
    blockchain.AddBlock(Block(2, "more data"))
    blockchain.AddBlock(Block(3, "even more data"))
    return

if __name__ == "__main__":
    main()

