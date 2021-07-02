# import libraries and functions
import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2

# import our own function and class files and reload
import file_classes
importlib.reload(file_classes)
import file_classes
importlib.reload(file_classes)
import requests


import homework_00_prints as hw;



def test_1():
    assert hw.tarea0()[0] == 0.0006
    assert hw.tarea0()[1] == -0.015768
    assert hw.tarea0()[2] == False
