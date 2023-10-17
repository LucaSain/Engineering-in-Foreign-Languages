dedelaine

## Ideal and real circuit elements. Power Balance.
**Ideal circuit elements** do not exist, but they are useful to analyse (model) the real circuit elements. 
Ideal circuit element has a *relation* between voltage at the terminals and the current through the element.
```u=f(i)```
 ![[Week 3 2023-10-17 10.08.55.excalidraw]]

**An ideal circuit element** is a *resistive* element if the ecuation between voltage and current is algebraic one.
 ```u=f(i)```
**An ideal circuit element** is a *reactive* element if the ecuation between voltage and current is differential one.
```u=df(i)/dt```
It can be also *passive* if it does note generate energy but it consumes power.

## The characteristics of a resistor
**The resistor** is one port element where the voltage and the current have an imposed relation. The voltage depends on the current.

![[Week 3 2023-10-17 10.16.39.excalidraw]]

The parameter of the resistor is the **resistance**. R-SI> Ω
```u=f(i)```
![[Week 3 2023-10-17 10.20.17.excalidraw]]

1. if R=0 (G=∞): U=0, whatever i (shortcircuit = perfect conductor)
2. if R=∞ (G=0): i=0, whatever u (opencircuit = perfect isolator)

#### Energetic characterisation
![[Week 3 2023-10-17 10.27.56.excalidraw]]
1. The resistor is a passive element.
2. It receives current from the circuit. 
3. It does not store energy. 
4. It transforms energy into head using the Joule's effect.


## Ideal Voltage Source (IVS🙏)
**The IVS** is a one port element where the voltage does not depend on the current, so it's an independent voltage source.

![[Week 3 2023-10-17 10.32.57.excalidraw]]
The parameter of the IVS is the electromotive force.
```text
e=e(t)
e(t), when t=const = E
e[V]
```

It's not a symmetric element.
![[Week 3 2023-10-17 10.36.38.excalidraw]]
u=+-e, whatever i
![[Week 3 2023-10-17 10.38.13.excalidraw]]
![[Week 3 2023-10-17 10.41.05.excalidraw]]
The **IVS** is an active element.

1. if e == 0: u=0 whatever i => short circuit === passivation of an *IVS*

## Ideal Current Source (independent source) = ICS
**The ICS** is a current source, where the current does not depend on the voltage.
![[Week 3 2023-10-17 10.47.15.excalidraw]]
![[Week 3 2023-10-17 11.06.34.excalidraw]]

 If j=0; i=0, whatever u => open-circuit => perfect isolator
![[Week 3 2023-10-17 11.09.22.excalidraw]]
![[Week 3 2023-10-17 11.16.34.excalidraw]]

![[Week 3 2023-10-17 11.19.58.excalidraw]]

# Real Elements

## 1. Real Voltage Source (RVS)
Technically a *IVS* connected w/ a Resistor in series.
**IVS**: R=0
**U**=+-Ri+-e
![[Week 3 2023-10-17 11.28.16.excalidraw]]

![[Week 3 2023-10-17 11.32.03.excalidraw]]
![[Week 3 2023-10-17 11.34.53.excalidraw]]
U0 =+-E Open Circuit Voltage (when I=0)
Ish =+-E/R Short Circuit Voltage (when U=0)

## Real Current Source
A real current source is basically an ideal current source connected in parallel w/ an ideal resistor.
![[Week 3 2023-10-17 11.39.55.excalidraw]]
I = I1 + I2 = j + G * U
I = +-j+-G * U

# The fucking theorem of god 🐙
Goodbye and thanks for the fish