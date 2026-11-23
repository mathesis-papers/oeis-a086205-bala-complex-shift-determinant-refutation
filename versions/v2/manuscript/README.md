# A086205, Bala's 19 February 2023 formula block

The note corrects the complex-shift conjecture in Peter Bala's formula block
of 19 February 2023 in OEIS A086205 (revision 35). For one-based row and column
indices,

`D_n(z) = a(n) * product_{i=1..n}(1 + z/i^2)`.

The argument extends Krattenthaler's (1999) polynomial Vandermonde evaluation.
The normalized determinants converge locally uniformly to the entire function
`sum_{r>=0} pi^(2r) z^r/(2r+1)!`, equivalently
`sinh(pi sqrt(z))/(pi sqrt(z))`, with value 1 at zero.
The companion results include Somos's signed integer-index recurrences,
Deutsch's staircase hook product, and alternative proofs of the earlier
staircase Schur and tableau formulas (Yutcis 1980; Stanley 1999; Striker 2009).
For the Burchnall-Chaundy polynomials in the linked Veselov-Willox (2014)
normalization, the leading term is `z^(n(n+1)/2)/b(n)`, where `b(n)=A057863(n)`.
The A266091 finite products are proved; its matrix enumeration is credited to
Behrend, Fischer and Konvalinka (2015/2017).
Both Barnes formulas and the recorded A057863/A086205 asymptotics follow
from factorial ratios, Gamma duplication and the classical Barnes expansion.

## Build

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, use a standard LaTeX distribution with the packages named in
`note.tex` and run `pdflatex note.tex` twice. The bibliography is included in
the TeX source; there are no external bibliography or figure dependencies.

## Exact finite checks

Python 3.10 or later, standard library only:

```sh
python3 verify.py > verification.json
```

The expected output has `status: pass`. The determinant is expanded by
permutations over rational-coefficient polynomials, independently of the
closed-product implementation. Full polynomial identities are compared for
sizes 0 through 6, including the shift-invariant zero-based-column variant.
The listed products and recurrences are checked through index 12, and
staircase tableaux are enumerated through size 5.
The standard staircase-tableau counts are independently enumerated through
size 5, hook products are checked through size 12, and the reflection and
signed recurrences are checked for indices -12 through 12. The differential
recurrence is checked for the Burchnall-Chaundy monomial solutions through
index 12 and for nine parameter choices in the cubic and sextic formulas.
The squared integer-argument Barnes formula is checked through size 12.

## Coverage

The pinned file
<https://github.com/the-omega-institute/trureturing/blob/d73267bacb7cde6604fdaee3818fa517d9ced843/D5/S0/Certificates/BalaComplexShiftDeterminantRefutation.lean>
contains `D5.S0.Certificates.BalaComplexShiftDeterminantRefutation.result`,
which proves the negation of universal shift independence using size one
and shift one. The general determinant evaluation and the accompanying
identities are written proofs in the note. Finite checks have the ranges
specified above.

## Authors And License

Haobo Ma — ChronoAI Pte Ltd, Singapore.

Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore.

CC BY 4.0 (Creative Commons Attribution 4.0 International).
<https://creativecommons.org/licenses/by/4.0/>.
