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


tableCodons = {
    "GCT": "Alanina",
    "GCC": "Alanina",
    "GCA": "Alanina",
    "GCG": "Alanina",
    "TGT": "Cisteína",
    "TGC": "Cisteína",
    "GAT": "Ácido aspártico",
    "GAC": "Ácido aspártico",
    "GAA": "Ácido glutâmico",
    "GAG": "Ácido glutâmico",
    "TTT": "Fenilalanina",
    "TTC": "Fenilalanina",
    "GGT": "Glicina",
    "GGC": "Glicina",
    "GGA": "Glicina",
    "GGG": "Glicina",
    "CAT": "Histidina",
    "CAC": "Histidina",
    "ATT": "Isoleucina",
    "ATC": "Isoleucina",
    "ATA": "Isoleucina",
    "TTA": "Leucina",
    "TTG": "Leucina",
    "CTT": "Leucina",
    "CTC": "Leucina",
    "CTA": "Leucina",
    "CTG": "Leucina",
    "AAA": "Lisina",
    "AAG": "Lisina",
    "ATG": "Metionina",
    "AAT": "Asparagina",
    "AAC": "Asparagina",
    "CCT": "Prolina",
    "CCC": "Prolina",
    "CCA": "Prolina",
    "CCG": "Prolina",
    "CAA": "Glutamina",
    "CAG": "Glutamina",
    "CGT": "Arginina",
    "CGC": "Arginina",
    "CGA": "Arginina",
    "CGG": "Arginina",
    "AGA": "Arginina",
    "AGG": "Arginina",
    "TCT": "Serina",
    "TCC": "Serina",
    "TCA": "Serina",
    "TCG": "Serina",
    "AGT": "Serina",
    "AGC": "Serina",
    "ACT": "Treonina",
    "ACC": "Treonina",
    "ACA": "Treonina",
    "ACG": "Treonina",
    "GTT": "Valina",
    "GTC": "Valina",
    "GTA": "Valina",
    "GTG": "Valina",
    "TGG": "Triptofano",
    "TAT": "Tirosina",
    "TAC": "Tirosina",
    "TAA": "Stop",
    "TAG": "Stop",
    "TGA": "Stop",
}

  


def traduction(sequence: str, tableCodons: dict) -> str:
    translated = ""
   
    for i in range(0, len(sequence), 3):
        
        codon = sequence[i:i+3]
        
        if len(codon) == 3:  
            amino = tableCodons.get(codon, "")
            if amino == "Stop":
                translated += "* (parada)-" 
                
            else:
                translated += amino + "-"  
    
    return translated.rstrip("-")  





## Testes 
if __name__ == "__main__":
    
    print(traduction("GCATGAATGTAG",tableCodons))
    """"
    seqeunce = allSeq[0]

    complemento = getComplement(seqeunce)

    print(f"sequencia:{seqeunce}")
    print(f"complemento:{complemento}")
"""
