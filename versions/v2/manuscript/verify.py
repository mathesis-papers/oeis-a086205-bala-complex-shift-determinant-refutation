from fractions import Fraction
from functools import cache
from itertools import permutations
from math import factorial, prod
import json


def trim(polynomial):
    while len(polynomial) > 1 and not polynomial[-1]:
        polynomial.pop()
    return polynomial


def add(first, second):
    result = [Fraction(0)] * max(len(first), len(second))
    for index, coefficient in enumerate(first):
        result[index] += coefficient
    for index, coefficient in enumerate(second):
        result[index] += coefficient
    return trim(result)


def multiply(first, second):
    result = [Fraction(0)] * (len(first) + len(second) - 1)
    for first_degree, first_coefficient in enumerate(first):
        for second_degree, second_coefficient in enumerate(second):
            result[first_degree + second_degree] += first_coefficient * second_coefficient
    return trim(result)


def binomial_polynomial(square, degree):
    result = [Fraction(1, factorial(degree))]
    for offset in range(degree):
        result = multiply(result, [Fraction(square - offset), Fraction(1)])
    return result


def determinant(matrix):
    size = len(matrix)
    result = [Fraction(0)]
    for permutation in permutations(range(size)):
        inversions = sum(permutation[first] > permutation[second]
                         for first in range(size) for second in range(first + 1, size))
        term = [Fraction((-1) ** inversions)]
        for row, column in enumerate(permutation):
            term = multiply(term, matrix[row][column])
        result = add(result, term)
    return result


def sequence(size):
    return prod(factorial(2 * index - 1) // factorial(index - 1)
                for index in range(1, size + 1))


def odd_sequence(size):
    return prod(prod(range(1, 2 * index, 2)) for index in range(1, size + 1))


