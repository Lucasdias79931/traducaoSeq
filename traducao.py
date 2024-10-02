import os
import numpy as np


base_directory = os.getcwd()

sequenceWhay = os.path.join(base_directory, "test/sequencias.fasta")

# Extrai todas as sequencias de um arquivo
def getSeq(sequenceWhay: str) -> list:
    try:
        sequences = list()

        with open(sequenceWhay) as file:
            sequenceName = ""
            sequence = ""

            for line in file:
                if line.startswith(">"):
                    sequenceName = line.strip().replace(">", "")
                else:
                    sequence = line.strip()

                if sequenceName and sequence:
                    sequences.append({sequenceName:sequence})
        
        return sequences
        
    except Exception as e:
        print(f"Erro: {e}")


# Extrai a fita complementar, inversa
def getComplement(sequence: dict) -> dict:
    seq = next(iter(sequence.items()))
    complement_map = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    
    complement = []
    
    for nucleotide in seq[1]:
        complement.append(complement_map[nucleotide])
    
    return {seq[0]: ''.join(complement[::-1])}


## Testes 
if __name__ == "__main__":
    allSeq = getSeq(sequenceWhay)

    seqeunce = allSeq[0]

    complemento = getComplement(seqeunce)

    print(f"sequencia:{seqeunce}")
    print(f"complemento:{complemento}")

