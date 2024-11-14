-- src/configs/db_schema.sql

-- Incomes table
CREATE TABLE Incomes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    income_name TEXT NOT NULL,
    income_frequency TEXT,
    income_amount REAL,
    income_source TEXT,
    income_start_date DATE,
    income_end_date DATE,
    income_note TEXT,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES Categories(id)
);

-- Expenses table
CREATE TABLE Expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expense_name TEXT NOT NULL,
    expense_frequency TEXT,
    expense_start_date DATE,
    expense_end_date DATE,
    expense_method TEXT,
    expense_amount REAL,
    expense_note TEXT,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES Categories(id)
);

-- Transactions table
CREATE TABLE Transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    transaction_type TEXT NOT NULL CHECK(transaction_type IN ('income', 'expense')),
    transaction_desc TEXT,
    payment_method TEXT,
    transaction_amount REAL NOT NULL,
    account_balance REAL,
    notes TEXT,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES Categories(id)
);

-- Categories table
CREATE TABLE Categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL,
    parent_id INTEGER,
    FOREIGN KEY (parent_id) REFERENCES Categories(id)
);

-- Frequencies table
CREATE TABLE IF NOT EXISTS Frequencies (
    frequency_id INTEGER PRIMARY KEY AUTOINCREMENT,
    frequency_name TEXT NOT NULL UNIQUE
);