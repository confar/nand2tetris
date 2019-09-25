// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.


// sum = 0
// let decr = R1
// While decr > 0:
//.     sum += R0
//		decr = decr - 1	
// End
//

@sum
M = 0

@R1
D = M
@num
M = D

(LOOP)
@num
D = M
@STOP
D; JEQ

@num
D = M

@DECREMENT
D; JGT

@INCREMENT
D; JLT

(DECREMENT)
@num
M = D
M = M - 1

@R0
D = M
@sum
M = M + D

@LOOP
0; JMP

(INCREMENT)
@num
M = D
M = M + 1

@R0
D = M
@sum
M = M - D

@LOOP
0; JMP

(STOP)
@sum
D = M
@R2  
M = D // R2 = sum of multiplications

(END)
@END
0; JMP


