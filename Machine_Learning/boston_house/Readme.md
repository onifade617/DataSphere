# 🏠 Boston Housing Price Prediction (Streamlit App)

This project is an interactive **Streamlit web application** that explores the classic **Boston Housing dataset**, trains a **Linear Regression model**, and allows users to make predictions on housing prices based on selected test data rows.

---

## 📌 Features

✅ **Explore the dataset** – View the first few rows and shape of the Boston Housing dataset.  
✅ **Visualize correlations** – Interactive heatmap showing relationships between features and `medv` (Median value of owner-occupied homes).  
✅ **Train a Linear Regression model** – The app automatically trains a model using scikit-learn.  
✅ **Evaluate model performance** – Displays **Mean Absolute Error (MAE)** and **Mean Squared Error (MSE)**.  
✅ **Compare Actual vs Predicted values** – View a table comparing real and predicted housing prices.  
✅ **Make interactive predictions** – Select a row from the test set and see its predicted price vs. the actual price.

---

## 🛠️ Tech Stack

- [Python 3.x](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – for building the interactive web app  
- [Pandas](https://pandas.pydata.org/) – data manipulation  
- [NumPy](https://numpy.org/) – numerical computations  
- [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/) – data visualization  
- [Scikit-learn](https://scikit-learn.org/) – model training & evaluation  

---

## 📂 Dataset

The project uses the **Boston Housing Dataset** (`boston.csv`), which contains the following columns:

- **CRIM** – per capita crime rate by town  
- **ZN** – proportion of residential land zoned for lots over 25,000 sq.ft.  
- **INDUS** – proportion of non-retail business acres per town  
- **CHAS** – Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)  
- **NOX** – nitric oxides concentration (parts per 10 million)  
- **RM** – average number of rooms per dwelling  
- **AGE** – proportion of owner-occupied units built prior to 1940  
- **DIS** – weighted distances to five Boston employment centers  
- **RAD** – index of accessibility to radial highways  
- **TAX** – full-value property-tax rate per $10,000  
- **PTRATIO** – pupil-teacher ratio by town  
- **B** – 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town  
- **LSTAT** – % lower status of the population  
- **MEDV** – Median value of owner-occupied homes (target variable)

---

## 🚀 Installation & Usage
```pip install -r requirements.txt```

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/boston-housing-streamlit.git
cd boston-housing-streamlit
