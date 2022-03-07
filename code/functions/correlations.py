from scipy.stats import pearsonr
import pandas as pd
import numpy as np
import pingouin as pg
import scipy.stats


def pearsonr_CI(x, y, alpha=0.05):
    """
    This function computes the confidence interval for a Pearson coefficient
    # credit to:
    # https://shandou.medium.com/how-to-compute-confidence-interval-for-pearsons-r-a-brief-guide-951445b9cb2d
    :param x: first array
    :param y: second array
    :param alpha: significance (default=0.05)
    :return: correlation and CI
    """
    # compute pearson coeff
    r, p = pearsonr(x, y)

    # sample size
    n = len(x)
    
    # compute z-critical
    alpha = alpha / 2 # Two-tail test
    z_critical = scipy.stats.norm.ppf(1 - alpha)
    
    # tranform z
    z_prime = 0.5 * np.log((1 + r) / (1 - r))
    
    # sample standard error
    se = 1 / np.sqrt(n - 3) 
    
    # compute XI
    CI_lower = z_prime - z_critical * se
    CI_upper = z_prime + z_critical * se
    
    return r, np.tanh(CI_lower), np.tanh(CI_upper)



def partial_corr(x, y, cov, method='pearson'):
    """
    This function computes the partial correlation between two arrays
    :param x: first array
    :param y: second array
    :param cov: control variables (must be a list of lists)
    :param method: correlation method (default: pearson)
    :return: correlation and CI
    """
    df = pd.DataFrame(data={"x": x, "y": y})
    
    cov_cols = []
    for i in range(len(cov)):
        df['cov' + str(i)] = cov[i]
        cov_cols.append('cov' + str(i))
        
    df_notnull = df.loc[np.all(df[['x', 'y'] + cov_cols].notnull(), axis=1)]
    pcorr = pg.partial_corr(data=df_notnull, x="x", y='y', covar=cov_cols, method=method)
    return pcorr['r'].values[0], pcorr['CI95%'].values[0][0], pcorr['CI95%'].values[0][1]

