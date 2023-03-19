def estimate_carry(a,b):
    """Estimate the number of carries.
    The estimated carry may be less than
    the actual one."""
    carry_count = 0
    while a > 0 and b > 0:
        a,digit_a = divmod(a,10)
        b,digit_b = divmod(b,10)
        if digit_a + digit_b > 9:
            carry_count += 1
    return carry_count
