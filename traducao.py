import os

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
                    sequenceName = ""
                    sequence = ""
        
        return sequences
        
    except Exception as e:
        print(f"Erro: {e}")


# Extrai a fita complementar, inversa
def getComplement(sequence: str) -> str:
    
    complement_map = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    
    complement = []
    
    for nucleotide in sequence:
        complement.append(complement_map[nucleotide])
    
    return ''.join(complement[::-1])





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




    



## EXECUTAR ##

tableCodons = {
    "GCT": "A",  # Alanina
    "GCC": "A",  # Alanina
    "GCA": "A",  # Alanina
    "GCG": "A",  # Alanina
    "TGT": "C",  # Cisteína
    "TGC": "C",  # Cisteína
    "GAT": "D",  # Ácido aspártico
    "GAC": "D",  # Ácido aspártico
    "GAA": "E",  # Ácido glutâmico
    "GAG": "E",  # Ácido glutâmico
    "TTT": "F",  # Fenilalanina
    "TTC": "F",  # Fenilalanina
    "GGT": "G",  # Glicina
    "GGC": "G",  # Glicina
    "GGA": "G",  # Glicina
    "GGG": "G",  # Glicina
    "CAT": "H",  # Histidina
    "CAC": "H",  # Histidina
    "ATT": "I",  # Isoleucina
    "ATC": "I",  # Isoleucina
    "ATA": "I",  # Isoleucina
    "TTA": "L",  # Leucina
    "TTG": "L",  # Leucina
    "CTT": "L",  # Leucina
    "CTC": "L",  # Leucina
    "CTA": "L",  # Leucina
    "CTG": "L",  # Leucina
    "AAA": "K",  # Lisina
    "AAG": "K",  # Lisina
    "ATG": "M",  # Metionina
    "AAT": "N",  # Asparagina
    "AAC": "N",  # Asparagina
    "CCT": "P",  # Prolina
    "CCC": "P",  # Prolina
    "CCA": "P",  # Prolina
    "CCG": "P",  # Prolina
    "CAA": "Q",  # Glutamina
    "CAG": "Q",  # Glutamina
    "CGT": "R",  # Arginina
    "CGC": "R",  # Arginina
    "CGA": "R",  # Arginina
    "CGG": "R",  # Arginina
    "AGA": "R",  # Arginina
    "AGG": "R",  # Arginina
    "TCT": "S",  # Serina
    "TCC": "S",  # Serina
    "TCA": "S",  # Serina
    "TCG": "S",  # Serina
    "AGT": "S",  # Serina
    "AGC": "S",  # Serina
    "ACT": "T",  # Treonina
    "ACC": "T",  # Treonina
    "ACA": "T",  # Treonina
    "ACG": "T",  # Treonina
    "GTT": "V",  # Valina
    "GTC": "V",  # Valina
    "GTA": "V",  # Valina
    "GTG": "V",  # Valina
    "TGG": "W",  # Triptofano
    "TAT": "Y",  # Tirosina
    "TAC": "Y",  # Tirosina
    "TAA": "*",  # Stop
    "TAG": "*",  # Stop
    "TGA": "*",  # Stop
}

base_directory = os.getcwd()

sequenceWhay = os.path.join(base_directory, "test/sequencias.fasta")

allSequence = getSeq(sequenceWhay)

for i in range(len(allSequence)):
    
    sequenceName, sequence = next(iter(allSequence[i].items()))
    complement = getComplement(sequence)
    
    print(f"{i + 1}. {sequenceName}: {sequence}\n")
    for j in range(3):
        print(f"Frame +{j + 1} (Sentido direto):")
        print("DNA: ", end= " ")
        for bases in range(j, len(sequence),3):
            codon = sequence[bases:bases + 3]
            print(f"{codon}", end= " ") 

        # passa sequence a partir do index j usando [j:]
        sequenceTrans = traduction(sequence[j:],tableCodons)

        print(f"\n\nTradução: {sequenceTrans}\n")
    
    
    print(f"Fita complementar (inversa e complementada): {complement}\n")
    for j in range(3):
        print(f"Frame +{j + 1} (Sentido direto):")
        print("DNA: ", end= " ")
        for bases in range(j, len(complement),3):
            codon = complement[bases:bases + 3]
            print(f"{codon}", end= " ") 

        # passa sequence a partir do index j usando [j:]
        complementTrans = traduction(complement[j:],tableCodons)

        print(f"\n\nTradução: {complementTrans}\n")
    
    

