// push constant 0    

@0
D=A

@SP
A=M
M=D

@SP
M=M+1

// pop local 0         // initializes sum = 0

@0
D=A

@LCL
A=M+D
D=A

@R13
M=D

@SP
AM=M-1
D=M

@R13
A=M
M=D

// label LOOP_START
(LOOP_START)
// push argument 0    

@0
D=A

@ARG
A=M+D
D=A

@R13
M=D

@R13
A=M
D=M

@SP
M=M+1
A=M-1
M=D

// push local 0

@0
D=A

@LCL
A=M+D
D=A

@R13
M=D

@R13
A=M
D=M

@SP
M=M+1
A=M-1
M=D

// add

@SP
AM=M-1
D=M

@SP
A=M-1
M=M+D

// pop local 0	        // sum = sum + counter

@0
D=A

@LCL
A=M+D
D=A

@R13
M=D

@SP
AM=M-1
D=M

@R13
A=M
M=D

// push argument 0

@0
D=A

@ARG
A=M+D
D=A

@R13
M=D

@R13
A=M
D=M

@SP
M=M+1
A=M-1
M=D

// push constant 1

@1
D=A

@SP
A=M
M=D

@SP
M=M+1

// sub

@SP
AM=M-1
D=M

@SP
A=M-1
M=M-D

// pop argument 0      // counter--

@0
D=A

@ARG
A=M+D
D=A

@R13
M=D

@SP
AM=M-1
D=M

@R13
A=M
M=D

// push argument 0

@0
D=A

@ARG
A=M+D
D=A

@R13
M=D

@R13
A=M
D=M

@SP
M=M+1
A=M-1
M=D

// if-goto LOOP_START  // If counter > 0, goto LOOP_START

@SP
AM=M-1
D=M

@LOOP_START
D;JGT

// push local 0

@0
D=A

@LCL
A=M+D
D=A

@R13
M=D

@R13
A=M
D=M

@SP
M=M+1
A=M-1
M=D

