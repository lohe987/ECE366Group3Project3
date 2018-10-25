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
i = 0
while i < len(instruction_Memory):
   #  instruction_Memory[i] = instruction_Memory[i].replace("\n", "")  # remove 'endline' character
    # if(instruction_Memory[i][0:1] == '0'):
       #  instruction_Memory[i] = instruction_Memory[i].replace("0", "", 1)  # remove parity bit
    # else:
        # instruction_Memory[i] = instruction_Memory[i].replace("1", "", 1)  # remove parity bit
        # instruction_Memory[i] = instruction_Memory[i].replace(" ", "")  # remove spaces anywhere in line

    if (instruction_Memory[i][1:4] == '000'):  # lw
        # instruction_Memory[i] = instruction_Memory[i].replace("000", "lw ", 1)  # remove 000 and use lw
        if(instruction_Memory[i][4:6] == '00'):
            # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0, ', 1)
            Rx = 0
        elif(instruction_Memory[i][4:6] == '01'):
            # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1, ', 1)
            Rx = 1
        elif(instruction_Memory[i][4:6] == '10'):
            # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2, ', 1)
            Rx = 2
        else:
            # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3, ', 1)
            Rx = 3

        if (instruction_Memory[i][6:8] == '00'):
            # instruction_Memory[i] = instruction_Memory[i].replace('00', '($0)', 1)
            Ry = 0
        elif (instruction_Memory[i][6:8] == '01'):
            # instruction_Memory[i] = instruction_Memory[i].replace('01', '($1)', 1)
            Ry = 1
        elif (instruction_Memory[i][6:8] == '10'):
            # instruction_Memory[i] = instruction_Memory[i].replace('10', '($2)', 1)
            Ry = 2
        else:
            # instruction_Memory[i] = instruction_Memory[i].replace('11', '($3)', 1)
            Ry = 3

        register[Rx] = data_Memory[register[Ry]]

    elif (instruction_Memory[i][1:4] == '001'):  # sw
        # instruction_Memory[i] = instruction_Memory[i].replace("001", "sw ", 1)  # remove 000 and use sw
        if(instruction_Memory[i][4:6] == '00'):
            # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0, ', 1)
            Rx = 0
        elif(instruction_Memory[i][4:6] == '01'):
            # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1, ', 1)
            Rx = 1
        elif(instruction_Memory[i][4:6] == '10'):
            # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2, ', 1)
            Rx = 2
        else:
            # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3, ', 1)
            Rx = 3

        if (instruction_Memory[i][6:8] == '00'):
            # instruction_Memory[i] = instruction_Memory[i].replace('00', '($0)', 1)
            Ry = 0
        elif (instruction_Memory[i][6:8] == '01'):
            # instruction_Memory[i] = instruction_Memory[i].replace('01', '($1)', 1)
            Ry = 1
        elif (instruction_Memory[i][6:8] == '10'):
            # instruction_Memory[i] = instruction_Memory[i].replace('10', '($2)', 1)
            Ry = 2
        else:
            # instruction_Memory[i] = instruction_Memory[i].replace('11', '($3)', 1)
            Ry = 3

        data_Memory[register[Ry]] = register[Rx]



    elif (instruction_Memory[i][1:4] == '100'):  # add/addi
        if(instruction_Memory[i][4:5] == '0'):
            # instruction_Memory[i] = instruction_Memory[i].replace('100', 'add ', 1)
            if (instruction_Memory[i][4:6] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0, ', 1)
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1, ', 1)
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2, ', 1)
                Rx = 2
            else:
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3, ', 1)
                Rx = 3

            if (instruction_Memory[i][6:8] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0', 1)
                Ry = 0
            elif (instruction_Memory[i][6:8] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1', 1)
                Ry = 1
            elif (instruction_Memory[i][6:8] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2', 1)
                Ry = 2
            else:
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3', 1)
                Ry = 3
            register[Rx] = register[Rx] + register[Ry]
        else:
            # instruction_Memory[i] = instruction_Memory[i].replace('100', 'addi ', 1)
            if (instruction_Memory[i][4:6] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0, ', 1)
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1, ', 1)
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2, ', 1)
                Rx = 2
            else:
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3, ', 1)
                Rx = 3

            if (instruction_Memory[i][6:8] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '0')
                im = 0
            elif (instruction_Memory[i][6:8] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '1')
                im = 1
            elif (instruction_Memory[i][6:8] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '2')
                im = 2
            elif (instruction_Memory[i][6:8] == '11'):
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '3')
                im = 3

            register[Rx] = register[Rx] + im


    elif (instruction_Memory[i][1:4] == '010'):  # sub/subi
        if(instruction_Memory[i][4:5] == '0'):
            # instruction_Memory[i] = instruction_Memory[i].replace('010', 'sub ', 1)
            if (instruction_Memory[i][4:6] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0, ', 1)
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1, ', 1)
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2, ', 1)
                Rx = 2
            else:
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3, ', 1)
                Rx = 3

            if (instruction_Memory[i][6:8] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0', 1)
                Ry = 0
            elif (instruction_Memory[i][6:8] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1', 1)
                Ry = 1
            elif (instruction_Memory[i][6:8] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2', 1)
                Ry = 2
            else:
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3', 1)
                Ry = 3
            register[Rx] = register[Rx] - register[Ry]
        else:
            # instruction_Memory[i] = instruction_Memory[i].replace('010', 'subi ', 1)
            if (instruction_Memory[i][4:6] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0, ', 1)
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1, ', 1)
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2, ', 1)
                Rx = 2
            else:
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3, ', 1)
                Rx = 3

            if (instruction_Memory[i][6:8] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '0')
                im = 0
            elif (instruction_Memory[i][6:8] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '1')
                im = 1
            elif (instruction_Memory[i][6:8] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '2')
                im = 2
            elif (instruction_Memory[i][6:8] == '11'):
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '3')
                im = 3
            register[Rx] = register[Rx] - im

    elif (instruction_Memory[i][1:4] == '011'):  # sltR0/seqR0
        if(instruction_Memory[i][4:5] == '0'):
            # instruction_Memory[i] = instruction_Memory[i].replace('011', 'sltR0 ', 1)
            if (instruction_Memory[i][4:6] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0, ', 1)
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1, ', 1)
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2, ', 1)
                Rx = 2
            else:
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3, ', 1)
                Rx = 3

            if (instruction_Memory[i][6:8] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0', 1)
                Ry = 0
            elif (instruction_Memory[i][6:8] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1', 1)
                Ry = 1
            elif (instruction_Memory[i][6:8] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2', 1)
                Ry = 2
            else:
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3', 1)
                Ry = 3
            if (register[Rx] < register[Ry]):
                register[0] = 1
            else:
                register[0] = 0
        else:
            # instruction_Memory[i] = instruction_Memory[i].replace('011', 'seqR0 ', 1)
            if (instruction_Memory[i][4:6] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0, ', 1)
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1, ', 1)
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2, ', 1)
                Rx = 2
            else:
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3, ', 1)
                Rx = 3

            if (instruction_Memory[i][6:8] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0', 1)
                Ry = 0
            elif (instruction_Memory[i][6:8] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1', 1)
                Ry = 1
            elif (instruction_Memory[i][6:8] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2', 1)
                Ry = 2
            else:
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3', 1)
                Ry = 3
            if (register[Rx] == register[Ry]):
                register[0] = 1
            else:
                register[0] = 0

    elif (instruction_Memory[i][1:4] == '110'):  # xor/and
        first = 0
        if (instruction_Memory[i][4:5] == '0'):
            # instruction_Memory[i] = instruction_Memory[i].replace('110', 'xor ', 1)
            first = 0
        else:
            # instruction_Memory[i] = instruction_Memory[i].replace('110', 'and ', 1)
            first = 1

        if (instruction_Memory[i][4:6] == '00'):
            # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0, ', 1)
            Rx = 0
        elif (instruction_Memory[i][4:6] == '01'):
            # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1, ', 1)
            Rx = 1
        elif (instruction_Memory[i][4:6] == '10'):
            # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2, ', 1)
            Rx = 2
        else:
            # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3, ', 1)
            Rx = 3

        if (instruction_Memory[i][6:8] == '00'):
            # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0', 1)
            Ry = 0
        elif (instruction_Memory[i][6:8] == '01'):
            # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1', 1)
            Ry = 1
        elif (instruction_Memory[i][6:8] == '10'):
            # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2', 1)
            Ry = 2
        else:
            # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3', 1)
            Ry = 3
        if (first == 0):
            register[Rx] = register[Rx] ^ register[Ry]  # bitwise xor
        else:
            register[Rx] = register[Rx] & register[Ry]  # bitwise and

    elif (instruction_Memory[i][1:4] == '101'):  # init/sll
        if(instruction_Memory[i][4:5] == '1'):
            # instruction_Memory[i] = instruction_Memory[i].replace('101', 'sll ', 1)
            if (instruction_Memory[i][4:6] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0, ', 1)
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1, ', 1)
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2, ', 1)
                Rx = 2
            else:
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3, ', 1)
                Rx = 3

            if (instruction_Memory[i][6:8] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '0')
                im = 0
            elif (instruction_Memory[i][6:8] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '1')
                im = 1
            elif (instruction_Memory[i][6:8] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '2')
                im = 2
            elif (instruction_Memory[i][6:8] == '11'):
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '3')
                im = 3
            register[Rx] = register[Rx] << im
        else:
            # instruction_Memory[i] = instruction_Memory[i].replace('101', 'init ', 1)
            if (instruction_Memory[i][4:6] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '$0, ', 1)
                Rx = 0
            elif (instruction_Memory[i][4:6] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '$1, ', 1)
                Rx = 1
            elif (instruction_Memory[i][4:6] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '$2, ', 1)
                Rx = 2
            else:
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '$3, ', 1)
                Rx = 3

            if (instruction_Memory[i][6:8] == '00'):
                # instruction_Memory[i] = instruction_Memory[i].replace('00', '0')
                im = 0
            elif (instruction_Memory[i][6:8] == '01'):
                # instruction_Memory[i] = instruction_Memory[i].replace('01', '1')
                im = 1
            elif (instruction_Memory[i][6:8] == '10'):
                # instruction_Memory[i] = instruction_Memory[i].replace('10', '-2')
                im = 2
            elif (instruction_Memory[i][6:8] == '11'):
                # instruction_Memory[i] = instruction_Memory[i].replace('11', '-1')
                im = 3
            register[Rx] = im

    elif (instruction_Memory[i][1:4] == '111'):  # j/beqR0
        if (instruction_Memory[i][4:5] == '0'):
            # instruction_Memory[i] = instruction_Memory[i].replace('1110', 'j ', 1)
            if (instruction_Memory[i][5:8] == '000'):
                # instruction_Memory[i] = instruction_Memory[i].replace('000', '0')
                im = 0
            elif (instruction_Memory[i][5:8] == '001'):
                # instruction_Memory[i] = instruction_Memory[i].replace('001', '1')
                im = 1
            elif (instruction_Memory[i][5:8] == '010'):
                # instruction_Memory[i] = instruction_Memory[i].replace('010', '2')
                im = 2
            elif (instruction_Memory[i][5:8] == '011'):
                # instruction_Memory[i] = instruction_Memory[i].replace('011', '3')
                im = 3
            elif (instruction_Memory[i][5:8] == '100'):
                # instruction_Memory[i] = instruction_Memory[i].replace('100', '4')
                im = 4
            elif (instruction_Memory[i][5:8] == '101'):
                # instruction_Memory[i] = instruction_Memory[i].replace('101', '5')
                im = 5
            elif (instruction_Memory[i][5:8] == '110'):
                # instruction_Memory[i] = instruction_Memory[i].replace('110', '6')
                im = 7
            else:
                # instruction_Memory[i] = instruction_Memory[i].replace('111', '7')
                im = 7
            i = i - 2**im - 1
        else:
            # instruction_Memory[i] = instruction_Memory[i].replace('1111', 'beqR0 ', 1)
            if (instruction_Memory[i][5:8] == '000'):
                # instruction_Memory[i] = instruction_Memory[i].replace('000', '0')
                im = 0
            elif (instruction_Memory[i][5:8] == '001'):
                # instruction_Memory[i] = instruction_Memory[i].replace('001', '1')
                im = 1
            elif (instruction_Memory[i][5:8] == '010'):
                # instruction_Memory[i] = instruction_Memory[i].replace('010', '2')
                im = 2
            elif (instruction_Memory[i][5:8] == '011'):
                # instruction_Memory[i] = instruction_Memory[i].replace('011', '3')
                im = 3
            elif (instruction_Memory[i][5:8] == '100'):
                # instruction_Memory[i] = instruction_Memory[i].replace('100', '4')
                im = 4
            elif (instruction_Memory[i][5:8] == '101'):
                # instruction_Memory[i] = instruction_Memory[i].replace('101', '5')
                im = 5
            elif (instruction_Memory[i][5:8] == '110'):
                # instruction_Memory[i] = instruction_Memory[i].replace('110', '6')
                im = 7
            else:
                 instruction_Memory[i] = instruction_Memory[i].replace('beqR0 111', 'Halt')
            if (register[0] == 0):
                i = i + 1
            else:
                i = i - 2**im -1
    else:
        print("Unknown instruction:" + instruction_Memory[i])
        instruction_Count = instruction_Count - 1
    instruction_Count = instruction_Count + 1
    i = i + 1

    #output_file.write(instruction_Memory[i] + "\n")

debugger_file.write("Instruction Count: " + str(instruction_Count) + "\n")
i = 0
for x in register:
    debugger_file.write("register " + str(i) + ": " + str(x) + "\n")
    i = i + 1

i = 0
for x in data_Memory:
    debugger_file.write(str(i) + ": " + str(x) + "\n")
    i = i + 1

input_file.close()
output_file.close()
debugger_file.close()
