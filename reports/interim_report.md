# Interim Report: Brent Oil Change Point Analysis

## 1. Objective

The primary goal of this analysis is to understand how major geopolitical and economic events influence Brent oil prices. Using Bayesian change point detection, we aim to identify structural breaks in the oil price time series and relate them to specific real-world events.

## 2. Data Science Workflow

### Step 1: Data Collection & Cleaning
- Load Brent oil prices from 1987 to 2022.
- Convert 'Date' column to datetime format.
- Sort data and handle missing values.
- Calculate log returns for stationarity.

### Step 2: Event Compilation
- Create a CSV file with 10–15 major global events.
- Include political decisions, conflicts, sanctions, and OPEC announcements.

### Step 3: Exploratory Data Analysis
- Visualize raw prices and log returns.
- Identify periods of volatility or major shifts.

### Step 4: Bayesian Change Point Modeling (PyMC3)
- Define a single change point (`tau`) using a discrete uniform prior.
- Create models for mean/volatility before and after `tau`.
- Use MCMC sampling to estimate posterior distributions.

### Step 5: Insight Generation
- Identify likely change points and compare with real events.
- Quantify the impact (e.g., % shift in average prices).

### Step 6: Dashboard (Flask + React)
- Flask API to serve results.
- React frontend to visualize timelines, price shifts, and event correlations.

### Step 7: Reporting
- Compile a final report and/or blog post.
- Focus on clear communication of Bayesian insights.

## 3. Assumptions and Limitations

- We assume availability and accuracy of Brent oil daily prices.
- Causal relationships cannot be fully proven, only correlated statistically.
- Events are manually compiled and not exhaustive.

## 4. Communication Channels

- Reports: Blog post or PDF summary
- Dashboard: Interactive web dashboard (Flask + React)
- Stakeholders: Policymakers, analysts, investors, energy companies
