"""Reproduce the Schur coefficient for the star counterexample over the integers."""

from math import comb


def multiply(left, right):
    """Homogeneous binary forms stored by increasing y-degree."""
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def star_polynomials(max_degree):
    result = [[1]]
    for degree in range(1, max_degree + 1):
        row = [0] * (degree + 1)
        for chosen in range(degree):
            complete_homogeneous = [1] * (degree - chosen + 1)
            product = multiply(complete_homogeneous, result[chosen])
            row = [a - comb(degree, chosen) * b for a, b in zip(row, product, strict=True)]
        result.append(row)
    return result


def two_weight_intervals(max_degree):
    """Direct interval sum over center blocks with two nonnegative weights."""
    mu = {(0, 0): 1}
    for leaves in range(1, max_degree + 1):
        for red in range(leaves + 1):
            blue = leaves - red
            mu[leaves, red] = -sum(
                comb(leaves, small) * mu[small, lower_red]
                for small in range(leaves)
                for lower_red in range(max(0, small - blue), min(red, small) + 1)
            )
    return [[mu[n, red] for red in range(n + 1)] for n in range(max_degree + 1)]


def main():
    polys = star_polynomials(9)
    assert polys == two_weight_intervals(9)
    assert polys[2:5] == [[1, 3, 1], [-1, -7, -7, -1], [1, 15, 33, 15, 1]]
    for j, p in enumerate(polys[1:], 1):
        assert p[:2] == [(-1)**j, (-1)**j * (2**j - 1)]

    hook_square = multiply(polys[8], polys[8])
    hook_cross = multiply(polys[7], polys[9])
    alpha = hook_square[1] - hook_square[0]
    beta = hook_cross[1] - hook_cross[0]
    assert (alpha, beta) == (509, 637)
    for leaves in (16, 17, 18, 78):
        coefficient = alpha * comb(leaves, 8)**2 - beta * comb(leaves, 7) * comb(leaves, 9)
        assert 9 * (leaves - 7) * coefficient == comb(leaves, 8)**2 * (8701 - 515 * leaves)
        if leaves == 17:
            assert coefficient == -354585660
        print(f"K_{{1,{leaves}}}, degree 8, s_(15,1): {coefficient:,}")

    square = multiply(polys[3], polys[3])
    cross = multiply(polys[2], polys[4])
    assert (square[3], square[2], cross[3], cross[2]) == (100, 63, 129, 79)
    alpha = square[3] - square[2]
    beta = cross[3] - cross[2]
    for leaves, expected in [(76, 33392500), (77, 0), (78, -38076038), (100, -3068257500)]:
        coefficient = alpha * comb(leaves, 3)**2 - beta * comb(leaves, 2) * comb(leaves, 4)
        assert coefficient == expected
        assert 72 * coefficient == leaves**2 * (leaves - 1)**2 * (leaves - 2) * (77 - leaves)
        print(f"K_{{1,{leaves}}}, degree 3, s_(3,3): {coefficient:,}")


if __name__ == "__main__":
    main()
