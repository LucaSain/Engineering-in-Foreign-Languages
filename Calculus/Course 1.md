Calculus is an extension of the Euclidian Geometry
_The area of a rect with the l of a irrational number_
![[Course 1 2024-02-29 08.09.57.excalidraw]]

**Theorem**
$$\displaylines{\displaylines {r_n \epsilon Q \space r_n \rightarrow x \\ \rho_n \epsilon Q \space \rho_n \rightarrow y } \space \space r_n \cdot \rho_n \rightarrow xy  }$$

# The area under the graph of a function
The fundamental theorem of calculus. The theorem of Leibniz-Newton.
![[Course 1 2024-02-29 08.28.42.excalidraw]]
$$A=F(b)-F(a), F'=f$$
$$\int_a^bf(x)dx=A$$

## Proof
![[Course 1 2024-02-29 08.33.38.excalidraw]]
Newton looked at the derivative of the Area of $f(x)$.
The area of the rectangle is: $$\displaylines{(y-x)*m\le A(y) - A(x)\le M(y-x) \\ m \le \frac{A(y) -A(x)}{y-x}\le M \\ \lim_x}$$

## The Riemann integral
$$f:[a,b] \rightarrow R $$
![[Course 1 2024-02-29 09.04.31.excalidraw]]
_Fermat found the formula for the area of $x^\alpha$ but the formula for $x^{-1}$._
A division:$$\Delta = division[a,b] \quad a=x_0\lt x_1 \lt x_2 \lt ... \lt x_n = b  $$
$$\displaylines{||\Delta|| = \max_{i=1,n}(x_i-x_{i-1}) \\ \xi_i \epsilon [x_{i-1},x_i] \quad intermediary \space point  \\ \sum_{i=0}^n{f(\xi_i)(x_i-x_{i-1})}=S(f,\Delta,\xi_i)}$$

**Definition**
$f$ is Riemann integrable on the interval $[a,b]$ if $\exists I \epsilon R$ with $\forall \xi \gt 0, \exists \delta_\xi \space such \space that \space \forall \Delta \space with ||\Delta|| \lt \delta_{\xi_i} \space and  \space \forall(\xi_i)$  

### The fundamental theorem of calculus
$$f:[a,b] \rightarrow R \quad \int_a^bf(x)dx = F(b)-F(a), F'=f$$
The set of all primitives of function f is:
$$\int f(x)dx = \set{F| F'=f}$$
_We must know the ta_