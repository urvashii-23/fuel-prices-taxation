# Global Fuel Prices and Taxation Trends

## Objective
This project studies global fuel prices and taxation trends using public data.

## Questions
1. How different are petrol prices in different countries?
2. How much of the petrol price is tax?
3. How did governments change taxes when oil prices went up in 2026?

## Data
Fuel prices for EU countries, 12 October 2026. Source: fuel-prices.eu, which publishes the European Commission Weekly Oil Bulletin.

## Method
I saved the data as a CSV file and used Python (pandas and matplotlib) to read it and draw a bar chart of petrol prices.

## Result
Malta has the cheapest petrol at 1.340 euro per litre and Denmark the most expensive at 2.658 euro per litre. The EU average is 2.010 euro per litre.

## How to run
pip install pandas matplotlib
python src/analysis.py

## Limits
This is a small snapshot from one date, so it shows prices only, not trends over time.

## Next steps
Add more countries, tax share data and price history.