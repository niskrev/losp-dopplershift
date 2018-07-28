"""Makes special plots for our library."""

import matplotlib.pyplot as plt

import numpy as np


def random_plot(num_points, seed=None):
    """Make a random plot of some size for science.

    Makes a random plot of num_points and colored randomly. While this probably
    sounds silly, it sometimes shows more patterns that some real dataself.

    Parameters
    ----------
    num_points : integer
        The number of random points to plot on the graph.
    seed : integer, optional
        Seed value for the random number generator for reproducible plots.

    Returns
    -------
    matplotlib.figure.Figure : figure object
    matplotlib.axes._subplots.AxesSubplot : axes

    """
    if seed:
        np.random.seed(seed)
    x = np.random.rand(num_points)
    y = np.random.rand(num_points)
    z = np.random.rand(num_points)

    fig = plt.figure(figsize=(5, 5))
    ax = plt.subplot(1, 1, 1)
    ax.scatter(x, y, c=z)
    return fig, ax
