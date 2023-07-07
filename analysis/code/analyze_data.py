import pandas as pd
import numpy as np
from linearmodels import PanelOLS

### DEFINE
def main():
    df = import_data()
    fit = run_regression(df)
    formatted = format_model(fit)

    with open('output/regression.csv', 'w') as f:
        f.write('<tab:regression>' + '\n')
        formatted.to_csv(f, sep = '\t', index = False, header = False)

    # subset df to years greater than or equal to 1960
    df_subset = df.reset_index().copy()
    df_subset = df_subset[df_subset['year'] >= 1960]

    # fit new model, format
    fit_subset = run_regression(df_subset)
    formatted_subset = format_model(fit_subset)

    # write to file
    with open('output/regression_post1960.csv', 'w') as f:
        f.write('<tab:regression_post1960>' + '\n')
        formatted_subset.to_csv(f, sep = '\t', index = False, header = False)
    
   
    
def import_data():
    df = pd.read_csv('input/data_cleaned.csv')
    df['post_tv'] = df['year'] > df['year_tv_introduced']
    
    return(df)

def run_regression(df):
    df = df.set_index(['county_id', 'year'])
    model = PanelOLS.from_formula('chips_sold ~ 1 + post_tv + EntityEffects + TimeEffects', data = df)
    fit = model.fit()
    
    return(fit)
    
def format_model(fit):
    formatted = pd.DataFrame({'coef'     : fit.params, 
                              'std_error': fit.std_errors, 
                              'p_value'  : fit.pvalues})
    formatted = formatted.loc[['post_tv']]
    
    return(formatted)
    
### EXECUTE
main()