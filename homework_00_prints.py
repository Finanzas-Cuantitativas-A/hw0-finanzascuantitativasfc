# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:37:42 2020

@author: Meva
"""
import json
# import libraries and functions
import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2



# import our own function and class files and reload
import file_functions
importlib.reload(file_functions)
import file_classes
importlib.reload(file_classes)
import requests


#Escribe aqui tu numero de cuenta. Si tienes dudas consulta el README.md
numeroDeCuenta = ''


'''
HOMEWORK 0.

You can submit the homework as many times as you like until the deadline. The
final note will be the maximum note of all your submits.

Every submit with pytest is register on our record!

After the deadline, we will send our solution.

You can test your code on your computer before sending it to github.
To test your code, you can run the ' pytest ' command on your computer or select
run test option in spyder and select test_homework01.py .
Remember to install pytest using $pip install pytest or $conda install pytest
'''
def tarea0():

    # inputs
    inputs = file_classes.distribution_input()
    inputs.data_type = 'real'
    inputs.variable_name = '^STOXX'

    # computations
    dm = file_classes.distribution_manager(inputs)
    dm.load_timeseries()
    dm.compute()
    # You must return 
    # median rounded to 4 decimals
    # var_95 rounded to 6 decimals
    # is_normal 
    return 


#NO MODIFICAR
def settings(numero_cuenta):
    r = requests.post('http://meva.sytes.net/ulmo/dataHW0.php',
                      {'numero_cuenta': numero_cuenta})
    data = json.loads(r.text)
    rics = data['rics']
    benchmarks = data['benchmarks']
    df_student = tarea0(benchmarks, rics)
    print('--------------------------------------------------------')
    data_json = df_student.to_json()
    payload = {'json_data': data_json, 'numero_cuenta': numero_cuenta}
    r = requests.post(
        'http://meva.sytes.net/ulmo/evaluateHW0.php', json=payload)
    print(r.text)
    return(r.text)
