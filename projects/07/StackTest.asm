@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
A=D-A
D=M
@SP
A=M-1
D=D-M
@TRUE0
D;JEQ
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
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
A=D-A
D=M
@SP
A=M-1
D=D-M
@TRUE1
D;JEQ
@FALSE1
0;JMP
(TRUE1)
D=-1
@END1
0;JMP
(FALSE1)
D=0
@END1
0;JMP
(END1)
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
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
A=D-A
D=M
@SP
A=M-1
D=D-M
@TRUE2
D;JEQ
@FALSE2
0;JMP
(TRUE2)
D=-1
@END2
0;JMP
(FALSE2)
D=0
@END2
0;JMP
(END2)
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
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
A=D-A
D=M
@SP
A=M-1
D=D-M
@TRUE3
D;JLT
@FALSE3
0;JMP
(TRUE3)
D=-1
@END3
0;JMP
(FALSE3)
D=0
@END3
0;JMP
(END3)
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
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
A=D-A
D=M
@SP
A=M-1
D=D-M
@TRUE4
D;JLT
@FALSE4
0;JMP
(TRUE4)
D=-1
@END4
0;JMP
(FALSE4)
D=0
@END4
0;JMP
(END4)
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
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
A=D-A
D=M
@SP
A=M-1
D=D-M
@TRUE5
D;JLT
@FALSE5
0;JMP
(TRUE5)
D=-1
@END5
0;JMP
(FALSE5)
D=0
@END5
0;JMP
(END5)
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
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
A=D-A
D=M
@SP
A=M-1
D=D-M
@TRUE6
D;JGT
@FALSE6
0;JMP
(TRUE6)
D=-1
@END6
0;JMP
(FALSE6)
D=0
@END6
0;JMP
(END6)
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
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
A=D-A
D=M
@SP
A=M-1
D=D-M
@TRUE7
D;JGT
@FALSE7
0;JMP
(TRUE7)
D=-1
@END7
0;JMP
(FALSE7)
D=0
@END7
0;JMP
(END7)
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
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
A=D-A
D=M
@SP
A=M-1
D=D-M
@TRUE8
D;JGT
@FALSE8
0;JMP
(TRUE8)
D=-1
@END8
0;JMP
(FALSE8)
D=0
@END8
0;JMP
(END8)
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
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
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
D=M@R14
A=M
M=D
@SP
M=M-1
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
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
D=M@R14
A=M
M=D
@SP
M=M-1
@SP
A=M-1
D=M
@SP
A=M-1
M=-D
@SP
D=M
@2
A=D-A
D=M
@SP
A=M-1
D=D&M
@R13
M=D
@SP
D=M
@2
D=D-A
@R14
M=D
@R13
D=M@R14
A=M
M=D
@SP
M=M-1
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@2
A=D-A
D=M
@SP
A=M-1
D=D|M
@R13
M=D
@SP
D=M
@2
D=D-A
@R14
M=D
@R13
D=M@R14
A=M
M=D
@SP
M=M-1
@SP
A=M-1
D=M
@SP
A=M-1
M=!D
