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
def getComplement(sequence: dict)->dict:
    seq = next(iter(sequence.items()))
    complement = ""
    
    for nucleotides in seq[1]:
        if nucleotides == "A":
            complement += "T"
        elif nucleotides == "T":
            complement += "A"
        elif nucleotides == "G":
            complement += "C"
        elif nucleotides == "C":
            complement += "G"
    
    return {seq[0]:complement[::-1]}


