bn 327

## Equivalence of real current sources connected in series
![[Week 5 2023-10-31 10.12.06.excalidraw]]
**Particular cases**
* Jk=0, k=1,n => R=sum(Rk)
* R1=∞ : R=∞ 
	then J=J1
An ideal current source connected in series with something compatible will enforce the ideal current source.
*Remember* an ideal voltage source connected in parallel with something compatible enforces the ideal voltage source
* if(J1,J2 ideal) J1!=J2
	I=J1
	I=J2
	=> contradiction
	if(J1,J2 ideal) J1=J2
	We cannot compute the voltages, we do not have enough ecuations, WRONG case.
	We cannot connect in series two ideal current sources.

No loops with ideal voltage sources!
No sections with only ideal current sources on its branches!
If we can have a tree with only ideal current sources or ideal voltage source and resistors on the branches the problem is 100% good. 👍 

![[Week 5 2023-10-31 10.33.11.excalidraw]]

# Lecture 5: The star triangle equivalence. Current and voltage dividers. Controlled sources. Khirchhoff's method.

## Equivalence of star triangle connections of passive branches.
Star=🔼
Triangle=⏫️
![[Week 5 2023-10-31 10.49.23.excalidraw]]

⏫️->🔼
	**R1**=R12 R21/(R12+R23+R31)
	**R2**=R12 R23/(R12+R23+R31)
	**R3**=R23 R31/(R12+R23+R31)
🔼->⏫️
	**R12**=(R1 R2 + R2 R3 + R3 R1)/R3
	**R23**=(R1 R2 + R2 R3 + R3 R1)/R1
	**R31**=(R1 R2 + R2 R3 + R3 R1)/R2

## Current Divider Theorem
![[Week 5 2023-10-31 11.29.50.excalidraw]]
U=RI=R1R2/(R1+R2) I 
I1=U/R1 = I R2/(R1+R2)
I2= I R1/(R1+R2)

if(R1=R2 )=>
	I1=I2=I/2

## Voltage divider theorem
![[Week 5 2023-10-31 11.34.53.excalidraw]]
R=R1+R2
U=RI=(R1+R2)I =>
	I=U/R
U1=R1I=UR1/(R1+R2)
U2=R2I=UR2/(R1+R2)

if(R1=R2)=>
	U1=U2=U/2

## Two port circuits elements
![[Week 5 2023-10-31 11.39.08.excalidraw]]
1) Voltage controlled voltage source, current controlled voltage source
2) Voltage controlled current source, current controlled current source

### Voltage controlled voltage source (VCVS)
![[Week 5 2023-10-31 11.45.33.excalidraw]]