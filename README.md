# 深度學習

使用 Keras 和 TensorFlow 建立各式深度學習模型，包含：

* Mnist 手寫數字圖像辨識 - 灰階圖片分析
	* MLP Model, Autoencoder Model
* Cifar10 照片圖像辨識 - 彩色圖片分析
	* CNN Model
* Titanic 旅客生存率分析 - 典型分類問題（X1, X2, ..., Xn -> Y）
	* MLP Model
* IMDb 影評分析 - 自然語言處理、文字分析
	* MLP, RNN, LSTM Model
	
將訓練好的模型，以 Web Service/API 的方式提供服務：

* Flask
* Django

## 環境

### Operating System

Mac OS X

### Virtual Environment

Python 3.6 venv

### Python Package

* jupyter - 可在網頁介面上開發 Python，最大的特色是能夠以區塊的方式撰寫和執行代碼。
* scikit-learn - 可導入各式機械學習資料集。
* pandas - 可讀取各種檔案格式的資料集，並能產生可視化的表格，用以分析訓練和測試結果。
* matplotlib - 可圖形化圖像資料集，或產生各式圖表來分析模型的有效性。
* tensorflow - 低階的深度學習程式庫，學習門檻高，但開發彈性高，可微調參數或自創函式。
* keras - 高階的深度學習程式庫，學習門檻低，可幫助初學者快速建立深度學習模型。
* flask - 可快速建立一個簡單的 Web API。
* django - 免費且開放原始碼的 Web 應用程式框架。
* djangorestframework - 建立在 django 上的 REST API 框架。
