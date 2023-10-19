#!/usr/bin/env python3

if __name__ == '__main__':
    import numpy as np
    from multinormal import MultiNormal

    C = np.array([[36, -30, 15], [-30, 100, -20], [15, -20, 25]])
    mn = MultiNormal(C)
    print(C)
    print(mn.pdf(np.array([[1], [2], [3]])))
