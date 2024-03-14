# Final Assignment

In this project we will predict if the Falcon 9 first stage will land successfully or
not. Much of the savings of Spacex is because of reusing first stage. If we are
able to determine this, we will be able to predict the cost of launch, for an
alternate company.

Some of the questions that need to be answered include which launch site, orbit
has more successes? How success is impacted by payload mass, booster
version? How does flight number affect success?

## Prerequisites and tools used
Pandas  
Numpy  
BeautifulSoup  
SQLAlchemy
Seaborn  
Matplotlib  
Folium  
Dash  
Plotly  
Sklearn  


## Steps involved
### Data collection methodology:
Using Spacex Api data of past launches were collected and relevant subsequent api calls were made. Data was cleaned and filtered for Falcon 9 launches.
Also web scraped Wiki page of the Falcon 9 launches and cleaned the data.
### Perform data wrangling
The various types of landing outcomes were classified into success or failure and added as a field to the dat
### Perform exploratory data analysis (EDA) using visualization and SQL
### Perform interactive visual analytics using Folium and Plotly Dash
### Perform predictive analysis using classification models
LogisticRegression, SVCClassifier, DecisionTreeClassifer and KNeigborClassifier models were used to train and test the data. GridSearchCV was used for hyper-parameter tuning. All were performing equally well on test data.


## Findings and results
Launch successes have increased, as flight number increases, which may be due to learnings in earlier launches.   
High payloads (above 10000kg) have high success/failure ratio  
ES L1, HEO, GEO and SSO orbits have all successes. The number of launches in them are not high, and payloads are below 6000 kg.  
The launch sites tend to be near coastline and modes of transportation and far away from city.  
Booster version FT has more success/failure ratio, in the 1000-9000 kg payload mass range, with some number of launches.  
B5 booster version is used for high payloads.  