def signed_odd_sequence(index):
    if index >= 0:
        return odd_sequence(index)
    reflected = -index - 1
    return (-1) ** ((reflected + 1) // 2) * odd_sequence(reflected)


def barnes_integer(argument):
    return prod(factorial(index) for index in range(argument - 1))


@cache
def standard_tableau_count(shape):
    if not shape:
        return 1
    total = 0
    for row, length in enumerate(shape):
        if row + 1 < len(shape) and length == shape[row + 1]:
            continue
        smaller = list(shape)
        smaller[row] -= 1
        total += standard_tableau_count(tuple(value for value in smaller if value))
    return total


def derivative(polynomial):
    return [Fraction(0)] if len(polynomial) == 1 else [
        degree * coefficient for degree, coefficient in enumerate(polynomial[1:], 1)]


def negate(polynomial):
    return [-coefficient for coefficient in polynomial]


def monomial(degree, coefficient):
    return [Fraction(0)] * degree + [Fraction(coefficient)]


def tableau_count(size):
    cells = [(row, column) for row in range(size) for column in range(size - row)]
    entries = {}

    def count(position):
        if position == len(cells):
            return 1
        row, column = cells[position]
        minimum = max(entries.get((row, column - 1), 1),
                      entries.get((row - 1, column), 0) + 1)
        total = 0
        for value in range(minimum, size + 1):
            entries[(row, column)] = value
            total += count(position + 1)
        entries.pop((row, column), None)
        return total

    return count(0)


def check(condition, label):
    if not condition:
        raise AssertionError(label)


def main():
    polynomial_rows = []
    for size in range(7):
        matrix = [[binomial_polynomial(row * row, column)
                   for column in range(1, size + 1)] for row in range(1, size + 1)]
        actual = determinant(matrix)
        expected = [Fraction(sequence(size))]
        for index in range(1, size + 1):
            expected = multiply(expected, [Fraction(1), Fraction(1, index * index)])
        check(actual == expected, ('shifted polynomial', size))
        invariant = [[binomial_polynomial(row * row, column)
                      for column in range(size)] for row in range(1, size + 1)]
        check(determinant(invariant) == [Fraction(sequence(size), factorial(size))],
              ('invariant polynomial', size))
        polynomial_rows.append({'n': size, 'D_n_coefficients': [str(value) for value in actual]})
    check(polynomial_rows[1]['D_n_coefficients'] == ['1', '1'], 'size-one witness')
    initial_terms = [1, 1, 6, 360, 302400, 4572288000, 1520925880320000,
                     13153940405570764800000, 3412910854477066178396160000000,
                     30107378079113824305786648526848000000000]
    check([sequence(size) for size in range(10)] == initial_terms, 'A086205 terms 0..9')
    for size in range(13):
        actual = sequence(size)
        alternative = prod(Fraction(factorial(size + index), factorial(2 * index))
                           for index in range(size + 1))
        odd_product = odd_sequence(size)
        schur_product = factorial(size) * prod(first + second for first in range(1, size + 1)
                                             for second in range(first + 1, size + 1))
        check(actual == alternative == 2 ** (size * (size - 1) // 2) * odd_product
              == schur_product, ('sequence products', size))
        check(odd_product == prod((2 * index + 1) ** (size - index)
                                  for index in range(size + 1)), ('odd power product', size))
        odd_next, odd_after, odd_last = (odd_sequence(size + offset) for offset in range(1, 4))
        check(odd_product * odd_after ** 3 + odd_next ** 3 * odd_last
              == (4 * size + 8) * odd_next ** 2 * odd_after ** 2,
              ('odd quartic recurrence', size))
        telescope = prod(Fraction(first + second, first + second - 1)
                         for second in range(1, size + 1) for first in range(1, second + 1))
        check(telescope == 2 ** size, ('A266091 auxiliary product', size))
        triangular_product = prod(Fraction(first + 2 * second, first + second - 1)
                                  for second in range(1, size + 1)
                                  for first in range(1, second + 1))
        factorial_product = prod(Fraction(factorial(3 * index), factorial(size + index))
                                 for index in range(size + 1))
        check(triangular_product == factorial_product, ('A266091 defining product', size))
        if size >= 1:
            check(odd_next * odd_sequence(size - 1) == (2 * size + 1) * odd_product ** 2,
                  ('odd quadratic recurrence', size))
            previous, following, next_term = sequence(size - 1), sequence(size + 1), sequence(size + 2)
            check(following * previous == (4 * size + 2) * actual ** 2,
                  ('quadratic recurrence', size))
            check(actual ** 3 * next_term + previous * following ** 3
                  == (8 * size + 8) * (actual * following) ** 2,
                  ('quartic recurrence', size))
    tableau_rows = []
    for size in range(6):
        count = tableau_count(size)
        check(count == 2 ** (size * (size - 1) // 2), ('tableau count', size))
        tableau_rows.append({'n': size, 'count': count})
    standard_rows = []
    for size in range(13):
        hooks = prod(2 * (size - row - column + 1) + 1
                     for row in range(1, size + 1)
                     for column in range(1, size - row + 2))
        check(hooks == odd_sequence(size), ('staircase hooks', size))
        barnes_square = Fraction(barnes_integer(2 * size + 2),
                                2 ** (size * size) * barnes_integer(size + 1) ** 2
                                * factorial(size))
        check(barnes_square == odd_sequence(size) ** 2, ('Barnes square formula', size))
        if size <= 5:
            count = standard_tableau_count(tuple(range(size, 0, -1)))
            check(count * hooks == factorial(size * (size + 1) // 2),
                  ('standard tableau enumeration', size))
            standard_rows.append({'n': size, 'count': count})
    for index in range(-12, 13):
        current = signed_odd_sequence(index)
        sign = -1 if ((index + 1) // 2) % 2 else 1
        check(current == sign * signed_odd_sequence(-index - 1),
              ('signed reflection', index))
        before, after, second, third = (
            signed_odd_sequence(index + offset) for offset in [-1, 1, 2, 3])
        check(before * after == (2 * index + 1) * current ** 2,
              ('signed quadratic recurrence', index))
        check(current * second ** 3 + after ** 3 * third
              == (4 * index + 8) * after ** 2 * second ** 2,
              ('signed quartic recurrence', index))
    for index in range(13):
        current = monomial(index * (index + 1) // 2, Fraction(1, odd_sequence(index)))
        before = [Fraction(1)] if index == 0 else monomial(
            index * (index - 1) // 2, Fraction(1, odd_sequence(index - 1)))
        after = monomial((index + 1) * (index + 2) // 2,
                         Fraction(1, odd_sequence(index + 1)))
        actual = add(multiply(derivative(after), before),
                     negate(multiply(after, derivative(before))))
        check(actual == multiply(current, current), ('Burchnall-Chaundy monomial', index))
    for second_parameter in [-3, 0, 2]:
        for third_parameter in [-5, 0, 7]:
            cubic = [Fraction(second_parameter, 3), Fraction(0), Fraction(0), Fraction(1, 3)]
            sextic = [Fraction(-5 * second_parameter ** 2, 45),
                      Fraction(third_parameter, 45), Fraction(0),
                      Fraction(5 * second_parameter, 45), Fraction(0), Fraction(0),
                      Fraction(1, 45)]
            actual = add(multiply(derivative(sextic), [Fraction(0), Fraction(1)]),
                         negate(sextic))
            check(actual == multiply(cubic, cubic),
                  ('Burchnall-Chaundy cubic and sextic', second_parameter, third_parameter))
    print(json.dumps({'status': 'pass', 'arithmetic': 'exact rational polynomial coefficients and integers',
                      'determinant_polynomial_range': [0, 6], 'product_range': [0, 12],
                      'recurrence_range': [1, 12], 'tableau_enumeration': tableau_rows,
                      'signed_recurrence_range': [-12, 12], 'hook_product_range': [0, 12],
                      'Barnes_square_formula_range': [0, 12],
                      'standard_tableau_enumeration': standard_rows,
                      'Burchnall_Chaundy_monomial_range': [0, 12],
                      'Burchnall_Chaundy_parameter_cases': 9,
                      'polynomials': polynomial_rows}, indent=2))


if __name__ == '__main__':
    main()
