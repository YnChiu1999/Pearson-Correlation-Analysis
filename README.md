# Pearson-Correlation-Analysis
隨機森林(RandomForestRegressor) + 皮爾森積動差相關係數分析：利用Python分析週期表元素特定間的相關性

結合Python機器學習及計算材料科學，提供分析週期表元素特性與材料性能分析的實作案例。

## 使用方式

### Step 0：透過機器學習中的隨機森林(RandomForestRegressor)回歸器，探討數據中的重要特徵。
### (1) 將(線性)模型的數據轉化為正態分佈
##### # 正態化之前的數據分布
![image](https://user-images.githubusercontent.com/111637364/189491387-c191bff2-8be3-47a2-97eb-56bcf85fb223.png)

##### # 正態化之後的數據分布
![image](https://user-images.githubusercontent.com/111637364/189491407-1965d4f3-d475-4d6d-b25d-431c476a8f51.png)

#### (2) 查看各特徵與預測目標的相關性，找出其中較重要的特徵。
###### # 特徵重要性(Feature Importance) & 特徵置換重要性(Feature Importance)
![image](https://user-images.githubusercontent.com/111637364/189491654-6fbd1db2-4415-4b94-b331-4ab56dc53bd0.png)

```
$ python Pearson_Correlations.py
```
### Step 1：繪製核密度估計圖（kernel density estimation)，幫助判斷數據特徵分布。
![image](https://user-images.githubusercontent.com/111637364/188358075-2f956fe1-fe1e-4da6-a834-c20a34c09b70.png)

### Step 2：針對由核密度估計圖（kernel density estimation)取得的資訊，進一步進行皮爾森積動差相關係數分析，計算出數據相關性係數。
![image](https://user-images.githubusercontent.com/111637364/188369720-b1ef8227-b95b-4290-a940-de9e0ea582f0.png)

### Step 3：選取想要視覺化的元素，繪製週期表熱力圖(heatmap)。
![image](https://user-images.githubusercontent.com/111637364/188358128-3a75d0a4-96de-453b-bba3-3cc92ad348d6.png)
