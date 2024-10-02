import os


base_directory = os.getcwd()

sequenceWhay = os.path.join(base_directory, "test/sequencias.fasta")

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

allSequence = getSeq(sequenceWhay)

