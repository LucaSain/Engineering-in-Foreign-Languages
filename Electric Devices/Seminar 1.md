Seminar 
	solve exercises
	circuit analysis 
		diode circuits
		small single amplifier
		DC-op analisys
		AC analysis
$$A_v=\frac{V_out}{V_in}$$
Laboratory 💿
	HW1 => BONUS (5p)
		On paper calculations
		PSpice sim results
	HW2 => Mandatory (diode circuits)
	HW3 => Basic amplifier stages
	HW4 => Small signal amplifier. SSA
	and so on


# Modeling of an electronic device
1. Device. Symbol and elec. variables definition
![[Seminar 1 2024-02-28 14.45.09.excalidraw]]
2. Device Equation and/\or equivalent circuits
	1. For resistor: $$v=R\times i$$
	2. For diode: $$i_D=I_S[\exp(\frac{gV_d}{nkT})-1]$$
3. Model parameter
	1. For resistor: $R_j$
	2. For diode:
		1. $I_s=I_0$ saturation current
		2. $n$  ideality factor $[1..2]$
		3. $T=300K$
		4. $q=e=1.6\times10^-19C$
		5. $\frac{kT}{q}[V]=0.025V$
		6. Bias Regions $$i_d =
\begin{cases} I_s\times\exp{\frac{gV_0}{nkT}} \\ D_1 \\ - I_s\end{cases}$$

![[Seminar 1 2024-02-28 15.14.48.excalidraw]]