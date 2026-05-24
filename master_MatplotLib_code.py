# ============================================================
#              MATPLOTLIB MASTER LEARNING SCRIPT
# ============================================================
#
# Goal:
# Learn almost all important matplotlib concepts from ONE file.
#
# Recommended workflow:
# 1. Run this script.
# 2. Change ONE thing at a time.
# 3. Observe what changes in the plot.
#
# This script teaches:
#
# ✔ line plot
# ✔ multiple curves
# ✔ legend
# ✔ legend spacing
# ✔ x/y labels
# ✔ title
# ✔ linear plot
# ✔ log-log plot
# ✔ xlim / ylim
# ✔ ticks
# ✔ tick size
# ✔ line width
# ✔ linestyle
# ✔ marker
# ✔ alpha transparency
# ✔ zorder
# ✔ text on plot
# ✔ grid
# ✔ subplot
# ✔ plot style
# ✔ figure size
# ✔ saving figure
# ✔ LaTeX labels
#
# ============================================================

# -----------------------------
# IMPORT LIBRARIES
# -----------------------------

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# GLOBAL STYLE SETTINGS
# ============================================================
#
# These affect ALL plots.
#
# Think of rcParams as your "global plotting configuration".
#

plt.rcParams.update({

    # Font size everywhere
    "font.size": 16,

    # Figure size in inches
    "figure.figsize": (8,6),

    # Better quality saved figure
    "figure.dpi": 120,

    # Axis line thickness
    "axes.linewidth": 1.5,

    # Tick sizes
    "xtick.major.size": 6,
    "ytick.major.size": 6,

    # Tick thickness
    "xtick.major.width": 1.5,
    "ytick.major.width": 1.5,

    # Tick direction
    "xtick.direction": "in",
    "ytick.direction": "in",

    # Show ticks on top/right also
    "xtick.top": True,
    "ytick.right": True,
    #command mirrors the MAIN bottom-axis ticks onto the top border ****

    # Grid transparency
    "grid.alpha": 0.3,

    # Legend frame
    "legend.frameon": True,

    # Legend font size
    "legend.fontsize": 13,

    # Use LaTeX rendering (requires latex installed)
    # Uncomment if installed
    # "text.usetex": True,
})




# plt.style.use('ggplot')
#plt.rc('text', usetex=True)
# plt.rc('axes', labelsize='x-large')
# plt.rc(('xtick','ytick'), labelsize='x-large')
# plt.rc(('xtick', 'ytick'), direction='in')
# plt.rc(('xtick.major', 'ytick.major'), size=6)
# plt.rc(('xtick.minor', 'ytick.minor'), size=3)
# plt.rc('xtick', top=True)
# plt.rc('ytick', right=True)


# ============================================================
# CREATE DATA
# ============================================================

# 200 equally spaced points between 0.1 and 10
x = np.linspace(0.1,10,200)

# Some functions
y1 = x
y2 = x**2
y3 = np.exp(x/3)


# ============================================================
# CREATE FIGURE AND AXES
# ============================================================
#
# Figure = whole canvas/page
# Axes   = actual plot area
#

fig, ax = plt.subplots()





# ============================================================
# AXIS LIMITS
# ============================================================

ax.set_xlim(0,10)

ax.set_ylim(0,30)
# it must be placed before axvspan and axhspan ****




# ============================================================
# BASIC LINE PLOTS
# ============================================================

# ------------------------------------------------------------
# plot(x,y)
#
# linewidth = line thickness
# linestyle = solid/dashed/etc
# color     = line color
# alpha     = transparency
# label     = legend label
# zorder    = what appears on top
# ------------------------------------------------------------

ax.plot(
    x,
    y1,

    color='blue',

    linewidth=3,

    linestyle='-',

    alpha=0.9,

    label=r'$y=x$',

    zorder=3
)


# ------------------------------------------------------------
# Another curve
# ------------------------------------------------------------

ax.plot(
    x,
    y2,

    color='red',

    linewidth=2,

    linestyle='--',

    alpha=0.8,

    label=r'$y=x^2$',

    zorder=2
)


# ------------------------------------------------------------
# Another curve with markers
# ------------------------------------------------------------

ax.plot(
    x,
    y3,

    color='green',

    linewidth=2,

    linestyle=':',

    marker='o',

    markersize=4,

    markevery=15,

    alpha=0.7,

    label=r'$y=e^{x/3}$',

    zorder=1
)





# ============================================================
# VERTICAL LINE
# ============================================================
#
# axvline(x-position)
#
# Useful for:
# - benchmark values
# - phase transitions
# - horizon crossing
# - constraints
#

ax.axvline(

    x=8,

    color='black',

    linestyle='--',

    linewidth=2,

    alpha=0.8,

    label='Vertical line'
)




# ============================================================
# HORIZONTAL LINE
# ============================================================
#
# axhline(y-position)
#
# Useful for:
# - observational bounds
# - thresholds
# - critical values
#

