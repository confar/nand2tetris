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

@JumpHere1
D;JEQ

@SP
A=M
M=0

(JumpHere1)
@SP
A=M
M=-1

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

@JumpHere1
D;JEQ

@SP
A=M
M=0

(JumpHere1)
@SP
A=M
M=-1

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

@JumpHere1
D;JEQ

@SP
A=M
M=0

(JumpHere1)
@SP
A=M
M=-1

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

@JumpHere3
A=M
D;JGT

@SP
A=M
M=0

(JumpHere3)
@SP
A=M
M=-1

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

@JumpHere3
A=M
D;JGT

@SP
A=M
M=0

(JumpHere3)
@SP
A=M
M=-1

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

@JumpHere3
A=M
D;JGT

@SP
A=M
M=0

(JumpHere3)
@SP
A=M
M=-1

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

@JumpHere2
D;JLT

@SP
A=M
M=0

(JumpHere2)
@SP
A=M
M=-1

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

@JumpHere2
D;JLT

@SP
A=M
M=0

(JumpHere2)
@SP
A=M
M=-1

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

@JumpHere2
D;JLT

@SP
A=M
M=0

(JumpHere2)
@SP
A=M
M=-1

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
M=!M

