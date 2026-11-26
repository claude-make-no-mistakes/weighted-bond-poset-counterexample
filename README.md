# A Counterexample to Schur Log-Concavity of Weighted Bond Posets

The **18-vertex star $K_{1,17}$** refutes Conjecture 7.3 of González D'León and Wachs ([arXiv:2608.08692v2](https://arxiv.org/abs/2608.08692v2)), which conjectured that the weighted bond-poset symmetric function $\Psi_G$ is Schur-log-concave for every finite simple graph $G$.

Let $f_d$ denote the degree-$d$ homogeneous component of $\Psi_{K_{1,m}}$. Then:

$$
[s_{(15,1)}]\bigl(f_8^2 - f_7 f_9\bigr)
= 509\binom{m}{8}^{2} - 637\binom{m}{7}\binom{m}{9}.
$$

At $m = 17$ this equals $-354{,}585{,}660$, and it remains strictly negative for every integer $m \geq 17$.

A degree-three failure also occurs for larger stars:

$$
[s_{(3,3)}]\bigl(f_3^2 - f_2 f_4\bigr)
= 37\binom{m}{3}^{2} - 50\binom{m}{2}\binom{m}{4}
= \frac{m^2(m-1)^2(m-2)(77-m)}{72}.
$$

At $m = 78$ this equals $-38{,}076{,}038$, and it remains strictly negative for every integer $m \geq 78$.

## Documents

- [Proof note (PDF)](proof.pdf)
- [LaTeX source](proof.tex)

## Verification

Run the exact integer verification script (Python 3 standard library only):

```sh
python3 verify.py
```

The script computes the two-variable Möbius polynomials of $K_{1,j}$ ($0 \leq j \leq 9$) via the Möbius recurrence, cross-checks them independently by direct interval summation over the two-weighted bond poset, and verifies all closed-form identities and negative Schur coefficients.
