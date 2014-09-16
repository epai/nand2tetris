// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.
// SCREEN:  RAM[16386], 256 rows, 32 words each (16bit)
// KEYBOARD:  RAM[24576]
@i
M=1
@SCREEN
D=A
@currPos
M=D
(LOOP)
	@KBD
	D=M
	@ELSE
	D;JNE
	@currKey
	M=0
	@LOOP1
	0;JMP
	(ELSE)
	@currKey
	M=-1
	@LOOP1
	0;JMP
	(LOOP1)
		@i
		D=M
		@8192
		D=D-A
		@BREAK1
		D;JGT
		@currKey
		D=M
		@currPos
		A=M
		M=D
		@i
		M=M+1
		@currPos
		M=M+1
		@LOOP1
		0;JMP
	(BREAK1)
	@i
	M=1
	@SCREEN
	D=A
	@currPos
	M=D
	@LOOP
	0;JMP
		


