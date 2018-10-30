.data
	T: .word -5
	best_matching_score: .word -1     # best score = ? within [0, 32]
	best_matching_count: .word -1     # how many patterns achieve the best score?
	Pattern_Array: .word  1, -2, 3, -4, 5,  -6, 7,   -8, 9, -10, -5, 5, -5, 5, -5, 1, -2, 3, -4, 5  
	

.text
	lw $t0, T
	addi $t9, $0, 20
loop2:
	addi $t5, $0, 0x00000001
	lw $t1, 0x200C($t2)
	add $t2, $t2, 4
	addi $t8, $0, 32
loop:
	and $t3, $t0, $t5
	and $t4, $t1, $t5
	bne $t3, $t4, else
	addi $t7, $t7, 1
else:
	addi $t6, $0, 2
loop3:
	addu $s3, $s3, $t5
	subi $t6, $t6, 1
	beq $t6, $0, done3
	j loop3
done3:
	add $t5, $0, $s3
	add $s3, $0, $0
	subi $t8, $t8, 1
	beq $t8, $0, done
	j loop
done:
	beq $t7, $s0, else2
	slt $s1, $t7, $s0
	bne $s1, $0, else3
	add $s0, $0, $t7
	add $s4, $0, 1
	j else3
	
else2:
	addi $s4, $s4, 1
else3:	
	add $t7, $0, $0
	subi $t9, $t9, 1
	beq $t9, $0, done2 
	j loop2
done2:
	sw $s0, best_matching_score
	sw $s4, best_matching_count
	syscall
