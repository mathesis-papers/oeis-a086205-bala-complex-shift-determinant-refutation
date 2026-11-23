# Complex-shift correction at OEIS A086205 (revision 35), Bala's formula block of 19 February 2023: an extension of Krattenthaler (1999)

**Authors:** Haobo Ma, Wenlin Zhang

At OEIS A086205 (revision 35), Bala's formula block of 19 February 2023, we correct the complex-shift conjecture by extending Krattenthaler's (1999) polynomial Vandermonde evaluation: the determinant changes from 1 to 2 at size one and shift one. The corrected formula is det_{1<=i,j<=n} binomial(i^2+z,j)=a(n) product_{i=1..n}(1+z/i^2) for every complex z. Its normalized limit is an entire hyperbolic-sine product. We give alternative proofs of the companion identities, including the staircase-tableau count treated by Yutcis (1980), and prove Somos's recurrences for all integer indices. In the directly linked A057863, the Burchnall-Chaundy leading exponent is corrected using the normalization of Veselov and Willox (2014).

- PDF: [frozen public file](paper.pdf)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [oeis-a086205-bala-complex-shift-determinant-refutation](https://mathesis-omega-research.apps.chrono-ai.fun/papers/oeis-a086205-bala-complex-shift-determinant-refutation?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Complex-shift correction at OEIS A086205 (revision 35), Bala's formula block of 19 February 2023: an extension of Krattenthaler (1999). Mathesis, version 2. https://mathesis-omega-research.apps.chrono-ai.fun/papers/oeis-a086205-bala-complex-shift-determinant-refutation?version=2

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/d73267bacb7cde6604fdaee3818fa517d9ced843/D5/S0/Certificates/BalaComplexShiftDeterminantRefutation.lean) | No public receipt |
| Corollary (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/d73267bacb7cde6604fdaee3818fa517d9ced843/D5/S0/Certificates/BalaComplexShiftDeterminantRefutation.lean) | No public receipt |
| Corollary (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/d73267bacb7cde6604fdaee3818fa517d9ced843/D5/S0/Certificates/BalaComplexShiftDeterminantRefutation.lean) | No public receipt |
| Corollary (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/d73267bacb7cde6604fdaee3818fa517d9ced843/D5/S0/Certificates/BalaComplexShiftDeterminantRefutation.lean) | No public receipt |
| Corollary (s5) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/d73267bacb7cde6604fdaee3818fa517d9ced843/D5/S0/Certificates/BalaComplexShiftDeterminantRefutation.lean) | No public receipt |
| Corollary (s6) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/d73267bacb7cde6604fdaee3818fa517d9ced843/D5/S0/Certificates/BalaComplexShiftDeterminantRefutation.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).
