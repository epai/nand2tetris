@256
D=A
@SP
M=D
@return-address
D=M
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(return-address0)
@22222
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@22222
@SP
M=M-1
@SP
A=M
D=M
@THAT
M=D
@22222
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@22222
@SP
M=M-1
@THAT
D=M
@0
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
@22222
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@22222
@SP
M=M-1
@THAT
D=M
@1
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
@22222
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@22222
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
@22222
@SP
D=M
@2
A=D-A
D=M
@SP
A=M-1
D=D-M
@R13
M=D
@SP
D=M
@2
D=D-A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
@SP
M=M-1
@22222
@SP
M=M-1
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
@22222
(FibonacciSeries$MAIN_LOOP_START)
@22222
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@22222
@SP
M=M-1
@SP
A=M
D=M
@FibonacciSeries$COMPUTE_ELEMENT
D;JNE
@22222
@FibonacciSeries$END_PROGRAM
0;JMP
@22222
(FibonacciSeries$COMPUTE_ELEMENT)
@22222
@THAT
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@22222
@THAT
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@22222
@SP
D=M
@2
A=D-A
D=M
@SP
A=M-1
D=D+M
@R13
M=D
@SP
D=M
@2
D=D-A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
@SP
M=M-1
@22222
@SP
M=M-1
@THAT
D=M
@2
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
@22222
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@22222
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@22222
@SP
D=M
@2
A=D-A
D=M
@SP
A=M-1
D=D+M
@R13
M=D
@SP
D=M
@2
D=D-A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
@SP
M=M-1
@22222
@SP
M=M-1
@SP
A=M
D=M
@THAT
M=D
@22222
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
@22222
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@22222
@SP
D=M
@2
A=D-A
D=M
@SP
A=M-1
D=D-M
@R13
M=D
@SP
D=M
@2
D=D-A
@R14
M=D
@R13
D=M
@R14
A=M
M=D
@SP
M=M-1
@22222
@SP
M=M-1
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
@22222
@FibonacciSeries$MAIN_LOOP_START
0;JMP
@22222
(FibonacciSeries$END_PROGRAM)
