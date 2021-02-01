# Surfs Up

## Overview of the statistical analysis:

The project is to perform climate analysis to find out the temperature trends before openning a surf shop and identify a surf and ice cream shop business year around sustainable or not in the weather conditions and provide recommendations. We performed a analysis of  Precipitation Summary , Weather Station Analysis and temperature in the stations. W.Avy  wants more information about temperature trends before opening the surf shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round. 

## Results:
* [Precipitation Analysis]()

* [Weather Station Analysis]()

* [Temperature Analysis]()

*  **Summary Statistics for June :** 
 * By using Python, Pandas functions and methods, and SQLAlchemy, A working query is written to retrieve the June temperatures from the date column of the Measurement table in hawaii.sqlite. 
 * The temperatures are added to a list "results".
 * The list of temperatures is converted to a Pandas DataFrame.
 * [June Summary statistics]() are generated for the DataFrame.
 
 * **Summary Statistics for December :**
 * By using Python, Pandas functions and methods, and SQLAlchemy, A working query is written to retrieve the June temperatures from the date column of the Measurement table in hawaii.sqlite. 
 * The temperatures are added to a list "results".
 * The list of temperatures is converted to a Pandas DataFrame.
 * [June Summary statistics]() are generated for the DataFrame.

## Summary:
* With the given data provided and based on the data analysis, we can state as a high-level summary of results that 
  * The count is 1700 in June and 1517 in Decemeber , resulting decrease in December and an oppurtunity to improve in the winter time.
 
  * Standard deviation is 3.25 in June and 3.75 in December, making a 0.5 difference between both seasons.
 
  * The table below povides the temperature values helps to determine the profitability of opening a surf and ice cream shop all year round.

    Statistics | June (F) | December (F)
    | :--- | ---: | :---:
    Minimum Value  | 64.0 | 56.0
    Maximum Value  | 85.0 | 83.0
    Average Value  | 74.9 | 71.0

* In addition, current data provide attributes such as precipitation and weather station and temperatures in statios performing weather data for June and December that helps results to decide on how would improve to build the shop and ideas to develop areas would make this location visitor attractive to elevate a successful business.