ax.axhline(

    y=15,

    color='orange',

    linestyle='-.',

    linewidth=2,

    alpha=0.8,

    label='Horizontal line'
)




# ============================================================
# SHADED REGIONS
# ============================================================
#
# axvspan(xmin, xmax)
# -> vertical shaded region
#
# axhspan(ymin, ymax)
# -> horizontal shaded region
#
# Useful for:
# - excluded regions
# - observational bounds
# - allowed parameter space
#

# Example:
#
ax.axvspan(

    8,

    ax.get_xlim()[1],

    color='plum',

    alpha=0.3
)

# ============================================================
# HORIZONTAL SHADED REGION
# ============================================================

ax.axhspan(

    29,

    ax.get_ylim()[1],

    color='#5DA5DA',

    alpha=0.2,

    label='Horizontal shaded region'
)




# ============================================================
# FILL BETWEEN CURVE AND AXIS
# ============================================================
#
# Useful for:
# - shaded area
# - integrated region
# - excluded parameter space
#

# ax.fill_between(
# 
#     x,
# 
#     y1,
# 
#     0,
# 
#     color='blue',
# 
#     alpha=0.1
# )

ax.fill_between(

    x,

    y1,
    y2,

    where=(y2 > y1),

    alpha=0.3
)


# ============================================================
# AXIS LABELS
# ============================================================

ax.set_xlabel(
    r'$x$',
    fontsize=18,
    labelpad=10
)

ax.set_ylabel(
    r'$y$',
    fontsize=18,
    labelpad=10
)



# ============================================================
# TOP X-AXIS
# ============================================================

#ax_top = ax.secondary_xaxis('top') #normal mirrored ticks (0 2 4 6 ...) ***

# ax_top.set_xlabel(
# 
#     'Top x-axis label',
# 
#     fontsize=16
# )



# ============================================================
# RIGHT Y-AXIS
# ============================================================

ax_right = ax.secondary_yaxis('right')

ax_right.set_ylabel(

    'Right y-axis label',

    fontsize=16
)




# ============================================================
# SECONDARY AXES
# ============================================================
#
# Useful for:
# - different physical scales
# - transformed variables
# - custom labels
# - auxiliary information
# - cosmology/HEP scales
#
#
# ------------------------------------------------------------
# METHOD 1 :
# ANALYTIC TRANSFORMATION
# ------------------------------------------------------------
#
# Example:
#
# Top axis = 2*x
#
# Requires:
#
# 1. forward transformation
# 2. inverse transformation
#
# Useful when simple analytic relation exists.
#

def x_to_top(x):

    return 2*x


def top_to_x(x):

    return x/2


ax_top = ax.secondary_xaxis(

    'top',
    
    # functions=(forward_function, inverse_function)
    functions=(x_to_top, top_to_x)
)

# ax_top.set_xlabel(
# 
#     r'Top axis : $2x$',
# 
#     fontsize=16
# )


# ------------------------------------------------------------
# METHOD 2 :
# CUSTOM TICKS + CUSTOM LABELS
# ------------------------------------------------------------
#
# Very common in research papers.
#
# Useful when:
# - no simple formula exists
# - irregular physical mapping
# - custom scales
# - phenomenology plots
#
# Tick positions are given in MAIN-axis coordinates.
#

# ax_top.set_xticks(
# 
#     [1,3,5,7,9]
# )
# 
# ax_top.set_xticklabels(
# 
#     ['A','B','C','D','E']
# )


# ------------------------------------------------------------
# RIGHT Y-AXIS
# ------------------------------------------------------------
#
# Left axis   : y
# Right axis  : y/10
#

# def y_to_right(y):
# 
#     return y/10
# 
# 
# def right_to_y(y):
# 
#     return 10*y
# 
# 
# ax_right = ax.secondary_yaxis(
# 
#     'right',
#     
#     # functions=(forward_function, inverse_function)
#     functions=(y_to_right, right_to_y) 
# )

# ax_right.set_ylabel(
# 
#     r'Right axis : $y/10$',
# 
#     fontsize=16
# )


# ------------------------------------------------------------
# CUSTOM RIGHT-AXIS TICKS
# ------------------------------------------------------------

ax_right.set_yticks(

    [0,10,20,30]
)

ax_right.set_yticklabels(

    ['L','M','H','E']
)





# ============================================================
# TITLE
# ============================================================

ax.set_title(
    'Matplotlib Master Learning Plot',
    fontsize=20,
    pad=15
)



# ============================================================
# SCIENTIFIC NOTATION
# ============================================================

ax.ticklabel_format(

    style='sci',

    axis='y',

    scilimits=(0,0)
)


# ============================================================
# LOG SCALE
# ============================================================
#
# Uncomment to learn log plots
#

# ax.set_xscale('log')
# ax.set_yscale('log')


# ============================================================
# CUSTOM TICKS
# ============================================================

