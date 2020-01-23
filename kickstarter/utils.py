# Source: https://www.kaggle.com/kabure/kickstarter-projects-eda-stat-tests-pipeline
import pandas as pd
from scipy import stats

def resumetable(df):
    print(f"Dataset Shape: {df.shape}")
    summary = pd.DataFrame(df.dtypes,columns=['dtypes'])
    summary = summary.reset_index()
    summary['Name'] = summary['index']
    summary = summary[['Name','dtypes']]
    summary['Missing'] = df.isnull().sum().values    
    summary['Uniques'] = df.nunique().values
    summary['First Value'] = df.loc[0].values
    summary['Second Value'] = df.loc[1].values
    summary['Third Value'] = df.loc[2].values

    for name in summary['Name'].value_counts().index:
        summary.loc[summary['Name'] == name, 'Entropy'] = round(stats.entropy(df[name].value_counts(normalize=True), base=2),2) 

    return summary

def chi2_test(col, prob=.95):
    stat, p, dof, expected = stats.chi2_contingency((pd.crosstab(df_kick[col[0]], 
                                                                 df_kick[col[1]]
                                                                )))
    print("CHI-SQUARED TEST: ")
    # calculating the value to compare with chi2 statistic
    critical = stats.chi2.ppf(prob, dof)
    print(f'dof={dof}, probability={round(prob,3)}, critical={round(critical,5)}, stat={round(stat,5)}')
    print("Accept or Reject H0: ")
    # interpret test statistic
    if abs(stat) >= critical:
        print('Dependent (reject H0)')
    else:
        print('Independent (fail to reject H0)')

def ttest_onesided(cols, alpha = 0.05):
    """
    
    cols: list with the , we will test the mean of the population and the sample mean
    
    H0:
    The null Hypothesis is that the both distributions are the same
    H1:
    The alternative hypothesis is that the distributions are different
    
    """
    pop_mean = cols[0].mean()
    sample = cols[1]
    
    print(f"Mean of Population: {pop_mean} \nMean of Sample: {sample.mean()}")
    ttest_val, pval = stats.ttest_1samp(sample, pop_mean)

    print(f"t-test value: {ttest_val}")
    print("Comparing p_value by...\n")
    print(f'p-value result: {pval}')
    if pval < alpha:    # alpha value is 0.05 or 5%
        print(" we are rejecting null hypothesis")
    else:
        print("we are accepting null hypothesis")

def ttest_twosided(cols, alpha = 0.05):
    sample1 = cols[0]
    sample2 = cols[1]
    print(f"Mean of Sample 1: {sample1.mean()} \nMean of Sample 2: {sample2.mean()}")    
    ttest_val, pval = stats.ttest_ind(sample1, sample2)

    print(f"t-test value: {ttest_val}")
    # print("Comparing p_value by...\n")
    print(f'p-value result: {pval}')
    if pval < alpha:    # alpha value is 0.05 or 5%
        print(" we are rejecting null hypothesis")
    else:
        print("we are accepting null hypothesis")