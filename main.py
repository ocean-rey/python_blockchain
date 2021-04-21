import time
from hashlib import sha256

class Blockchain:
    def __init__(self, difficulty):
        self.chain = []
        self.difficulty = difficulty
        self.chain.append(Block(0, "Genisis"))

    def AddBlock(self, bNew):
        bNew.prevHash = self.chain[-1].hash
        bNew.MineBlock(self.difficulty)
        return

    def IncDiff(self):
        self.difficulty+= 1;
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
        return digest

    def MineBlock(self, difficulty):
        start = time.time()
        compStr = ""
        for i in range(difficulty) :
            compStr = compStr+'0'
        while True:
            self.nonce += 1;
            self.hash = self.CalculateHash()
            #print(self.hash[0:difficulty])
            if (self.hash[0:difficulty] == compStr):
                break
        stop = time.time()
        duration = stop - start
        print("Block mined:\t{}".format(self.hash))
        print("Difficulty:\t{}".format(difficulty))
        print("kH/s:\t{}".format((self.nonce/1000)/duration))

def main():
    blockchain = Blockchain(1)
    i = 1
    while True:
        blockchain.AddBlock(Block(i, "some data"))
        blockchain.IncDiff()
        i+=1
    return

if __name__ == "__main__":
    main()

