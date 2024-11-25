# -*- coding: utf-8 -*-
"""
Some tests for our code
"""
__all__ = [

]

# ====== IMPORT LIBRARIES ======

import numpy as np
import matplotlib.pyplot as plt

import smoothn


# ===================================================================

def test_plot(*args, **kwargs):

    figsize = kwargs.pop('figsize', (16, 9))

    fig, ax = plt.subplots(figsize=figsize)

    for arg in args:
        ax.plot(arg, **kwargs)
        ax.plot(smoothn.smoothn(arg), **kwargs)

    plt.show()


# ===================================================================

if __name__ == '__main__':

    shape = (200, )
    data = np.sin(np.linspace(0, 5*2*np.pi, shape[0]))
    data *= 0.1 * np.random.randn(*shape)
    data += 0.05 * np.random.randn(*shape)

    test_plot(data)
