# Authors: Henry Sampson, Karim, Eric
# SIC instruction encoding format:
# ~~: R0/R1
# --: R2/R3
# ii: immediate
# lw    p 000 xx yy
# sw    p 001 xx yy
# add   p 100 ~~ --
# addi  p 100 -- ii
# sub   p 010 ~~ --
# subi  p 010 -- ii
# sltR0 p 011 ~~ --
# seqR0 p 011 -- ~~
# xor   p 110 ~~ --
# and   p 110 -- ~~
# init  p 101 ~~ ii
# sll   p 101 -- ii
# j     p 111 0i ii
# beqR0 p 111 1i ii
# Halt  p 111 11 11
# -----------------------------------------------------------

print("ECE366 Fall 2018 mini SIC compiler")
input_file1 = open("p3_group_3_p1_imem.txt", "r")
input_file2 = open("p3_group_3_p2_imem.txt", "r")
input_fileA = open("patternA.txt", "r")
input_fileB = open("patternB.txt", "r")
input_fileC= open("patternC.txt", "r")
input_fileD= open("patternD.txt", "r")
output_fileA = open("p3_group_3_dmem_A.txt", "w")
output_fileB = open("p3_group_3_dmem_B.txt", "w")
output_fileC = open("p3_group_3_dmem_C.txt", "w")
output_fileD = open("p3_group_3_dmem_D.txt", "w")
register = []  # registers

i = 0
while i < 4: #allocate 4 registers
    register.append(0)
    i = i + 1

Rx = 0  # first argument
Ry = 0  # second argument (register)
im = 0  # second argument (immediate)

instruction_Count = 0
print("flag1")
instruction_Memory = []  # create instruction memory
data_Memory = []  # create data memory
pattern = [] #data from patterns

i = 0;
while i < (2**16 - 1):  # allocate data memory space
    data_Memory.append(0)
    i = i + 1
print("flag2")
for line in input_fileA:
    pattern.append(line)
print("flag3")

#for line in input_file1:  # allocate instruction memory
    #instruction_Memory.append(line)
for line in input_file2:
    instruction_Memory.append(line)
print("flag4")
i = 0
while i < len(pattern):
    data_Memory[i] = int(pattern[i], 2)
    i = i + 1
