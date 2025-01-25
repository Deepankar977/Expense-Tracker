# Expense Tracker

An interactive Python-based application that helps users manage their finances by tracking income, expenses, and net balance. This project allows users to record financial data and view previous transaction histories.

## Features

- **Add Income**: Record additional income to your account.
- **Add Expense**: Track expenses and manage your spending.
- **Net Balance Check**: View the total net balance based on income and expenses.
- **View Records**: Access a complete log of financial transactions.
- **Dual Entry**: Simultaneously add income and expenses in one session.

## How It Works

1. **User Menu**: Select from options to add income, expenses, view net balance, or check previous records.
2. **File Storage**: Financial data is stored persistently across three files:
   - `Income_rec.txt`: Tracks income entries.
   - `Expense_rec.txt`: Tracks expense entries.
   - `MoneyRec.txt`: Maintains a complete log of income, expenses, and net balance by date.
3. **Date Tracking**: Automatically logs transactions with the current date for better tracking.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd Expense-Tracker
