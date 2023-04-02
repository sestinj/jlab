import numpy as np

def gaussian(x, mu, sigma):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sigma, 2.)))

def gaussian2d(x, y, mu_x, mu_y, sigma_x, sigma_y):
    return np.exp(-np.power(x - mu_x, 2.) / (2 * np.power(sigma_x, 2.)) - np.power(y - mu_y, 2.) / (2 * np.power(sigma_y, 2.)))

def poisson(x, mu):
    return np.power(mu, x) * np.exp(-mu) / np.math.factorial(x)