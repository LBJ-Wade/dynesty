import numpy as np
import os
'''
Here we setup a common seed for all the tests
But we also allow to set the seed through DYNESTY_TEST_RANDOMSEED
environment variable.
That allows to run long tests by looping over seed value to catch
potentially rare behaviour
'''


def get_rstate(seed=None):
    if seed is None:
        kw = 'DYNESTY_TEST_RANDOMSEED'
        if kw in os.environ:
            seed = int(os.environ[kw])
        else:
            seed = 56432
        # seed the random number generator
    return np.random.default_rng(seed)


def get_printing():
    kw = 'DYNESTY_TEST_PRINTING'
    if kw in os.environ:
        return int(os.environ[kw])
    else:
        return False
