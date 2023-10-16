# Khirkhoff's Theorem, Tellgen's Theorem

**Intensity of electrical current** is caused by moving of electrons thorugh a conductor. 
The **Intenity** is measured in *Amperes*. i(t) = ∂Q/∂t. For DC the notation is I.
``` i(t) -SI> A (Amperes)```

To **measure** the current we use an *Ammeter* which is connected in series.
![[Screenshot 2023-10-10 at 10.22.06.png]] Series: Ammetter with resistor.

**Electrical voltage** is the difference in electric charge (potential) between tho nodes of a circuit.
The **Electric voltage** is measured in *Volts*. u(t) = W/q
```u(t) -SI> V (Volts)```

To **measure the voltage** we use a *Voltmeter* which is connected in parallel.
![[Screenshot 2023-10-10 at 10.27.16.png]] Parralel: Voltmeter with a resistor in parallel.

## The First Khirchoff theorem (TKI)
The algebraic sum of currents through all the branches incident to a node is zero.

![[Screenshot 2023-10-10 at 10.31.14.png]]
### The First Khirchoff theorem for sections
The algebraic sum of currents through all the branches belonging to a section is zero.
![[Screenshot 2023-10-10 at 10.34.59.png]]

## The Second Khirchoff theorem (TKII) - Voltage Khirchoff Law
The algebraic sum of voltages along all the branches belonging to a loop is zero.
![[Screenshot 2023-10-10 at 10.48.21.png]]
![[Screenshot 2023-10-10 at 11.13.30.png]]
Two branches connected in parallel have the same voltage.

**The electrical potential** of a node represents the voltage from the node to a reference node with an imposed potential(equal with zero).
UAB + UB0 - UA0 = 0
UAB = UA0 - UB0 = VA - VB
**Reference node** is a ground node: V0 = 0.
![[Screenshot 2023-10-10 at 11.27.16.png]]

## Electric Power 💪💪🏿
For an one=port elemen, the power is the product of voltage along the element and the current thourhg the element
```text
Power = U * I 
P -SI> Watts [W]
P = dw/dt
W -SI> Joules [J]
```

#### Receivers conventions (R)
The voltage along the element and the current are oriented in *the opposite way*.
```sgn(U*I)=-1```
**Producer convention** P (P<0)
**Consumer convention** C (P>0)

#### Generators conventions (G)
The voltage along the element and the current are oriented in *the same way*.
```sgn(U*I)=1```
**Producer convention** P (P>0)
**Consumer convention** C (P<0)

## Tellegen's theorem
For an electric circuit, the algebraic sum of powers transferred by all branches is zero.
![[Screenshot 2023-10-10 at 11.43.12.png]]

