// push constant 17

@17
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 17

@17
D=A

@SP
A=M
M=D

@SP
M=M+1

// eq

@SP
AM=M-1
D=M

@SP
AM=M-1
D=D-M

@JumpHere9
D;JEQ

@SP
A=M
M=0
@JumpOut9
0;JMP 

(JumpHere9)
@SP
A=M
M=-1

(JumpOut9)
@SP
M=M+1

// push constant 17

@17
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 16

@16
D=A

@SP
A=M
M=D

@SP
M=M+1

// eq

@SP
AM=M-1
D=M

@SP
AM=M-1
D=D-M

@JumpHere12
D;JEQ

@SP
A=M
M=0
@JumpOut12
0;JMP 

(JumpHere12)
@SP
A=M
M=-1

(JumpOut12)
@SP
M=M+1

// push constant 16

@16
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 17

@17
D=A

@SP
A=M
M=D

@SP
M=M+1

// eq

@SP
AM=M-1
D=M

@SP
AM=M-1
D=D-M

@JumpHere15
D;JEQ

@SP
A=M
M=0
@JumpOut15
0;JMP 

(JumpHere15)
@SP
A=M
M=-1

(JumpOut15)
@SP
M=M+1

// push constant 892

@892
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 891

@891
D=A

@SP
A=M
M=D

@SP
M=M+1

// lt

@SP
AM=M-1
D=M

@SP
AM=M-1
D=D-M

@JumpHere18
D;JGT

@SP
A=M
M=0
@JumpOut18
0;JMP 

(JumpHere18)
@SP
A=M
M=-1

(JumpOut18)
@SP
M=M+1

// push constant 891

@891
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 892

@892
D=A

@SP
A=M
M=D

@SP
M=M+1

// lt

@SP
AM=M-1
D=M

@SP
AM=M-1
D=D-M

@JumpHere21
D;JGT

@SP
A=M
M=0
@JumpOut21
0;JMP 

(JumpHere21)
@SP
A=M
M=-1

(JumpOut21)
@SP
M=M+1

// push constant 891

@891
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 891

@891
D=A

@SP
A=M
M=D

@SP
M=M+1

// lt

@SP
AM=M-1
D=M

@SP
AM=M-1
D=D-M

@JumpHere24
D;JGT

@SP
A=M
M=0
@JumpOut24
0;JMP 

(JumpHere24)
@SP
A=M
M=-1

(JumpOut24)
@SP
M=M+1

// push constant 32767

@32767
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 32766

@32766
D=A

@SP
A=M
M=D

@SP
M=M+1

// gt

@SP
AM=M-1
D=M

@SP
AM=M-1
D=D-M

@JumpHere27
D;JLT

@SP
A=M
M=0
@JumpOut27
0;JMP 

(JumpHere27)
@SP
A=M
M=-1

(JumpOut27)
@SP
M=M+1

// push constant 32766

@32766
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 32767

@32767
D=A

@SP
A=M
M=D

@SP
M=M+1

// gt

@SP
AM=M-1
D=M

@SP
AM=M-1
D=D-M

@JumpHere30
D;JLT

@SP
A=M
M=0
@JumpOut30
0;JMP 

(JumpHere30)
@SP
A=M
M=-1

(JumpOut30)
@SP
M=M+1

// push constant 32766

@32766
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 32766

@32766
D=A

@SP
A=M
M=D

@SP
M=M+1

// gt

@SP
AM=M-1
D=M

@SP
AM=M-1
D=D-M

@JumpHere33
D;JLT

@SP
A=M
M=0
@JumpOut33
0;JMP 

(JumpHere33)
@SP
A=M
M=-1

(JumpOut33)
@SP
M=M+1

// push constant 57

@57
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 31

@31
D=A

@SP
A=M
M=D

@SP
M=M+1

// push constant 53

@53
D=A

@SP
A=M
M=D

@SP
M=M+1

// add

@SP
AM=M-1
D=M

@SP
A=M-1
M=M+D

// push constant 112

@112
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

// neg

@SP
A=M-1
M=-M

// and

@SP
AM=M-1
D=M

@SP
A=M-1
M=M&D

// push constant 82

@82
D=A

@SP
A=M
M=D

@SP
M=M+1

// or

@SP
AM=M-1
D=M

@SP
A=M-1
M=M|D

// not

@SP
A=M-1
M=!M

