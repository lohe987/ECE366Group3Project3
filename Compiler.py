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
input_file = open("MIPS_machine_code", "r")
output_file = open("MIPS_output.txt", "w")
debugger_file = open("debugger.txt", "w")
register = []  # registers

i = 0
while i < 4:
    register.append(0)
    i = i + 1

Rx = 0  # first argument
Ry = 0  # second argument (register)
im = 0  # second argument (immediate)

instruction_Count = 0

instruction_Memory = []  # create instruction memory
data_Memory = []  # create data memory

i = 0;
while i < (2**16 - 1):  # allocate data memory space
    data_Memory.append(0)
    i = i + 1

for line in input_file:  # allocate instruction memory
    instruction_Memory.append(line)

i = 0 #PC
while i < len(instruction_Memory):
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
                register[0] = 1
            else:
                register[0] = 0
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
                register[0] = 1
            else:
                register[0] = 0

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
                im = 7
            else:
                im = 7
            i = i - 2**im - 1
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
                im = 7
            else:
                 instruction_Memory[i] = instruction_Memory[i].replace('beqR0 111', 'Halt')
            if (register[0] == 0):
                i
            else:
                i = i - 2**im -1
    else:
        print("Unknown instruction:" + instruction_Memory[i])
        instruction_Count = instruction_Count - 1
    instruction_Count = instruction_Count + 1
    i = i + 1

debugger_file.write("Instruction Count: " + str(instruction_Count) + "\n" + "\n")
i = 0
for x in register:
    debugger_file.write("Register " + str(i) + ": " + str(x) + "\n")
    i = i + 1
debugger_file.write("\n")
i = 0
for x in data_Memory:
    debugger_file.write("Address " + str(i) + ": " + str(x) + "\n")
    i = i + 1

input_file.close()
output_file.close()
debugger_file.close()
