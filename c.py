


def foo_c(n:int) :

    for i in range(1,n+1):
        print('*'*i)


def myPow(x: float, n: int) -> float:
    """
    Implement pow(x, n) which compu   tes x raised to the power n (x^n).

    Args:  
        x: The  base number (float)
        n: The    exponent (32-bit s igned integer)
 
    Returns:
        x raised to the power n
    """
    if n == 0:
        return 1.0

    # Handle negative exponents
    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0
    while n > 0:
        # If n is odd, multiply result by x
        if n % 2 == 1:
            result *= x
        # Square x and divide n by 2
        x *= x
        n //= 2

    return result
def foo_a(n: int) :
    return (n+(n+1))/2

def beebadoobee(sadfa): 
    "adsfadfdasfa"
    return "NOTHING AGAIN AGAIN"
