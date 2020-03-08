MNT = []
MDT = []
def pass1(source_code):
    for i in range(len(source_code)):
        if(source_code[i]=="Macro"):
            MNT.append(source_code[i+1])
            j = i + 1
            while(source_code[j]!="MEND"):
                MDT.append(source_code[j])
                j+=1
            MDT.append(source_code[j])
            i = j
    print(MNT,MDT)

def pass2(source_code):
    output = open("output.txt","a")
    for i in range(len(source_code)):
            if(source_code[i] in MNT):
                if(source_code[i-1]!="Macro"):
                    m = MDT.index(source_code[i])
                    for j in range(m+1,11000):
                        if(MDT[j]=="MEND"):
                            break
                        else:
                            output.write(MDT[j])
                            output.write('\n')
            else:
                output.write(source_code[i])
                output.write('\n')
    print(output)

                    
source_code = [line.strip() for line in open("input.txt")]
print(source_code)
pass1(source_code)
pass2(source_code)