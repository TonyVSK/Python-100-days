# Folder 072: Understanding Data Exploration with Pandas

In this folder we don't have a specific project, the 100 days of code class is focused on learning some online tools to use python and ork with some modules, such as pandas.
So I decided to explain about it

## Google Colab Notebook

Also known as Google Colab, it is a free online tool in the cloud that allows us to write and run Python code through the browser. It is a very useful tool for developers and data scientists as it offers free access to high-performance computing resources. It is the tool we will use throughout the course.

### Join Colab

You will need to log in to Google Colab through Google Drive. There, go to New → More → Google Colaboratory.
When you open Google Colab, you will notice that the tool is divided into cells. To execute a cell: Shift + Enter

### Sending

With the csv file in this folder, move and drop it into the Google Colab sidebar to start working. So, with the file in our online repository, we need to import our module and read our file:
```bash
import pandas as pd
df = pd.read_csv('salários_por_faculdade_major.csv')
```

To see the first 5 lines of the file, just use the df.head() command


And that's it! Now we can manipulate our data online, with this tool.

## Contribution

Feel free to contribute anything I'm missing.