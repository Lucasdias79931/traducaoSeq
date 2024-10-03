from traducao import tableCodons

def traduction(sequence: str, tableCodons: dict) -> str:
    translated = ""
   
    for i in range(0, len(sequence), 3):
        
        codon = sequence[i:i+3]
        # parada : (TAA, TAG, TGA)
        #print(codon)

        if len(codon) == 3:  
            amino = tableCodons.get(codon, "")
            if amino == "Stop":
                translated += "* (parada)-"
                #print(translated) 
                
            else:
                translated += amino + "-"  
        #print(translated)
    return translated.rstrip("-") 

print(traduction("GCATGAATGTAG",tableCodons))