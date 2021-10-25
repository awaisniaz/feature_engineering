# Transformation and Scaling of features

# 1.Normalization and Standardization
# 2. Scaling to Minimum and Maximum Values
# 3. Scaling to Median and Quantiles
# 4. Guassian Transformation
# 5. Logarithmic Transformation.
# 6. Reciprocal Transformation.
# 7. Square Root Transformation.
# 8. Exponential Transformation.
# 9. Box Cox Transformation.


# Standardization
# Z = (X-X_mean)/std

import pandas as pd
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df = pd.read_csv('train.csv',usecols=["Pclass",'Age','Fare','Survived'])
data_columns = df.columns
df_scaled = pd.DataFrame(scaler.fit_transform(df))
print(df_scaled.head(4))

# 30:00


# Min Max Scaling

#  Popularly use in cnn rnn
#  scale the value between 0 to 1
#  (X-Xmin)/(Xmax-Xmin)

from sklearn.preprocessing import MinMaxScaler
min_max = MinMaxScaler()
df_minmax = pd.DataFrame(min_max.fit_transform(df),columns=data_columns)
print(df_minmax.head(4))


# Robust Scaler
#  it is use to scale median and quantiles
#  x_scale = (X - Xmedian)/IQR

from sklearn.preprocessing import RobustScaler
r_scaler = RobustScaler()
df_robust = pd.DataFrame(r_scaler.fit_transform(df),columns=data_columns)
print(df_robust.head(4))


# Guassian Transformation

 # why we use this
 # for convert into normal distuributions

 # logarithm transformation
 # work well for right and left skewed data

 # reciprocal Transformation
 # SquarenRoot Transformation
 # Exponential Transformaton
 #  Boxcox transormation
