@256
D=A
@SP
M=D
@return-address0
D=A
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
(Main.fibonacci)
@0
D=A
@Main.fibonacci.COUNTER
M=D
(Main.fibonacci.LOOP)
@Main.fibonacci.COUNTER
D=M
@Main.fibonacci.END
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
@Main.fibonacci.COUNTER
M=M-1
@Main.fibonacci.LOOP
0;JMP
(Main.fibonacci.END)
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
@TRUE0
D;JLT
@FALSE0
0;JMP
(TRUE0)
D=-1
@END0
0;JMP
(FALSE0)
D=0
@END0
0;JMP
(END0)
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
@Main$IF_TRUE
D;JNE
@22222
@Main$IF_FALSE
0;JMP
@22222
(Main$IF_TRUE)
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
@LCL
D=M
@R14
M=D
@5
A=D-A
D=M
@R15
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@R14
A=M-1
D=M
@THAT
M=D
@R14
A=M-1
A=A-1
D=M
@THIS
M=D
@R14
D=M
@3
A=D-A
D=M
@ARG
M=D
@R14
D=M
@4
A=D-A
D=M
@LCL
M=D
@R15
A=M
0;JMP
@22222
(Main$IF_FALSE)
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
@return-address1
D=A
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
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(return-address1)
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
@return-address2
D=A
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
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(return-address2)
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
@LCL
D=M
@R14
M=D
@5
A=D-A
D=M
@R15
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@R14
A=M-1
D=M
@THAT
M=D
@R14
A=M-1
A=A-1
D=M
@THIS
M=D
@R14
D=M
@3
A=D-A
D=M
@ARG
M=D
@R14
D=M
@4
A=D-A
D=M
@LCL
M=D
@R15
A=M
0;JMP
@22222
(Sys.init)
@0
D=A
@Sys.init.COUNTER
M=D
(Sys.init.LOOP)
@Sys.init.COUNTER
D=M
@Sys.init.END
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
@Sys.init.COUNTER
M=M-1
@Sys.init.LOOP
0;JMP
(Sys.init.END)
@22222
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
@22222
@return-address3
D=A
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
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(return-address3)
@22222
(Sys$WHILE)
@22222
@Sys$WHILE
0;JMP
