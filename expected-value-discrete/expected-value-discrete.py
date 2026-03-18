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
        raise ValueError()

    if np.any(p < 0):
        raise ValueError()

    if not np.isclose(np.sum(p), 1.0):
        raise ValueError()
        
    E = 0.0
    for i in range(num):
        E += x[i] * p[i]
        
    return  E
