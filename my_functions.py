import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from matplotlib import pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import Lasso
from sklearn import preprocessing
from scipy.interpolate import make_interp_spline
from sklearn.metrics import mean_absolute_error

# This function adds up Chromosome properties to deal with strains with multiple extra-chromosome
def Chr_to_disomes(RG, Chr_feat, column_name):
    orf = []
    for ind, row in RG.iterrows():
        dis = ind.split(';')
        genes = 0
        for d in dis:
            genes += Chr_feat._get_value(int(d), column_name)
        orf.append(genes)
    RG[column_name] = orf
    return RG

# function to get the p-values of the model and of feature
def ols_pval(RG, features, yf):
    X = RG[features]
    y = RG[yf]
    # standardization of dependent variables (sklearn)
    scaler = preprocessing.MinMaxScaler()
    scaler.fit(X)
    X_s = scaler.transform(X)
    X_s = sm.add_constant(X_s)
    linreg = sm.OLS(y, X_s)
    res = linreg.fit()
    print(res.summary())
    var = ['const'] + features
    for x in range(len(var)):
        print(var[x] + ' p(t): ' + str(res.pvalues[x]))
    return res

# Function to plot data and fit the linear regression
# Print the plot and the R2 score.
# Arguments are: Dataframe outputed by combineRG_Moby, cx: title of column for the x axis
# cy: title of coulum to use for y axis
def Fitlin(RG, cx, cy, std=False, filenamesvg=None, labels=True, alpha=1):
    X = list(RG[cx])
    y = list(RG[cy])
    n = list(RG.index)

    fig, axs = plt.subplots(ncols=2, figsize=(15, 5))
    sns.regplot(x=cx, y=cy, data=RG, label=RG.index, truncate=False, ax=axs[0], scatter_kws={'alpha': alpha},
                color='black')
    if std:
        axs[0].errorbar(X, y, yerr=list(RG[std]), fmt='none', zorder=1, color='black')
    if labels:
        for i in range(len(n)):
            axs[0].text(X[i] + 10, y[i] + 1, n[i], horizontalalignment='center', color='black', weight='light')

    X = sm.add_constant(X)
    results = sm.OLS(y, X).fit()
    y_pred = results.predict(X)
    y_p_np = np.array(y_pred)
    y_np = np.array(y)
    residuals = np.subtract(y_np, y_p_np)
    residuals = list(residuals)
    sns.scatterplot(x=y_pred, y=residuals, ax=axs[1], s=60, alpha=alpha, color='black')
    sns.set_style("whitegrid", {'axes.grid': False})
    if labels:
        for i in range(len(n)):
            axs[1].text(y_pred[i] + 1, residuals[i] + 1, n[i], horizontalalignment='center', color='black',
                        weight='light')
    axs[1].axhline(0, color='black')
    axs[1].set(xlabel="Fitted values", ylabel="Residuals")

    if filenamesvg != None:
        plt.savefig(filenamesvg, bbox_inches='tight')
    print('Parameters: ', results.params)
    print('R2: ', results.rsquared)
    print('Adjusted R2: ', results.rsquared_adj)
    print('F p-value: ', results.f_pvalue)

    return results