# tj_locations
## Overview
The aim of this data science project is to analyze factors that might play a role in determining the number of Trader Joe's locations in a county in California. The project was inspired by a tweet I saw on Twitter alleging that Trader Joe's tend to open stores in richer neighborhoods. The allegation was not the first of its kind and, after searching the web, I found an article (https://nextcity.org/daily/entry/infographic-why-isnt-trader-joes-moving-into-underserved-neighborhoods) that mentions that TJ's "continues to open shop in ZIP codes with above average median incomes and very small percentages of households on SNAP."

To further explore the possibile relationship between the number of stores and the median income in a neighborhood, I focused on California and pulled data on median household income for each county, county land area, population, and other census statistics from various sources, and conducted linear regression and Poisson regression to examine the statistical significance of each of the features, and finally ran a random forest to predict the number of TJ's stores in a given county.
## Webscraping
Selenium and Python were used to extract the number of Trader Joe's stores in each of the cities in California from the Trader Joe's website, as well as county median household income from IndexMundi.
## Selected Graphs
![Median Household Income by County](Screen%20Shot%202020-05-22%20at%209.16.05%20PM.png)
![Total Population vs Number of Stores](Screen%20Shot%202020-05-22%20at%209.16.53%20PM.png)
![Median Household Income vs Number of Stores](Screen%20Shot%202020-05-22%20at%209.17.57%20PM.png)
![Heatmap for All Features](Screen%20Shot%202020-05-22%20at%209.18.18%20PM.png)
![Counties with Most Stores](Screen%20Shot%202020-05-22%20at%209.18.35%20PM.png)

### Key findings:
## Linear Regression
- Population is the most significant factor contributing to the number of stores in a county, with a Pearson corelation (Pearson's r) of 0.961518. In particular, LA county has both the largest population and the most Trader Joes' stores.
- Household is also highly correlated with number of stores with a correlation of 0.961889. This makes sense since population and household are positively correlated.
- Surprisingly, population density does not have a strong correlation with the number of stores in a county, with a correlation of only 0.11786. This may have to do with the fact that population density is calculated by dividing population over total land area, where especially in this case a large proportion of the land can be undeveloped and thus remote. So, the population density could be misrepresenting the true density __experienced by the people__.
- Some other factors such as single detached/attached homes and mobile homes also have high positive correlations so they can be ignored for the sake of multicollinearity.

## Limitations

## Data Sources
Census data: http://www.dof.ca.gov/Forecasting/Demographics/Estimates/e-5/

Trader Joe's Store Locations: https://locations.traderjoes.com/ca/

US Demographic: https://www.census.gov/geographies/reference-files/2018/demo/popest/2018-fips.html (2018 State, County, Minor Civil Division, and Incorporated Place FIPS Codes)

City Land Areas: https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_California

County Land Areas: https://en.wikipedia.org/wiki/List_of_counties_in_California

County FIPS: https://www.weather.gov/hnx/cafips

County Median Household Income: https://www.indexmundi.com/facts/united-states/quick-facts/california/median-household-income#table

## Resources
Linear Regression: https://towardsdatascience.com/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn-83a8f7ae2b4f
