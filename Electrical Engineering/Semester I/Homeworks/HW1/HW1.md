
### Initial Graph + Systems of independent loops and cut-sets
In this example we have 7 nodes and 12 edges.

Thus our **tree** will have N-1 = 6 **twigs**. There will also be B-N+1 = 6 **chords**.
Further, the number of **independent loops and sections** will be both equal to 6.

![[HW1.excalidraw]]
### Let's assign values to the chords

|  Chord 	| Value   	|
|---	|---	|
|   7	|   3	|
|   8	|   4	|
|   9	|   5	|
|   10	|   3	|
|   11	|   4	|
|   12	|   2	|

Now we can generate the graph of currents and voltages using Khirkhoff's laws
### Applying TKI
![[HW1 2023-10-21 16.27.19.excalidraw]]

Now that we have computed all the currents using *TKI for sections* we can draw the graph of currents and verify using TKI for each node of the graph.

![[HW1 2023-10-21 16.54.02.excalidraw]]
We have to apply TK1 only for the node (n)=1 since our cut-sets match the other nodes.
	Node 1: 1+1 -1 -2 +1



