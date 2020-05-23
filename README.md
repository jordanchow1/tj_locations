# tj_locations
## Overview
The aim of this data science project is to analyze factors that might play a role in determining the number of Trader Joe's locations in a county in California. The project was inspired by a tweet I saw on Twitter alleging that Trader Joe's tend to open stores in richer neighborhoods. The allegation was not the first of its kind and, after searching the web, I found an article (https://nextcity.org/daily/entry/infographic-why-isnt-trader-joes-moving-into-underserved-neighborhoods) that mentions that TJ's "continues to open shop in ZIP codes with above average median incomes and very small percentages of households on SNAP."

To further explore the possibile relationship between the number of stores and the median income in a neighborhood, I focused on California and pulled data on median household income for each county, county land area, population, and other census statistics from various sources, and conducted linear regression and Poisson regression to examine the statistical significance of each of the features, and finally ran a random forest to predict the number of TJ's stores in a given county.

## Summary


## Limitations

### Data Sources
Census data: http://www.dof.ca.gov/Forecasting/Demographics/Estimates/e-5/

Trader Joe's Store Locations: https://locations.traderjoes.com/ca/

US Demographic: https://www.census.gov/geographies/reference-files/2018/demo/popest/2018-fips.html (2018 State, County, Minor Civil Division, and Incorporated Place FIPS Codes)

City Land Areas: https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_California

County Land Areas: https://en.wikipedia.org/wiki/List_of_counties_in_California

County FIPS: https://www.weather.gov/hnx/cafips

County Median Household Income: https://www.indexmundi.com/facts/united-states/quick-facts/california/median-household-income#table

### Resources
Linear Regression: https://towardsdatascience.com/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn-83a8f7ae2b4f
