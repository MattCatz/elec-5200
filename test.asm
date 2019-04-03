        ADDI r6, 	r6,100
        ADD r5, 	r5, r6
start:	LOAD r4, r4, 50
		STOR  r3, r3, 0
		ADDI zero, 	zero, 5
		LUI r2 , r2, 100
Misslw: ADD r1,r1, r1
		SUB r0, r0, r0
		AND r5, r5 , r5
		OR r6, r6, r6
		SLT r4, r4, r4
		JAL r3, r3, 	666666
		BEQ	 r2, r2, END
END:	BEQ	 r1, r1, 10
		SLT r0, r0, r0