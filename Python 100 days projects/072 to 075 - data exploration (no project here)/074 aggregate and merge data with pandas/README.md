# First steps

At this README file, you will see how to answer de 074 challenge.
As you imagine, we should import pandas to start our data analysis

```bash
import pandas as pd
```

## Exploring the LEGO Brick Colours

to see the first 5 rows, we can open the csv and use head() function:
```bash
colors = pd.read_csv('data/colors.csv')
colors.head()
```

To find the number of unique colours, it's necessary to check if every entry is unique:
```bash
colors['name'].nunique()
```

The result should be equal to 135.

## Find the number of transparent colours

To find it, we can combine the groupby() function with .count() function:
```bash
colors.is_trans.value_counts()
```

(to find the number of transparent colours where is trans == 't' versus the number of opaque colours where is_trans == 'f', we could do something like this:
```bash
colors.groupby('is_trans').count()
```
The output should be:
f 107
t 28
)

The rest of the csv file contains more challenges, these at this README are just the first steps, if you want to continue, go ahead, you already know the way, it's a good exercise to practice data analysis.