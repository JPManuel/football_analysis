# Football Analysis

A collection of personal football data analytics work in progress. Some example plots can be found in the *example_plots* directory. Most of these plots use a custom *matplotlib* style.

Two main data sources are used throughout these anaylses:
- StatsBomb [open-data](https://statsbomb.com/academy/)
- [FBref](https://fbref.com/en/) with advanced statistics provided by StatsBomb.

## modules
The *modules* directory contains two scripts:

**importing_sb.py** - Contains functions for importing and handling the StatsBomb free data.

For example:

`get_shot` - Extracts all the shots to a *pandas* `DataFrame` keeping the data relevant for analysis.

`shot_map_player` - Creates an xG shot map for a specified player. Can plot xG as colour or size of marker.


**draw_pitch.py** - Contains a function for plotting a football pitch.

## data_overview_liverpool.ipynb

A notebook performing a data overview of Liverpool FC using FBref data, producing the *data_overview_liverpool.png* image seen in *example_plots*. The idea was to produce a single image that can give the viewer an idea of the way Liverpool FC play and who are the most involved players.

## messi_career.ipynb

A broad look at Messi's career using simple stats and metrics, with free data from StatsBomb. Includes shot numbers, conversion rates, types, etc. 
Passes into final third and box and types (through ball, cross, switch).
Progressive carries: Success, ending event, contribution to overall attacking contribution.
How Messi has been used: Starting position.

## nmf.ipynb

Using Non-negative Matrix Factorisation to investigate spatial shooting, passing and progressive carry tendencies in the WSL 18/19 season using StatsBomb free data, with the eventual aim of finding players who fulfil similar roles.

## pass_clustering.ipynb

Using k-means clustering to identify different types of passes. Firstly, this is used to look at the most common passes played by Messi in the 18/19 season. Secondly, this is applied to the whole WSL 18/19 season from which players who play a certain type of pass can be identified.

## pass_sonar.ipynb

Incomplete code for creating team passing sonars (or radars), displaying pass direction tendencies and typical pass length.

## poisson_prediction.ipynb

Exploring the use of the Poisson distribution to predict football matches. Applied to simple scoring data from the 16/17 Premier League season, the model quantifies an offensive and defensive strength to each team as well as a league average home advantage.

## post_match_probs.ipynb

Using the process of random simulation (Monte-Carlo) to describe the probabilties of different scorelines and results for matches based off the xG of shots.

## xG_model.ipynb

A notebook exploring the process of creating an xG model, analysing features and resulting model performance.
