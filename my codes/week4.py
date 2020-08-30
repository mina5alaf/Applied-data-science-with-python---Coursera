import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

chi_squared_df2 = np.random.chisquare(2, size=10000)
stats.skew(chi_squared_df2)
chi_squared_df5 = np.random.chisquare(5, size=10000)
stats.skew(chi_squared_df5)
output = plt.hist([chi_squared_df2, chi_squared_df5], bins=50, histtype='step',
                  label=['2 degrees of freedom', '5 degrees of freedom'])
plt.legend(loc='upper right')
plt.show()

