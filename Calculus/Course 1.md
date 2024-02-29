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
_We must know the table of primitives_

**Integration by parts**
$$\int_a^buv'=uv\rvert_a^b - \int_a^bu'v$$
**Compositie functions**
$$\int_a^bf(\phi(t))\cdot\phi'(x)dx = F(\phi(b))-F(\phi(a))$$

We are going to define the generalisations of this formulas.

### Improper Riemann integrals
![[Course 1 2024-02-29 09.28.29.excalidraw]]

Compute the area $\ln:(0,1] \rightarrow R$ 
$$
A(a)=\int_\epsilon^1|ln(x)|dx = -\int_\epsilon^1\ln(x)dx = -(-\epsilon\ln(\epsilon)-1+\epsilon), \epsilon \to 0 = 1
$$
Compute the area $e^x$. The area is still 1 👌 .
**Definition**
Let $$\displaylines{f \rightarrow R, b \space \epsilon \space R\cup\set{\infty} \\ \int_a^bf(x)dx \quad is \space convergent \space if \\
\lim_{\displaylines{{u \to b} \\ u \lt b}} \int_a^bf(x)dx \space \epsilon \space \Re \\ 
\mathit{if \space yes} \\ 
\int_a^bf(x)dx=\lim_{\displaylines{{u \to b} \\ u<b}}\int_a^uf(x)dx
}$$

The analogy with the theory of series goes **deeper** than just the formulations
For example:
$$\int_a^\infty \frac{1}{x^2} dx \quad (a>0) \space C \Rightarrow \alpha >1$$
$$\int_1^{\infty}\frac{1}{x^2} \mathit{is \space convergent}$$

**Tests of convergence**
let $\int_a^bf(x) \quad f \ge 0  \space(at \space b)_{b \space \epsilon \space \Re} \quad \mathit{if} \space (b-x)^\alpha f(x)\epsilon(0,\infty)$

**Exercise**


