import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats.stats import pearsonr
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from statsmodels.stats.outliers_influence import summary_table

# plt.style.context(['science', 'ieee','no-latex']) use it if you get science-plot installed

n = 100

x = np.linspace(0, 10, n)
e = np.random.normal(size=n)
y = 1 + 0.5*x + 2*e
gamma, pvalue = pearsonr(x,y)
X = sm.add_constant(x)

re = sm.OLS(y, X).fit()
print(re.summary())

prstd, iv_l, iv_u = wls_prediction_std(re)

st, data, ss2 = summary_table(re, alpha=0.05)

fittedvalues = data[:, 2]
predict_mean_se  = data[:, 3]
predict_mean_ci_low, predict_mean_ci_upp = data[:, 4:6].T
predict_ci_low, predict_ci_upp = data[:, 6:8].T

# Check we got the right things
print(np.max(np.abs(re.fittedvalues - fittedvalues)))
print(np.max(np.abs(iv_l - predict_ci_low)))
print(np.max(np.abs(iv_u - predict_ci_upp)))


plt.scatter(x, y, label='data', alpha=.4)
plt.plot(x, fittedvalues, '-', label='fit')
plt.plot(x, predict_ci_low, 'r--',label='95% prediction limit')
plt.plot(x, predict_ci_upp, 'r--')
plt.plot(x, predict_mean_ci_low, 'b--',lw=.5,label=f'95% ci')
plt.plot(x, predict_mean_ci_upp, 'b--',lw=.5)
plt.title(fr'''scatter plot with x vs y 
$\gamma = $ {gamma:.2f}''')
plt.legend()
plt.tight_layout()
plt.show()