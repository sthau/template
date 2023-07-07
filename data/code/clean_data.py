import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### DEFINE
def main():
    # read data
    df = pd.read_csv('output/data_merged.csv')

    # clean data
    df = clean_data(df)

    # run plot
    plot_data(df)

    # save data
    df.to_csv('output/data_cleaned.csv', index = False)

def plot_data(df):
    # plot histogram of chips_sold variable as percentages
    plt.hist(df['chips_sold'], weights = np.zeros_like(df['chips_sold']) + 1. / df['chips_sold'].size)

    # add x axis label of chips_sold, y axis of percentage
    plt.xlabel('chips_sold')
    plt.ylabel('percentage')

    # save plot to output folder
    plt.savefig('output/chips_sold.pdf')

def clean_data(df):
    # remove rows with missing indicator
    df['chips_sold'][df['chips_sold'] == -999999] = np.NaN
    return(df)
    
### EXECUTE
main()
