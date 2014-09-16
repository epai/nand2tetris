// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[3], respectively.)

// Put your code here.
	@i
	M=1
	@sum
	M=0
(LOOP)
	@i
	D=M // D=i
	@R1
	D=D-M
	@REST
	D;JGT // if (i-R1)>0 goto REST
	@R0
	D=M // D=M[R0]
	@sum
	M=D+M // sum=sum+M[R0]
	@i
	M=M+1 // i=i+1
	@LOOP
	0;JMP // goto LOOP
(REST)	
	@sum
	D=M
	@R2
	M=D
	@END
	0;JMP // goto END
(END)
	@END
	0;JMP // Terminate