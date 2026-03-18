import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    num=len(x)
    x=np.asarray(x,dtype=float)
    p=np.asarray(p,dtype=float)
    if len(x) != len(p):
        raise ValueError("x and p must have the same length")

    if np.any(p < 0):
        raise ValueError("probabilities must be non-negative")

    if not np.isclose(np.sum(p), 1.0):
        raise ValueError("probabilities must sum to 1")
        
    E = 0.0
    for i in range(num):
        E += x[i] * p[i]
        
    return  E
