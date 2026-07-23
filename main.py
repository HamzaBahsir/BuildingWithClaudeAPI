def greeting():
    print("Hi There")


def calculate_pi_to_5th_digit():
    """
    Calculate pi to the 5th digit using the Machin formula.
    Pi ≈ 3.14159
    
    Uses the Machin formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    """
    from decimal import Decimal, getcontext
    
    # Set precision high enough to calculate to 5 decimal places
    getcontext().prec = 50
    
    def arctan(x, num_terms=500):
        """Calculate arctan(x) using Taylor series expansion."""
        x = Decimal(x)
        power = x
        result = power
        
        for n in range(1, num_terms):
            power *= -x * x
            result += power / (2 * n + 1)
        
        return result
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi = 4 * (4 * arctan(Decimal(1) / Decimal(5)) - arctan(Decimal(1) / Decimal(239)))
    
    return float(pi)