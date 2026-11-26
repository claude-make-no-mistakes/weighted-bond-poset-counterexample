# A counterexample to Schur log-concavity of weighted bond posets

The **18-vertex star $K_{1,17}$** refutes González D’León and Wachs’s Conjecture 7.3. If $f_d$ is the degree-$d$ component of $\Psi_{K_{1,m}}$, then

$$
[s_{(15,1)}]\bigl(f_8^2-f_7f_9\bigr)
=509\binom{m}{8}^{2}-637\binom{m}{7}\binom{m}{9}.
$$

At $m=17$ this is $-354{,}585{,}660$. The coefficient is negative for every $m\geq17$. There is also a degree-three counterexample family.

$$
[s_{(3,3)}]\bigl(f_3^2-f_2 f_4\bigr)
=37\binom{m}{3}^{2}-50\binom{m}{2}\binom{m}{4}
=\frac{m^2(m-1)^2(m-2)(77-m)}{72}.
$$

At $m=78$ this coefficient is $-38{,}076{,}038$. It is negative for every integer $m\geq78$. [Original conjecture](https://arxiv.org/html/2608.08692v2#S7)

[Proof note](proof.pdf) · [LaTeX source](proof.tex) · [X draft](POST-DRAFT.md)

## Replay the arithmetic

```sh
python verify.py
```

The verifier uses only the Python standard library. It computes the two-variable Möbius polynomials, checks them independently from two-weight intervals, and reproduces both negative coefficients.
