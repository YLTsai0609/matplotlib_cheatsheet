"""
An example of the 'science' theme.
install with lastest release

Error 
FileNotFoundError: [Errno 2] No such file or directory: 'latex': 'latex'
check issue no.2
https://github.com/garrettj403/SciencePlots/issues/2

basically line plot
"""

import numpy as np 
import matplotlib.pyplot as plt 

# from matplotlib import rc
# rc("text", usetex=False)

def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))

x = np.linspace(0.75, 1.25, 201)

with plt.style.context(['science','no-latex']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(xlabel='Voltage (mV)')
    ax.set(ylabel='Current (μA)')
    ax.autoscale(tight=True)
    fig.savefig('ex_science_plot/fig1.pdf')
    fig.savefig('ex_science_plot/fig1.jpg', dpi=300)

with plt.style.context(['science', 'ieee','no-latex']):
    fig, ax = plt.subplots()
    for p in [10, 20, 50]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(xlabel='Voltage (mV)')
    ax.set(ylabel='Current (μA)')
    ax.autoscale(tight=True)
    fig.savefig('ex_science_plot/fig2.pdf')
    fig.savefig('ex_science_plot/fig2.jpg', dpi=300)

with plt.style.context(['science', 'scatter','no-latex']):
    # scatter
    fig, ax = plt.subplots(figsize=(4,4))
    ax.plot([-2, 2], [-2, 2], 'k--')
    ax.fill_between([-2, 2], [-2.2, 1.8], [-1.8, 2.2], color='dodgerblue', alpha=0.2, lw=0)
    for i in range(7):
        x1 = np.random.normal(0, 0.5, 10)
        y1 = x1 + np.random.normal(0, 0.2, 10)
        ax.plot(x1, y1, label=r"#{}".format(i+1))
    ax.legend(title='Sample', loc=2)
    ax.set_xlabel(r"log10(LIRL⊙)")
    ax.set_ylabel(r"log10(L6.2L⊙)")
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    fig.savefig('ex_science_plot/fig3.pdf')
    fig.savefig('ex_science_plot/fig3.jpg', dpi=300)

with plt.style.context(['science', 'high-vis','no-latex']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(xlabel='Voltage (mV)')
    ax.set(ylabel='Current (μA)')
    ax.autoscale(tight=True)
    fig.savefig('ex_science_plot/fig4.pdf')
    fig.savefig('ex_science_plot/fig4.jpg', dpi=300)

with plt.style.context(['dark_background', 'science', 'high-vis','no-latex']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(xlabel='Voltage (mV)')
    ax.set(ylabel='Current (μA)')
    ax.autoscale(tight=True)
    fig.savefig('ex_science_plot/fig5.pdf')
    fig.savefig('ex_science_plot/fig5.jpg', dpi=300)

with plt.style.context(['science', 'notebook','no-latex']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(xlabel='Voltage (mV)')
    ax.set(ylabel='Current (μA)')
    ax.autoscale(tight=True)
    fig.savefig('ex_science_plot/fig10.pdf')
    fig.savefig('ex_science_plot/fig10.jpg', dpi=300)

# Plot different color cycles 

with plt.style.context(['science', 'bright','no-latex']):
    fig, ax = plt.subplots()
    for p in [5, 10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(xlabel='Voltage (mV)')
    ax.set(ylabel='Current (μA)')
    ax.autoscale(tight=True)
    fig.savefig('ex_science_plot/fig6.pdf')
    fig.savefig('ex_science_plot/fig6.jpg', dpi=300)

with plt.style.context(['science', 'vibrant','no-latex']):
    fig, ax = plt.subplots()
    for p in [5, 10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(xlabel='Voltage (mV)')
    ax.set(ylabel='Current (μA)')
    ax.autoscale(tight=True)
    fig.savefig('ex_science_plot/fig7.pdf')
    fig.savefig('ex_science_plot/fig7.jpg', dpi=300)

with plt.style.context(['science', 'muted','no-latex']):
    fig, ax = plt.subplots()
    for p in [5, 7, 10, 15, 20, 30, 38, 50, 100, 500]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order', fontsize=7)
    ax.set(xlabel='Voltage (mV)')
    ax.set(ylabel='Current (μA)')
    ax.autoscale(tight=True)
    fig.savefig('ex_science_plot/fig8.pdf')
    fig.savefig('ex_science_plot/fig8.jpg', dpi=300)

with plt.style.context(['science', 'retro','no-latex']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(xlabel='Voltage (mV)')
    ax.set(ylabel='Current (μA)')
    ax.autoscale(tight=True)
    fig.savefig('ex_science_plot/fig9.pdf')
    fig.savefig('ex_science_plot/fig9.jpg', dpi=300)

with plt.style.context(['science', 'grid','no-latex']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(xlabel='Voltage (mV)')
    ax.set(ylabel='Current (μA)')
    ax.autoscale(tight=True)
    fig.savefig('ex_science_plot/fig11.pdf')
    fig.savefig('ex_science_plot/fig11.jpg', dpi=300)
