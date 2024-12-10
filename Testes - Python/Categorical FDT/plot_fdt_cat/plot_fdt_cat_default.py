import matplotlib.pyplot as plt
import numpy as np

def plot_fdt_cat(x, 
                 plot_type='fb',
                 v=False,
                 v_round=2,
                 v_pos=3,
                 xlab=None,
                 xlas=0,
                 ylab=None,
                 y2lab=None,
                 y2cfp=np.arange(0, 101, 25),
                 col='0.4',
                 xlim=None,
                 ylim=None,
                 main=None,
                 box=False):
    """
    Plot a frequency distribution table (FDT) for categorical data.

    Parameters:
    x (DataFrame): Input DataFrame with columns including category labels, 
                   frequencies, relative frequencies, and cumulative frequencies.
    plot_type (str): Type of plot to generate. Options include:
                     'fb' - bar plot with frequencies,
                     'fp' - polygon plot with frequencies,
                     'fd' - dot chart with frequencies,
                     'pa' - Pareto plot with cumulative frequencies,
                     'rfb' - bar plot with relative frequencies,
                     'rfp' - polygon plot with relative frequencies,
                     'rfd' - dot chart with relative frequencies,
                     'rfpb' - bar plot with relative frequencies in %,
                     'rfpp' - polygon plot with relative frequencies in %,
                     'rfpd' - dot chart with relative frequencies in %,
                     'cfb' - bar plot with cumulative frequencies,
                     'cfp' - polygon plot with cumulative frequencies,
                     'cfd' - dot chart with cumulative frequencies,
                     'cfpb' - bar plot with cumulative frequencies in %,
                     'cfpp' - polygon plot with cumulative frequencies in %,
                     'cfpd' - dot chart with cumulative frequencies in %.
    v (bool): If True, display values on the plot.
    v_round (int): Decimal places for values displayed on the plot.
    v_pos (int): Vertical position for value labels.
    xlab (str): Label for the x-axis.
    xlas (int): Rotation angle for x-axis labels. Defaults to 0.
    ylab (str): Label for the y-axis.
    y2lab (str): Label for the secondary y-axis (used in Pareto plot).
    y2cfp (array): Percentage ticks for cumulative frequency y-axis in Pareto plot.
    col (str): Color for plot elements. Default is '0.4' (gray).
    xlim (tuple): Limits for the x-axis.
    ylim (tuple): Limits for the y-axis.
    main (str): Title for the plot.
    box (bool): If True, display a box around the plot.

    """

    # Helper function for bar plot
    def plot_b(y, categories):
        fig, ax = plt.subplots()
        bar_positions = np.arange(len(categories))
        
        ax.bar(bar_positions, y, color=col, edgecolor='black')
        ax.set_xticks(bar_positions)
        ax.set_xticklabels(categories, rotation=xlas * 90)
        
        if xlab:
            ax.set_xlabel(xlab)
        if ylab:
            ax.set_ylabel(ylab)
        if main:
            ax.set_title(main)
        if box:
            ax.spines['top'].set_visible(True)
            ax.spines['right'].set_visible(True)
        
        if v:
            for i, val in enumerate(y):
                ax.text(i, val, f"{round(val, v_round)}", ha='center', va='bottom')
        
        plt.show()
    
    # Helper function for polygon plot
    def plot_p(y, categories):
        fig, ax = plt.subplots()
        ax.plot(range(len(categories)), y, 'o-', color=col, markersize=5)
        
        ax.set_xticks(range(len(categories)))
        ax.set_xticklabels(categories, rotation=xlas * 90)
        
        if xlab:
            ax.set_xlabel(xlab)
        if ylab:
            ax.set_ylabel(ylab)
        if main:
            ax.set_title(main)
        
        if v:
            for i, val in enumerate(y):
                ax.text(i, val, f"{round(val, v_round)}", ha='center', va='bottom')
        
        plt.show()

    # Helper function for dotchart
    def plot_d(y, categories):
        fig, ax = plt.subplots()
        
        ax.plot(y, range(len(categories)), 'o', color=col)
        ax.set_yticks(range(len(categories)))
        ax.set_yticklabels(categories)
        
        if xlab:
            ax.set_xlabel(xlab)
        if ylab:
            ax.set_ylabel(ylab)
        if main:
            ax.set_title(main)
        
        if v:
            for i, val in enumerate(y):
                ax.text(val, i, f"{round(val, v_round)}", ha='right')
        
        plt.show()

    # Helper function for pareto plot
    def plot_pa(y, cf, cfp, categories):
        fig, ax1 = plt.subplots()
        
        bar_positions = np.arange(len(categories))
        
        # Bar plot
        ax1.bar(bar_positions, y, color=col, edgecolor='black')
        ax1.set_xticks(bar_positions)
        ax1.set_xticklabels(categories, rotation=xlas * 90)
        
        if xlab:
            ax1.set_xlabel(xlab)
        if ylab:
            ax1.set_ylabel(ylab)
        if main:
            ax1.set_title(main)
        
        # Set y-axis limit based on cumulative frequency
        ax1.set_ylim(0, max(cf) * 1.1)
        
        # Cumulative frequency plot
        ax2 = ax1.twinx()
        ax2.plot(bar_positions, cf, color='blue', marker='o', linestyle='-', markersize=5)
        ax2.set_ylabel(y2lab)
        ax2.set_ylim(0, max(cf) * 1.1)  # Ensure y-axis limit for cumulative frequency

        plt.show()

    # Call appropriate plot type based on `plot_type` argument
    categories = x['Category']
    if plot_type == 'fb':
        y = x.iloc[:, 1]
        xlab = xlab or 'Category'
        ylab = ylab or 'Frequency'
        ylim = ylim or (0, max(y) * 1.3)
        plot_b(y, categories)
        
    elif plot_type == 'fp':
        y = x.iloc[:, 1]
        xlab = xlab or 'Category'
        ylab = ylab or 'Frequency'
        ylim = ylim or (0, max(y) * 1.2)
        plot_p(y, categories)
        
    elif plot_type == 'fd':
        y = x.iloc[:, 1]
        xlab = xlab or 'Frequency'
        plot_d(y, categories)
        
    elif plot_type == 'pa':
        y = x.iloc[:, 1]
        cf = x.iloc[:, 4]  # Cumulative frequency
        cfp = x.iloc[:, 5]  # Cumulative frequency percentage
        xlab = xlab or 'Category'
        ylab = ylab or 'Frequency'
        y2lab = y2lab or 'Cumulative frequency, (%)'
        ylim = ylim or (0, sum(y) * 1.1)
        plot_pa(y, cf, cfp, categories)
        
    elif plot_type == 'rfb':
        y = x.iloc[:, 2]
        xlab = xlab or 'Category'
        ylab = ylab or 'Relative frequency'
        plot_b(y, categories)
        
    elif plot_type == 'rfp':
        y = x.iloc[:, 2]
        xlab = xlab or 'Category'
        ylab = ylab or 'Relative frequency'
        ylim = ylim or (0, max(y) * 1.2)
        plot_p(y, categories)
        
    elif plot_type == 'rfd':
        y = x.iloc[:, 2]
        xlab = xlab or 'Relative frequency'
        plot_d(y, categories)
        
    elif plot_type == 'rfpb':
        y = x.iloc[:, 3]
        xlab = xlab or 'Category'
        ylab = ylab or 'Relative frequency (%)'
        plot_b(y, categories)
        
    elif plot_type == 'rfpp':
        y = x.iloc[:, 3]
        xlab = xlab or 'Category'
        ylab = ylab or 'Relative frequency (%)'
        ylim = ylim or (0, max(y) * 1.2)
        plot_p(y, categories)
        
    elif plot_type == 'rfpd':
        y = x.iloc[:, 3]
        xlab = xlab or 'Relative frequency (%)'
        plot_d(y, categories)
        
    elif plot_type == 'cfb':
        y = x.iloc[:, 4]
        xlab = xlab or 'Category'
        ylab = ylab or 'Cumulative frequency'
        plot_b(y, categories)
        
    elif plot_type == 'cfp':
        y = x.iloc[:, 4]
        xlab = xlab or 'Category'
        ylab = ylab or 'Cumulative frequency'
        ylim = ylim or (0, max(y) * 1.2)
        plot_p(y, categories)
        
    elif plot_type == 'cfd':
        y = x.iloc[:, 4]
        xlab = xlab or 'Cumulative frequency'
        plot_d(y, categories)
        
    elif plot_type == 'cfpb':
        y = x.iloc[:, 5]
        xlab = xlab or 'Category'
        ylab = ylab or 'Cumulative frequency (%)'
        plot_b(y, categories)
        
    elif plot_type == 'cfpp':
        y = x.iloc[:, 5]
        xlab = xlab or 'Category'
        ylab = ylab or 'Cumulative frequency (%)'
        ylim = ylim or (0, max(y) * 1.2)
        plot_p(y, categories)
        
    elif plot_type == 'cfpd':
        y = x.iloc[:, 5]
        xlab = xlab or 'Cumulative frequency (%)'
        plot_d(y, categories)
