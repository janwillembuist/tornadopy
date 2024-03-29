import numpy as np
import matplotlib.pyplot as plt


# Tornado function
def plot(lows, highs, **kwargs):
    """Create tornadopy plot"""

    # Handle input
    if len(lows) != len(highs):
        raise AttributeError('Lows and highs must be of equal length')
    if isinstance(lows, list):
        lows = np.array(lows)
    if isinstance(highs, list):
        highs = np.array(highs)

    # Handle kwargs
    labels = kwargs.get('labels', None)
    center = kwargs.get('center', None)
    lines = kwargs.get('lines', False)
    ax = kwargs.get('ax', None)

    # Initialize plot
    if ax is None:
        ax = plt.gca()
    widths = highs-lows
    y_pos = np.argsort(np.argsort(widths))

    # Calculate coordinates
    if center is None:
        # Assume most bars have linear dependency
        center = np.median((highs + lows)/2)
        print(center)
    centers = np.ones_like(highs) * center
    l_parts = centers - lows
    r_parts = highs - centers

    # Carry out the plotting
    ax.barh(y_pos, l_parts, left=lows, align='center', height=0.8)
    ax.barh(y_pos, r_parts, left=centers, align='center')
    if lines is True:
        for id_y in y_pos:
            ax.plot([center, center], [id_y-0.4, id_y+0.4], 'k')
    ax.set_yticks(y_pos)
    if labels is not None:
        set_labels(labels)

    # Set default limit
    ax.set_xlim([0.9*(center-max(widths)), 1.1*(center+max(widths))])


def set_labels(labels):
    """Set labels on tornadopy chart"""
    ax = plt.gca()
    ax.set_yticklabels(labels)
