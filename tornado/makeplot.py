import numpy as np
import matplotlib.pyplot as plt


# Tornado function
def tornado(lows, highs, **kwargs):
    """Create tornado plot"""

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

    # Initialize plot
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
        ax.set_yticklabels(labels)
    ax.set_xlim([min(lows)-max(widths)/20, max(highs)+max(widths)/20])