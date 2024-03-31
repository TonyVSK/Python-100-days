# Folder 072 and 073: Understanding Data Exploration With Pandas

In these folders, we don't have a specific project. The "100 Days of Code" class focuses on learning online tools for using Python and working with modules, such as Pandas. Thus, I've decided to explain about it.

## Google Colab Notebook

Also known as Google Colab, this is a free online tool hosted in the cloud that enables us to write and execute Python code through a browser. It's an invaluable resource for developers and data scientists, offering free access to high-performance computing resources. It will be our primary tool throughout the course.

### Join Colab

To use Google Colab, you'll need to log into it via Google Drive. Navigate to New → More → Google Colaboratory.
Upon opening Google Colab, you'll notice that the interface is divided into cells. To execute a cell, press Shift + Enter.

### Sending

To begin working with your data, drag and drop the csv file into the Google Colab sidebar. Once the file is in our online repository, we need to import our module and read our file:
```bash
import pandas as pd
df = pd.read_csv('salários_por_faculdade_major.csv')
```

To view the first 5 lines of the file, simply use the command df.head().

This setup allows us to manipulate our data online using this powerful tool.

The course suggests using 2 csv files for data analysis: one for Day 072 (salaries_by_college_major.csv) and another for Day 073 (QueryResults.csv).




## Folder 074

This folder contains the materials for Day 074, focusing on a dataset about LEGO. The objective is to learn how to extract information regarding, for example, the history of LEGO, product offerings, etc.

### Idea - what to learn with 074
* How to combine a Notebook with HTML Markup.

* Apply Python List slicing techniques to Pandas DataFrames.

* How to aggregate data using the .agg() function.

* How to create scatter plots, bar charts, and line charts with two axes in Matplotlib.

* Understand database schemas that are organised by primary and foreign keys.

* How to merge DataFrames that share a common key


## Folder 075

This folder encompasses the materials for Day 075, combining Google Trends with other time series data. Google Trends allows us to access data on the popularity of Google searches. This lesson will explore how to analyze trends, such as how the search volume for "bitcoin" relates to the price of bitcoin.

### Idea - what to learn with 075
* How to make time-series data comparable by resampling and converting to the same periodicity (e.g., from daily data to monthly data).

* Fine-tuning the styling of Matplotlib charts by using limits, labels, linestyles, markers, colours, and the chart's resolution.

* Using grids to help visually identify seasonality in a time series.

* Finding the number of missing and NaN values and how to locate NaN values in a DataFrame.

* How to work with Locators to better style the time axis on a chart

* Review the concepts learned in the previous three days and apply them to new datasets


## Contribution

Feel free to contribute anything I'm missing.