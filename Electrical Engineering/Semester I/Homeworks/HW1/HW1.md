caby Sainenco Luchian, 1112EC IoT sgr2
### Initial Graph + Systems of independent loops and cut-sets

In this example we have 7 nodes and 12 edges.
Thus,our **tree** will have N-1 = 6 **twigs**. There will also be B-N+1 = 6 **chords**.
Further, the number of **independent loops and sections** will be both equal to 6.

![[HW1.excalidraw]]
### Let's assign values to the chords and twigs

|  Chord 	| Current   |
|---	|---	|
|   7	|   3	|
|   8	|   4	|
|   9	|   5	|
|   10	|   3	|
|   11	|   4	|
|   12	|   2	|

|  Twigs | Voltage   |
|---	|---	|
|   1	|   1	|
|   2	|   1	|
|   3	|   2	|
|   4	|   2	|
|   5	|   -1	|
|   6	|   -2	|


Now we can generate the graph of currents and voltages using Khirkhoff's laws
### Applying TKI
![[HW1 2023-10-21 16.27.19.excalidraw]]

Now that we have computed all the currents using *TKI for sections* we can draw the graph of currents and verify using TKI for each node of the graph.

![[HW1 2023-10-21 16.54.02.excalidraw]]
We have to apply TK1 only for the node (n)=1 since our cut-sets match the other nodes.
	Node 1: -1-1-1+2-1+2=0 true
So the graph of currents complies with TK1 👍👍👍

### Applying TKII

![[HW1 2023-10-21 17.20.17.excalidraw]]
Now we have the values for the voltage on the chords.
Let's draw the graph of voltages
![[HW1 2023-10-21 20.41.38.excalidraw]]
Our values also verifies TKII applied on the outer, bigger loop along with any other loops from the graph.👍👍👍
	3+0-3+4-3-1=0 true

### Tellgen's theorem
Finally we should draw the receiver/generator convention graph and check the Tellgen's Theorem for it.

Let's map the edges of the graph on the receiver/generator convention.
![[HW1 2023-10-22 15.04.09.excalidraw]]
And applying the Tellgen's theorem for the whole graph:
	0-12+20-9-4+6+1+1-2-4-1+4=8-13+8-7+4=16+4-20=0 **true**
So the graph checks the Tellgen's theorem🥳.