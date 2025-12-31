


def reverseBits(n: int) -> int:
    """
    Reverse the bits of a 32-bit unsigned integer.

    Args:
        n: A 32-bit unsigned integer

    Returns:
        The integer with bits reversed
    """
    result = 0
    for i in range(32):
        # Extract the i-th bit from n
        bit = (n >> i) & 1
        # Place it at position (31 - i) in result
        result |= (bit << (31 - i))
    return result

def foo_b(s:str) :
    return s in (s+s)[1:len(s)*2-1]
