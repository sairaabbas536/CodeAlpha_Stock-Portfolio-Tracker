# CodeAlpha_Stock-Portfolio-Tracker

# 📊 Stock Portfolio Tracker

This is a beginner-friendly Python script that helps you calculate your total stock investment. It uses hardcoded stock prices and allows users to enter the stock symbols and quantities they own.

## 🚀 Features

- ✅ Hardcoded stock prices for selected companies (AAPL, TSLA, GOOG, MSFT)
- 🧾 Accepts user input for stock symbols and quantities
- 💰 Calculates and displays total investment
- 💾 Optionally saves the output to a text file (`portfolio.txt`)

## 🛠️ How It Works

1. The user enters stock symbols and quantities.
2. The program checks if the symbol is valid (exists in the hardcoded price list).
3. It calculates the total value of each stock and the entire portfolio.
4. Optionally, it saves the result in a text file.

## 💻 How to Run

1. Make sure Python is installed on your system.
2. Clone or download this repository.
3. Open the terminal and navigate to the project directory.
4. Run the script using:

```bash 
python stock_tracker.py


##📁Example Output

Enter stock symbol (or 'done' to finish): AAPL
Enter quantity for AAPL: 3
Enter stock symbol (or 'done' to finish): TSLA
Enter quantity for TSLA: 2
Enter stock symbol (or 'done' to finish): done
AAPL: 3 x 180 = 540
TSLA: 2 x 250 = 500

Total Investment: $1040
Do you want to save this to a file? (yes/no): yes
Saved to portfolio.txt


##✨ Future Improvements

-Add live stock price fetching using an API

-Support for more stocks

-Export to CSV format

-GUI version using Tkinter or PyQt


👩‍💻 Created By: Saira Abbas

GitHub: https: //github.com/sairaabbas536
