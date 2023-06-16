# RandomForestRegressor-PearsonCorrelationAnalysis
Random Forest Regressor (RandomForestRegressor) + Pearson's Correlation Coefficient Analysis: Using Python to analyze the correlation between specific elements of the periodic table

Combining Python machine learning and computational material science, we selected the "Random Forest Regressor" after comparing various machine learning models. We reduced 11 types of atomic properties to 6 important features through feature selection, and used these 6 important features to perform machine learning regression on an important material property (Segregation energy). This provides a practical case for analyzing the relationship between the properties of elements in the periodic table and material performance!

## How to Use

### Step 0: Explore important features in the data using the Random Forest Regressor in machine learning.
### (1) Transform the data of the (linear) model into a normal distribution
##### # The distribution of data "before" normalization
![image](https://user-images.githubusercontent.com/111637364/189491387-c191bff2-8be3-47a2-97eb-56bcf85fb223.png)

##### # The distribution of data "after" normalization
![image](https://user-images.githubusercontent.com/111637364/189491407-1965d4f3-d475-4d6d-b25d-431c476a8f51.png)

#### (2) Feature selection
##### # Considering Pairwise correlation: Eliminate data with too high mutual correlation, find features with higher correlation with each other through a clustermap.  
![image](https://user-images.githubusercontent.com/111637364/190912749-f704b325-a248-48f0-85b9-e1300709972c.png)

##### # Remove data with too high mutual correlation, reduce training time, and increase model interpretability.   
![image](https://user-images.githubusercontent.com/111637364/189534906-898b8002-7833-4781-b694-c699114d315d.png)

#### (3) Look at the correlation of each feature with the prediction target to find out the more important features.   
###### # Feature Importance & Feature Importance
![image](https://user-images.githubusercontent.com/111637364/190912801-d759dcc4-4084-4d13-b690-c107d7496aa3.png)

```
$ python Pearson_Correlations.py
```
### Step 1：Draw a kernel density estimation chart to help determine the distribution of data features.
![image](https://user-images.githubusercontent.com/111637364/188358075-2f956fe1-fe1e-4da6-a834-c20a34c09b70.png)

### Step 2：Based on the information obtained from the kernel density estimation chart, further carry out Pearson's correlation analysis to calculate the data correlation coefficient.
![image](https://user-images.githubusercontent.com/111637364/188369720-b1ef8227-b95b-4290-a940-de9e0ea582f0.png)

### Step 3：Select the elements you want to visualize and draw a periodic table heatmap. (Unfinished)
![image](https://user-images.githubusercontent.com/111637364/188358128-3a75d0a4-96de-453b-bba3-3cc92ad348d6.png)