print("flag5")
i = 0 #PC
while i < len(instruction_Memory):
    print("Instruction Line " + str(i) + ": " + "R[0]->" + str(register[0]) + " " + "R[1]->" + str(register[1]) + " " + "R[2]->" + str(register[2]) + " " + "R[3]->" + str(register[3]) + "\n")
    if (instruction_Memory[i][1:4] == '000'):  # lw
        if(instruction_Memory[i][4:6] == '00'):
            Rx = 0
        elif(instruction_Memory[i][4:6] == '01'):
            Rx = 1
        elif(instruction_Memory[i][4:6] == '10'):
            Rx = 2
        else:
            Rx = 3
        if (instruction_Memory[i][6:8] == '00'):
            Ry = 0
        elif (instruction_Memory[i][6:8] == '01'):
            Ry = 1
        elif (instruction_Memory[i][6:8] == '10'):
            Ry = 2
        else:
            Ry = 3

        register[Rx] = data_Memory[register[Ry]]

    elif (instruction_Memory[i][1:4] == '001'):  # sw
        if(instruction_Memory[i][4:6] == '00'):
            Rx = 0
        elif(instruction_Memory[i][4:6] == '01'):
            Rx = 1
        elif(instruction_Memory[i][4:6] == '10'):
            Rx = 2
        else:
            Rx = 3
        if (instruction_Memory[i][6:8] == '00'):
            Ry = 0
        elif (instruction_Memory[i][6:8] == '01'):
            Ry = 1
        elif (instruction_Memory[i][6:8] == '10'):
            Ry = 2
        else:
            Ry = 3
        data_Memory[register[Ry]] = register[Rx]

    elif (instruction_Memory[i][1:4] == '100'):  # add/addi
        if(instruction_Memory[i][4:5] == '0'):
            if (instruction_Memory[i][4:6] == '00'):
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                Rx = 2
            else:
                Rx = 3
            if (instruction_Memory[i][6:8] == '00'):
                Ry = 0
            elif (instruction_Memory[i][6:8] == '01'):
                Ry = 1
            elif (instruction_Memory[i][6:8] == '10'):
                Ry = 2
            else:
                Ry = 3
            register[Rx] = register[Rx] + register[Ry]
        else:
            if (instruction_Memory[i][4:6] == '00'):
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                Rx = 2
            else:
                Rx = 3
            if (instruction_Memory[i][6:8] == '00'):
                im = 0
            elif (instruction_Memory[i][6:8] == '01'):
                im = 1
            elif (instruction_Memory[i][6:8] == '10'):
                im = 2
            elif (instruction_Memory[i][6:8] == '11'):
                im = 3
            register[Rx] = register[Rx] + im


    elif (instruction_Memory[i][1:4] == '010'):  # sub/subi
        if(instruction_Memory[i][4:5] == '0'):
            if (instruction_Memory[i][4:6] == '00'):
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                Rx = 2
            else:
                Rx = 3

            if (instruction_Memory[i][6:8] == '00'):
                Ry = 0
            elif (instruction_Memory[i][6:8] == '01'):
                Ry = 1
            elif (instruction_Memory[i][6:8] == '10'):
                Ry = 2
            else:
                Ry = 3
            register[Rx] = register[Rx] - register[Ry]
        else:
            if (instruction_Memory[i][4:6] == '00'):
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                Rx = 2
            else:
                Rx = 3
            if (instruction_Memory[i][6:8] == '00'):
                im = 0
            elif (instruction_Memory[i][6:8] == '01'):
                im = 1
            elif (instruction_Memory[i][6:8] == '10'):
                im = 2
            elif (instruction_Memory[i][6:8] == '11'):
                im = 3
            register[Rx] = register[Rx] - im

    elif (instruction_Memory[i][1:4] == '011'):  # sltR0/seqR0
        if(instruction_Memory[i][4:5] == '0'):
            if (instruction_Memory[i][4:6] == '00'):
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                Rx = 2
            else:
                Rx = 3
            if (instruction_Memory[i][6:8] == '00'):
                Ry = 0
            elif (instruction_Memory[i][6:8] == '01'):
                Ry = 1
            elif (instruction_Memory[i][6:8] == '10'):
                Ry = 2
            else:
                Ry = 3
            if (register[Rx] < register[Ry]):
                register[0] = 0
            else:
                register[0] = 1
        else:
            if (instruction_Memory[i][4:6] == '00'):
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                Rx = 2
            else:
                Rx = 3
            if (instruction_Memory[i][6:8] == '00'):
                Ry = 0
            elif (instruction_Memory[i][6:8] == '01'):
                Ry = 1
            elif (instruction_Memory[i][6:8] == '10'):
                Ry = 2
            else:
                Ry = 3
            if (register[Rx] == register[Ry]):
                register[0] = 0
            else:
                register[0] = 1

    elif (instruction_Memory[i][1:4] == '110'):  # xor/and
        first = 0
        if (instruction_Memory[i][4:5] == '0'):
            first = 0
        else:
            first = 1
        if (instruction_Memory[i][4:6] == '00'):
            Rx = 0
        elif (instruction_Memory[i][4:6] == '01'):
            Rx = 1
        elif (instruction_Memory[i][4:6] == '10'):
            Rx = 2
        else:
            Rx = 3

        if (instruction_Memory[i][6:8] == '00'):
            Ry = 0
        elif (instruction_Memory[i][6:8] == '01'):
            Ry = 1
        elif (instruction_Memory[i][6:8] == '10'):
            Ry = 2
        else:
            Ry = 3
        if (first == 0):
            register[Rx] = register[Rx] ^ register[Ry]  # bitwise xor
        else:
            register[Rx] = register[Rx] & register[Ry]  # bitwise and

    elif (instruction_Memory[i][1:4] == '101'):  # init/sll
        if(instruction_Memory[i][4:5] == '1'):
            if (instruction_Memory[i][4:6] == '00'):
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                Rx = 2
            else:
                Rx = 3
            if (instruction_Memory[i][6:8] == '00'):
                im = 0
            elif (instruction_Memory[i][6:8] == '01'):
                im = 1
            elif (instruction_Memory[i][6:8] == '10'):
                im = 2
            elif (instruction_Memory[i][6:8] == '11'):
                im = 3
            register[Rx] = register[Rx] << im
        else:
            if (instruction_Memory[i][4:6] == '00'):
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                Rx = 2
            else:
                Rx = 3
            if (instruction_Memory[i][6:8] == '00'):
                im = 0
            elif (instruction_Memory[i][6:8] == '01'):
                im = 1
            elif (instruction_Memory[i][6:8] == '10'):
                im = 2
            elif (instruction_Memory[i][6:8] == '11'):
                im = 3
            register[Rx] = im

    elif (instruction_Memory[i][1:4] == '111'):  # j/beqR0
        if (instruction_Memory[i][4:5] == '0'):
            if (instruction_Memory[i][5:8] == '000'):
                im = 0
            elif (instruction_Memory[i][5:8] == '001'):
                im = 1
            elif (instruction_Memory[i][5:8] == '010'):
                im = 2
            elif (instruction_Memory[i][5:8] == '011'):
                im = 3
            elif (instruction_Memory[i][5:8] == '100'):
                im = 4
            elif (instruction_Memory[i][5:8] == '101'):
                im = 5
            elif (instruction_Memory[i][5:8] == '110'):
                im = 6
            else:
                im = 7
            i = i - 5**im - 1
        else:
            if (instruction_Memory[i][5:8] == '000'):
                im = 0
            elif (instruction_Memory[i][5:8] == '001'):
                im = 1
            elif (instruction_Memory[i][5:8] == '010'):
                im = 2
            elif (instruction_Memory[i][5:8] == '011'):
                im = 3
            elif (instruction_Memory[i][5:8] == '100'):
                im = 4
            elif (instruction_Memory[i][5:8] == '101'):
                im = 5
            elif (instruction_Memory[i][5:8] == '110'):
                im = 6
            else:
                 instruction_Memory[i] = instruction_Memory[i].replace('beqR0 111', 'Halt')
            if (register[0] == 0):
                i = i + 5**im - 1
            else:
                i
    else:
        ##############print("Unknown instruction:" + instruction_Memory[i])
        instruction_Count = instruction_Count - 1
    instruction_Count = instruction_Count + 1
    i = i + 1
print("Instruction Line " + str(i) + ": " + "R[0]->" + str(register[0]) + " " + "R[1]->" + str(register[1]) + " " + "R[2]->" + str(register[2]) + " " + "R[3]->" + str(register[3]) + "\n")
output_fileA.write("Instruction Count: " + str(instruction_Count) + "\n" + "\n")
i = 0
for x in register:
    output_fileA.write("Register " + str(i) + ": " + str(x) + "\n")
    i = i + 1
output_fileA.write("\n")
i = 0
for x in data_Memory:
    output_fileA.write("Address " + str(i) + ": " + str(x) + "\n")
    i = i + 1

input_file1.close()
input_fileA.close()
output_fileA.close()