ax.set_xticks([0,2,4,6,8,10])

ax.set_yticks([0,5,10,15,20,25,30])


# ============================================================
# TICK LABEL SIZE
# ============================================================

ax.tick_params(
    axis='both',

    which='major',

    labelsize=14
)



# ============================================================
# MINOR TICKS
# ============================================================

ax.minorticks_on()

ax.tick_params(

    axis='both',

    which='minor',

    direction='in',

    length=4
)


# ============================================================
# BACKGROUND STYLING
# ============================================================
#
ax.set_facecolor('whitesmoke')


# ============================================================
# SPINES (PLOT BORDERS)
# ============================================================
#
# Spines are the border lines around the plot.
#
# Available spines:
#
# 'top'
# 'bottom'
# 'left'
# 'right'
#
# Useful for:
# - cleaner plots
#

# Hide top border
# ax.spines['top'].set_visible(False)

# Hide right border
# ax.spines['right'].set_visible(False)

# Change spine thickness
# ax.spines['left'].set_linewidth(2)

# Change spine color
# ax.spines['bottom'].set_color('red')




# ============================================================
# GRID
# ============================================================

ax.grid(True)


# ============================================================
# TEXT INSIDE PLOT
# ============================================================

ax.text(

    5,          # x-position
    25,         # y-position

    'Example text',

    fontsize=16,

    color='black',

    rotation=0,

    alpha=0.8,

    bbox=dict(
        facecolor='white',
        alpha=0.8
    )
)



# ============================================================
# ANNOTATION
# ============================================================

ax.annotate(

    'Interesting point',

    xy=(3,9),

    xytext=(5,15),

    arrowprops=dict(
        arrowstyle='->',
        lw=2
    )
)



# ============================================================
# SCATTER PLOT
# ============================================================
#
# scatter(x,y)
#
# s          = marker size
# c          = color
# alpha      = transparency
# marker     = marker shape
# edgecolors = boundary color
#
# Useful for:
# - parameter scans
# - Monte Carlo points
# - observational data
# - viable regions
#
#
#
# ------------------------------------------------------------
# COMMON MARKER TYPES
# ------------------------------------------------------------
#
# 'o'  = circle
# 's'  = square
# '^'  = triangle up
# 'v'  = triangle down
# '*'  = star
# 'x'  = x-mark
# '+'  = plus
# 'D'  = diamond
# '.'  = point
# ','  = pixel
# '<'  = triangle left
# '>'  = triangle right
# 'p'  = pentagon
# 'h'  = hexagon
#
# Example:
#
# marker='^'
#
# ------------------------------------------------------------


# Random scatter data
x_scatter = np.random.uniform(0,10,40)

y_scatter = 2*x_scatter + np.random.normal(0,2,40)


# ax.scatter(
# 
#     x_scatter,
#     y_scatter,
# 
#     s=80,
# 
#     c='purple',
# 
#     alpha=0.7,
# 
#     marker='o',
# 
#     edgecolors='black',
# 
#     label='Scatter points',
# 
#     zorder=5
# )




scatter = ax.scatter(

    x_scatter,
    y_scatter,

    c=y_scatter,

    cmap='viridis'
)

cbar = plt.colorbar(scatter)

cbar.set_label('Color scale')

# ============================================================
# ERROR BAR PLOT
# ============================================================
#
# Useful for:
# - observational data
# - experimental uncertainties
# - measured quantities
#

# Fake experimental data
x_err = np.linspace(1,9,8)

y_err = np.sin(x_err) + 5

# Symmetric uncertainties
y_unc = 0.3*np.ones_like(y_err)

ax.errorbar(

    x_err,
    y_err,

    yerr=y_unc,

    fmt='o',

    color='black',

    capsize=4,

    elinewidth=1.5,

    markersize=6,

    label='Error bars'
)



# ============================================================
# HISTOGRAM
# ============================================================
#
# Useful for:
# - distributions
# - MCMC chains
# - sampled parameters
#

random_data = np.random.normal(0,1,1000)

# Uncomment to learn histogram
#
ax.hist(

    random_data,
    
    bins=30, #Divide the data range into 30 intervals (boxes/buckets)
    
    histtype='step',

    linewidth=2,
    
    alpha=0.5
 )



# ============================================================
# LEGEND
# ============================================================

ax.legend(

    loc='upper left',

    # space between legend entries
    labelspacing=0.5,

    # length of line in legend
    handlelength=2,

    # spacing from plot boundary
    borderpad=0.8
)



# Automatically fixes spacing issues
plt.tight_layout()
# this must be before savefig ***



# ============================================================
# SAVE FIGURE
# ============================================================
#
# IMPORTANT FOR RESEARCH
#
# PDF gives vector graphics.
# Preferred for papers.
#

plt.savefig(

    'master_plot.pdf',

    bbox_inches='tight'
)




# ============================================================
# SHOW PLOT
# ============================================================

plt.show()