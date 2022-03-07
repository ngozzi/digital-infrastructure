import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import numpy as np
import pandas as pd
import seaborn as sns


def multicollinearity_diagnosis(ax, df, country, mapper):
    """
    This function performs the multicollinearity analysis
    :param ax: axis
    :param df: df of dependent/independet variables
    :param country: name of the country
    :param mapper: dict used to rename features (for plotting purposes)
    """
    
    df_r = df.copy()
    df_r = df_r.rename(columns=mapper)

    # compute vif
    X = sm.add_constant(df_r[mapper.values()])
    vif = pd.DataFrame()
    vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    vif["features"] = X.columns
    print(country)
    print(vif)

    # plot correlation matrix
    corr = df_r[mapper.values()].corr()
    mask = np.triu(np.ones_like(corr))
    corr_lt = corr.where(np.tril(np.ones(corr.shape)).astype(np.bool))
    sns.heatmap(corr_lt, xticklabels=df_r[mapper.values()].columns, yticklabels=df_r[mapper.values()].columns, annot=True,
                cmap=sns.diverging_palette(500, 10, as_cmap=True), mask=mask, linewidths=1, center=0, ax=ax, vmin=-1, vmax=1, fmt=".2f")
    ax.set_title(country, weight='bold')
    ax.tick_params(axis="x", rotation=90)