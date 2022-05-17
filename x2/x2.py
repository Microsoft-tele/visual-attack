from  scipy.stats import chi2_contingency
import numpy as np
import pandas as pd
data=[[25,21,10],[82,88,30],[223,16,5]]

df=pd.DataFrame(data,index=['美式咖啡','拿铁咖啡','卡布奇诺'],columns=['IT','行政','工程'])
kt=chi2_contingency(df)

print('卡方值=%.4f, p值=%.4f, 自由度=%i expected_frep=%s'%kt)