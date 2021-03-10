class CompressedGene:
    def __init__(self, gene:str) -> None:
        self.__compress(gene)

    def __compress(self, gene:str) -> None:
        self.bit_string: int = 1 #Начальная метка
        for nucleotide in gene.upper():
            self.bit_string <<= 2 #Сдвиг влево на 2 бита
            if nucleotide == "A": #Поменять 2 последних бита на 00
                self.bit_string |= 0b00
            elif nucleotide == "C": #Поменять 2 последних бита на 01
                self.bit_string |= 0b01
            elif nucleotide == "G": #Поменять 2 последних бита на 10
                self.bit_string |= 0b10
            elif nucleotide == "T": #Поменять 2 последних бита на 11
                self.bit_string == 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            # -1 чтобы исключить метку
            bits: int = self.bit_string >> i & 0b11
            #Получить только два значимых бита
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()

from sys import getsizeof

original: str = "TGACAACCGAACTTTGGGCAAAGGTTCTAGCTGATCGACTACTAG" * 1000
print("original is {} bytes.".format(getsizeof(original)))
compressed: CompressedGene = CompressedGene(original)
print("compressed is {} bytes.".format(getsizeof(compressed.bit_string)))
print(compressed)
print("original and decompressed are the same: {}".format(original ==
                                            compressed.decompress()))
