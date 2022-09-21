# RandomForestRegressor-PearsonCorrelationAnalysis
隨機森林(RandomForestRegressor) + 皮爾森積動差相關係數分析：利用Python分析週期表元素特定間的相關性

結合Python機器學習及計算材料科學，比較多種機器學習模型後選定"隨機森林回歸器(RandomForestRegressor)"將11種原子特性透過特徵選取降維至6個重要特性，將此6種重要特徵對材料重要特性(Segregation energy)作機器學習回歸，提供分析週期表元素特性與材料性能分析的實作案例。

## 使用方式

### Step 0：透過機器學習中的隨機森林回歸器(RandomForestRegressor)，探討數據中的重要特徵。
### (1) 將(線性)模型的數據轉化為正態分佈
##### # 正態化之前的數據分布
![image](https://user-images.githubusercontent.com/111637364/189491387-c191bff2-8be3-47a2-97eb-56bcf85fb223.png)

##### # 正態化之後的數據分布
![image](https://user-images.githubusercontent.com/111637364/189491407-1965d4f3-d475-4d6d-b25d-431c476a8f51.png)

#### (2) 特徵選擇(Feature selection)
##### # 考慮Pairwise correlation:將相互關聯性太高的數據屏除，透過clustermap找出彼此相關性較高的特徵   
![image](https://user-images.githubusercontent.com/111637364/190912749-f704b325-a248-48f0-85b9-e1300709972c.png)

##### # 將相互關聯性太高的數據去除，減少訓練時間，提升模型可解釋性   
![image](https://user-images.githubusercontent.com/111637364/189534906-898b8002-7833-4781-b694-c699114d315d.png)

#### (3) 查看各特徵與預測目標的相關性，找出其中較重要的特徵。   
###### # 特徵重要性(Feature Importance) & 特徵置換重要性(Feature Importance)
![image](https://user-images.githubusercontent.com/111637364/190912801-d759dcc4-4084-4d13-b690-c107d7496aa3.png)

```
$ python Pearson_Correlations.py
```
### Step 1：繪製核密度估計圖（kernel density estimation)，幫助判斷數據特徵分布。
![image](https://user-images.githubusercontent.com/111637364/188358075-2f956fe1-fe1e-4da6-a834-c20a34c09b70.png)

### Step 2：針對由核密度估計圖（kernel density estimation)取得的資訊，進一步進行皮爾森積動差相關係數分析，計算出數據相關性係數。
![image](https://user-images.githubusercontent.com/111637364/188369720-b1ef8227-b95b-4290-a940-de9e0ea582f0.png)

### Step 3：選取想要視覺化的元素，繪製週期表熱力圖(heatmap)。
![image](https://user-images.githubusercontent.com/111637364/188358128-3a75d0a4-96de-453b-bba3-3cc92ad348d6.png)
