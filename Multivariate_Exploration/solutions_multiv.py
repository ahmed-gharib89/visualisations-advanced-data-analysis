"""
Script with solutions for all workspace assignments in the Multivariate
Exploration of Data lesson.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def encodings_solution_1():
    """
    Solution for Question 1 in encodings practice: see if pokemon speed has a
    clear relationship with defense and special defense.
    """
    sol_string = ["When creating the plot, I made the figure size bigger and set",
                  "axis limits to zoom into the majority of data points. I might",
                  "want to apply some manual jitter to the data since I suspect",
                  "there to be a lot of overlapping points. From the plot as given,",
                  "I see a slight increase in speed as both defense and special",
                  "defense increase. However, the brightest points seem to be clumped",
                  "up in the center in the 60-80 defense and special defense ranges",
                  "with the two brightest points on the lower left of the diagonal."]
    print((" ").join(sol_string))

    # data setup
    pokemon = pd.read_csv('../data/pokemon.csv')

    # plotting
    plt.figure(figsize = [8,6])
    plt.scatter(data = pokemon, x = 'defense', y = 'special-defense',
                c = 'speed')
    plt.colorbar(label = 'Speed')
    plt.xlim(0,160)
    plt.ylim(15,160)
    plt.xlabel('Defense')
    plt.ylabel('Special Defense')


def encodings_solution_2():
    """
    Solution for Question 2 in encodings practice: compare the heights and
    weights for two extreme types of pokemon, fairy and dragon.
    """
    sol_string = ["After subsetting the data, I used FacetGrid to set up and",
                  "generate the plot. I used the .set() method for FacetGrid",
                  "objects to set the x-scaling and tick marks. The plot shows",
                  "the drastic difference in sizes and weights for the Fairy",
                  "and Dragon Pokemon types."]
    print((" ").join(sol_string))

    # data setup
    pokemon = pd.read_csv('../data/pokemon.csv')
    type_cols = ['type_1','type_2']
    non_type_cols = pokemon.columns.difference(type_cols)
    pkmn_types = pokemon.melt(id_vars = non_type_cols, value_vars = type_cols, 
                              var_name = 'type_level', value_name = 'type').dropna()

    pokemon_sub = pkmn_types.loc[pkmn_types['type'].isin(['fairy','dragon'])]

    # plotting
    g = sb.FacetGrid(data = pokemon_sub, hue = 'type', size = 5)
    g.map(plt.scatter, 'weight','height')
    g.set(xscale = 'log') # need to set scaling before customizing ticks
    x_ticks = [0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000]
    g.set(xticks = x_ticks, xticklabels = x_ticks)
    g.add_legend()


def adaptedplot_solution_1():
    """
    Solution for Question 1 in adapted plot practice: plot the city vs. highway
    mileage for each vehicle class.
    """
    sol_string = ["Due to overplotting, I've taken a faceting approach to this task.",
                  "There don't seem to be any obvious differences in the main cluster",
                  "across vehicle classes, except that the minicompact and large",
                  "sedans' arcs are thinner than the other classes due to lower",
                  "counts. The faceted plots clearly show that most of the high-efficiency",
                  "cars are in the mid-size and compact car classes."]
    print((" ").join(sol_string))

    # data setup
    fuel_econ = pd.read_csv('../data/fuel_econ.csv')

    sedan_classes = ['Minicompact Cars', 'Subcompact Cars', 'Compact Cars', 'Midsize Cars', 'Large Cars']
    pd_ver = pd.__version__.split(".")
    if (int(pd_ver[0]) > 0) or (int(pd_ver[1]) >= 21): # v0.21 or later
        vclasses = pd.api.types.CategoricalDtype(ordered = True, categories = sedan_classes)
        fuel_econ['VClass'] = fuel_econ['VClass'].astype(vclasses)
    else: # compatibility for v.20
        fuel_econ['VClass'] = fuel_econ['VClass'].astype('category', ordered = True,
                                                         categories = sedan_classes)

    # plotting
    g = sb.FacetGrid(data = fuel_econ, col = 'VClass', size = 3, col_wrap = 3)
    g.map(plt.scatter, 'city', 'highway', alpha = 1/5)


def adaptedplot_solution_2():
    """
    Solution for Question 2 in adapted plot practice: plot the engine size
    distribution against vehicle class and fuel type.
    """
    sol_string = ["I went with a clustered box plot on this task since there were",
                  "too many levels to make a clustered violin plot accessible.",
                  "The plot shows that in each vehicle class, engine sizes were",
                  "larger for premium-fuel cars than regular-fuel cars. Engine size",
                  "generally increased with vehicle class within each fuel type,",
                  "but the trend was noisy for the smallest vehicle classes."]
    print((" ").join(sol_string))

    # data setup
    fuel_econ = pd.read_csv('../data/fuel_econ.csv')

    sedan_classes = ['Minicompact Cars', 'Subcompact Cars', 'Compact Cars', 'Midsize Cars', 'Large Cars']
    pd_ver = pd.__version__.split(".")
    if (int(pd_ver[0]) > 0) or (int(pd_ver[1]) >= 21): # v0.21 or later
        vclasses = pd.api.types.CategoricalDtype(ordered = True, categories = sedan_classes)
        fuel_econ['VClass'] = fuel_econ['VClass'].astype(vclasses)
    else: # compatibility for v.20
        fuel_econ['VClass'] = fuel_econ['VClass'].astype('category', ordered = True,
                                                         categories = sedan_classes)
    fuel_econ_sub = fuel_econ.loc[fuel_econ['fuelType'].isin(['Premium Gasoline', 'Regular Gasoline'])]

    # plotting
    sb.boxplot(data = fuel_econ_sub, x = 'VClass', y = 'displ', hue = 'fuelType')
    plt.legend(loc = 6, bbox_to_anchor = (1.0, 0.5)) # legend to right of figure
    plt.xticks(rotation = 15)


def additionalplot_solution_1():
    """
    Solution for Question 1 in additional plot practice: create a plot matrix
    for five numeric variables in the fuel economy dataset.
    """
    sol_string = ["I set up my PairGrid to plot scatterplots off the diagonal",
                  "and histograms on the diagonal. The intersections where 'co2'",
                  "meets the fuel mileage measures are fairly interesting in how",
                  "tight the curves are. You'll explore this more in the next task."]
    print((" ").join(sol_string))

    # data setup
    fuel_econ = pd.read_csv('../data/fuel_econ.csv')

    # plotting
    g = sb.PairGrid(data = fuel_econ, vars = ['displ', 'co2', 'city', 'highway', 'comb'])
    g.map_diag(plt.hist)
    g.map_offdiag(plt.scatter)


def additionalplot_solution_2():
    """
    Solution for Question 2 in additional plot practice: plot the relationship
    between engine size and emissions in terms of g/gal, for selected fuel
    types.
    """
    sol_string = ["Due to the high number of data points and their high amount of overlap,",
                  "I've chosen to plot the data in a faceted plot. You can see that engine",
                  "sizes are smaller for cars that use regular gasoline against those that",
                  "use premium gas. Most cars fall in an emissions band a bit below 9 kg CO2",
                  "per gallon; diesel cars are consistently higher, a little above 10 kg CO2",
                  "per gallon. This makes sense, since a gallon of gas gets burned no matter",
                  "how efficient the process. More strikingly, there's a smattering of points",
                  "with much smaller emissions. If you inspect these points more closely you'll",
                  "see that they represent hybrid cars that use battery energy in addition to",
                  "conventional fuel! To pull these mechanically out of the dataset requires",
                  "more data than that which was trimmed to create it - and additional research",
                  "to understand why these points don't fit the normal CO2 bands."]
    print((" ").join(sol_string))

    # data setup
    fuel_econ = pd.read_csv('../data/fuel_econ.csv')
    fuel_econ['co2_gal'] = fuel_econ['comb'] * fuel_econ['co2']
    fuel_econ_sub = fuel_econ.loc[fuel_econ['fuelType'].isin(['Premium Gasoline', 'Regular Gasoline', 'Diesel'])]

    # plotting
    g = sb.FacetGrid(data = fuel_econ_sub, col = 'fuelType', size = 4,
                     col_wrap = 3)
    g.map(sb.regplot, 'co2_gal', 'displ', y_jitter = 0.04, fit_reg = False,
          scatter_kws = {'alpha' : 1/5})
    g.set_ylabels('Engine displacement (l)')
    g.set_xlabels('CO2 (g/gal)')
    g.set_titles('{col_name}')