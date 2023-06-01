# Script - EGM722 Assignment

## Intro
This script analyses and classifies different environmental and social status indicators to assess questions in relation to the topic of environmental justice within the city of Hamburg, Germany.
The four core indicators are: Social Status, Green Area Supply, Thermal Burden and Noise Pollution. Level of spatial analysis are districts for the City of Hamburg. The script first calculates and classifies statistics in relation to each individual indicator to explore the spatial distribution between the districts. In a second step, the individual indicators are combined to assess the relation between social status and environmental conditions.
The script creates maps and plots (available in the "output" folder) to visualize the results of the analysis. A How-to Guide is equally made available in the repository

## Installation / Set-Up
The code and all relevant files can be accessed in the GitHub repository available at: https://github.com/CharlotteGIS/egm722_project). The repository contains a Jupyter Notebook with the code. 
The data files used in the script are available in the “data” folder on GitHub. The maps and output is made available in the folder “output” on GitHub.

The steps to get started and run the code are: 
	1) Fork the repository. To fork the repository click onf the 'Fork' button at the top right corner of the screen. 
	2) Clone the repository to create a local version on your computer.
	3)Conda environment: To use the script, it is recommended to install conda and to set up a dedicated project environment. 
  4) Install required packages and dependencies: To recreate the project environment and automatically install all the required packages and dependencies import the environment.yml file. Make sure to change the name provided in the yml file to the name of your environment.

The required packages and dependencies used are: 
•	Python
•	Geopandas 
•	Cartopy>=0.21
•	Notebook
•	Folium
•	Raterio
•	Pyepsg

The code has been designed using Jupyter Notebook. To run the code the set up of an Integrated Development Environment (IDE) such as PyCharm is not required.



## RUN THE CODE
The code can be executed using the data files available in the data folder using Jupyter Notebook. 

For the noise data: Unzip the file: "Lärmkarten" available on your local drive to read the data.

*Please note that the use of data files, different from the files provided requires updating of the naming conventions in the script.  

Head over to the "output folder" to see the maps created by the code

##Troubleshooting
The script loads csv files. Issues with reading the csv files might arise when a different setting is used for the "separators" in excel. Update the code specifying the delimiter used for reading
the files when loading the data. Head to the How-to Guide for furher instructions.
