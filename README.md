# statsbomb_data

A collection of work in progress looking at the freely available Statsbomb open-data.

## importing_sb.py

This python script contains a number of functions for importing and sorting the Statsbomb data, pitch drawing and 
creating xG shot maps and pass maps.

For example:

`shot_map_player` - Creates an xG shot map for a specified player. Can plot xG as colour or size of marker.

`pass_map_player` - Creates a pass map for a specified player, with shot and goal assists highlighted.

## xG_model.ipynb

A notebook detailing the process of creating an xG model (using all the La Liga data) using logistic regression.

## messi_career.ipynb

A notebook that looks at simple stats and metrics across Messi's career. Includes shot numbers, conversion rates, types, etc. 
Passes into final third and box and types (through ball, cross, switch).

## pass_sonar.ipynb

Incomplete code for creating team passing sonars.
