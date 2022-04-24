# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 14:01:16 2021

@author: banik
"""

import numpy as np
from scipy import stats

def Gap_option(S, k1, k2, r, sigma, t, option='call', exact=False):
    if option not in ('call', 'put'):
        raise ValueError('option parameter must be one of "call" or "put".')
           
        n = Normal("x", 0.0, 1.0)
    
        if option == 'call':
            d1 = (np.ln(S / k2) + t * (r + sigma ** 2 / 2)) / (sigma * np.sqrt(t))
            d2 = d1 - sigma * np.sqrt(t)
            price =  (S * cdf(n)(d1) - np.exp(-r * t) * k1 * cdf(n)(d2))
        elif option == 'put':
            d1 = (np.ln(S / k1) + t * (r + sigma ** 2 / 2)) / (sigma * np.sqrt(t))
            d2 = d1 - sigma * np.sqrt(t)
            price = np.exp(-r * t) * k2 * cdf(n)(-d2) - S * cdf(n)(-d1)
        
    else:
        if option == 'call':
            d1 = (np.log(S / k2) + (r + sigma ** 2 / 2) * t) / (sigma * np.sqrt(t))
            d2 = d1 - sigma * np.sqrt(t)
            price = (S * stats.norm.cdf(d1) - np.exp(-r * t) * k1 * stats.norm.cdf(d2))
        elif option == 'put':
            d1 = (np.log(S / k1) + (r + sigma ** 2 / 2) * t) / (sigma * np.sqrt(t))
            d2 = d1 - sigma * np.sqrt(t)
            price = np.exp(-r * t) * k2 * stats.norm.cdf(-d2) - S * stats.norm.cdf(-d1)
        
    return price


call = Gap_option(60, 65,70, 0.10, 0.25, 1, option='call')
put = Gap_option(60, 65,70, 0.10, 0.25, 1, option='put')
print(f'Call price: ${round(call,2)}')
print(f'Put price: ${round(put,2)}')
