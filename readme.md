readme.md
# 📈 Stock Price Prediction Using Machine Learning

## Project Overview
This project predicts the next day's stock closing price using historical stock market data and Machine Learning. The model uses a Random Forest Regressor trained on stock data fetched from Yahoo Finance.

## Features
- Fetches real-time historical stock data
- Data preprocessing and cleaning
- Machine Learning-based prediction
- Predicts next day's closing price
- Visualizes actual vs predicted prices
- Easy to use and customizable

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Yahoo Finance (yfinance)

## Project Structure

```text
StockPricePrediction/
│
├── stock_prediction.py
├── README.md
└── requirements.txt
```

## Installation

1. Clone the repository:

```bash
git clone <repository-link>
cd StockPricePrediction
```

2. Install required libraries:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install yfinance pandas numpy scikit-learn matplotlib
```

## How to Run

Run the Python file:

```bash
python stock_prediction.py
```

Enter a stock symbol when prompted:

```text
AAPL
```

Example stock symbols:
- AAPL (Apple)
- TSLA (Tesla)
- MSFT (Microsoft)
- GOOGL (Google)

## Machine Learning Workflow

1. Collect stock data from Yahoo Finance
2. Preprocess the dataset
3. Create target values (next day's closing price)
4. Split data into training and testing sets
5. Train Random Forest Regression model
6. Evaluate model performance
7. Predict next day's stock price
8. Visualize results

## Evaluation Metric

The model uses:

- Mean Absolute Error (MAE)

to measure prediction performance.

## Future Enhancements

- Streamlit Web Dashboard
- LSTM Deep Learning Model
- Multiple Stock Comparison
- Real-Time Price Updates
- Buy/Sell Signal Generation
- Model Performance Comparison

## Learning Outcomes

Through this project, I learned:

- Data Collection and Preprocessing
- Machine Learning Model Training
- Regression Techniques
- Data Visualization
- Financial Data Analysis
- Python Libraries for Data Science

## Author

Developed as a Machine Learning project for learning and academic purposes.