
// for i; i< n, i++ {
// 	arr[i] = -1
// }

// arr = 100, n = 10

@100
D=M
@arr
M=D

@10
D=M
@n
M=D

@i
M=0

(LOOP)
@i
D=M
@n
D=D-M

@END
D; JEQ

@arr
D=M
@i
A=D+M
M=-1


// i++
@i
M=M+1

@LOOP
0;JMP

(END)
@END
0; JMP