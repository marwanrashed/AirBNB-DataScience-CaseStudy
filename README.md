# AirBNB-DataScience-CaseStudy

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

You will need the standard data science libraries found in the Anaconda distribution of Python.  The code should run with no issues using Python versions 3.*.  

You will also want to download [nltk](https://www.nltk.org/data.html) - directions for this can be found in the text processing portion of the workbook.

## Project Motivation<a name="motivation"></a>

For this project, I was interestested in analyzing data from AirBnB homes located in Boston.  Specifically, I looked at the following questions:

1. What is the price average for the listed neighbourhoods indvidually ? Which neighbourhood has the maximum/minuimum price ?
1. Does the neighbourhood affects the listing price ?
1. Does the price fluctuates based on the month/ season of the year ? 
1. Do hosts with various/single listings tend to stabilize prices or change them frequently ?
1. What impact do the host attributes (superhost, acceptance rate, ..., etc) have on the price ?
1. What is the relationship between the property attributes and the price ?   


## File Descriptions <a name="files"></a>

The following are the files available in this repository:

* `AirBNB_Exploratory_Data_Analysis.ipynb` - a notebook of the analysis performed following the CRISP-DM process.

* `BostonCalendar.csv` - csvs containing **home_id**, **date**, **availability**, and **price** for each home. ***Unused***

* `BostonListings.csv` - The main file of interest. It contains 96 features about the listings, which cover the price, host attributes, property attributes, date/time, neighbourhoods, and more unused features in the analysis. 

* `BostonReviews.csv` - csvs containing the **home_id**, **date** of review, **reviewer_id**, **reviewer_name**, and reviewer **comments** for the reviewed stays. ***Unused***

It is worth noting here that the reviews and calendar files did not have overlapping dates, and there were no numeric values associated with reviews.

## Results<a name="results"></a>

The results are presented and dicussed in the following link [blog post available here]().

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to AirBnB and Kaggle for the data.  You can find the Licensing for the data and other descriptive information for the [Boston data on Kaggle](https://www.kaggle.com/airbnb/boston) and for the [Seattle data](https://www.kaggle.com/airbnb/seattle).
