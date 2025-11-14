# Australian Stock Portfolio Optimization Analysis

> **Financial Analysis & Quantitative Portfolio Management**

A comprehensive quantitative analysis of Australian stock markets using modern portfolio theory, risk management techniques, and statistical methods to optimize investment portfolios for maximum risk-adjusted returns.

---

## **Executive Summary**

This project demonstrates advanced quantitative finance skills through a complete portfolio optimization framework analyzing 10 major Australian stocks over a 5-year period. The analysis includes:

- **Modern Portfolio Theory (MPT)** implementation
- **Risk-Return Optimization** using multiple strategies
- **Comprehensive Backtesting** with performance attribution
- **Monte Carlo Simulation** for risk assessment
- **Stress Testing** under various market scenarios
- **Financial Visualizations**

---

## **Key Findings**

### **Portfolio Performance Highlights**
- **Maximum Sharpe Portfolio**: 28.23% annual return, 17.68% volatility, 1.48 Sharpe ratio
- **Minimum Volatility Portfolio**: 12.46% annual return, 13.59% volatility, 0.77 Sharpe ratio
- **Equal Weight Benchmark**: 15.86% annual return, 15.21% volatility, 0.91 Sharpe ratio

### **Risk Management Insights**
- **95% VaR Analysis**: Portfolio risk ranges from -6.65% to -14.21% across strategies
- **Maximum Drawdown**: Controlled within acceptable limits for institutional standards
- **Correlation Analysis**: Identified diversification opportunities across sectors

---

## **Project Structure**

```
Stock-Portfolio-Optimization/
├── Stock Portfolio Optimization.ipynb # Main analysis notebook
├── portfolio optimation/ # Core Python package
│   ├── __init__.py
│   ├── backtest.py
│   ├── config.py
│   ├── data.py
│   ├── features.py
│   ├── optimizers.py
│   ├── plots.py
│   └── simulate.py
├─ Overview/
│   ├── Executive Summary.md
│   └── Portfolio Performance Report.md
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## **Quick Start**

### **Prerequisites**
- Python 3.8+
- Jupyter Notebook
- Basic understanding of financial markets

### **Installation**
```bash
# Clone the repository
git clone https://github.com/gabrielnguyen2603/Stock-Portfolio-Optimization.git
cd Stock-Portfolio-Optimization

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook
```

### **Running the Analysis**
1. Open `Stock Portfolio Optimization.ipynb`
2. Run all cells sequentially
3. Review the comprehensive analysis and visualizations

---

## **Analysis Components**

### **1. Data Collection & Preprocessing**
- **Source**: Yahoo Finance API
- **Period**: 5 years of daily data
- **Stocks**: 10 major Australian companies across sectors
- **Data Quality**: Automated cleaning and validation

### **2. Exploratory Data Analysis (EDA)**
- **Price Movement Analysis**: Historical trends and patterns
- **Return Distribution**: Statistical properties and risk metrics
- **Correlation Analysis**: Inter-stock relationships and diversification
- **Volatility Assessment**: Risk measurement and comparison

### **3. Portfolio Optimization**
- **Mean-Variance Optimization**: Modern Portfolio Theory implementation
- **Risk-Return Trade-offs**: Efficient frontier analysis
- **Multiple Strategies**: Max Sharpe, Min Volatility, Equal Weight
- **Constraint Handling**: Real-world portfolio constraints

### **4. Backtesting Framework**
- **Historical Performance**: Out-of-sample testing
- **Rebalancing Strategy**: Monthly portfolio adjustments
- **Performance Attribution**: Return decomposition analysis
- **Transaction Cost Analysis**: Real-world implementation costs

### **5. Risk Management**
- **Value at Risk (VaR)**: Multiple confidence levels
- **Expected Shortfall**: Tail risk assessment
- **Monte Carlo Simulation**: 10,000 scenario analysis
- **Stress Testing**: Market crash and rally scenarios

---

## **Business Applications**

### **For Individual Investors**
- **Portfolio Construction**: Evidence-based asset allocation
- **Risk Assessment**: Understanding portfolio risk characteristics
- **Performance Benchmarking**: Comparing against market indices

### **For Institutional Use**
- **Asset Management**: Quantitative portfolio management
- **Risk Management**: Comprehensive risk assessment framework
- **Client Reporting**: Professional performance attribution

### **For Financial Professionals**
- **Research & Development**: Quantitative finance methodology
- **Model Validation**: Backtesting and stress testing frameworks
- **Regulatory Compliance**: Risk reporting and documentation

---

## **Key Metrics & KPIs**

| Metric | Max Sharpe | Min Volatility | Equal Weight |
|--------|------------|----------------|--------------|
| **Annual Return** | 28.23% | 12.46% | 15.86% |
| **Volatility** | 17.68% | 13.59% | 15.21% |
| **Sharpe Ratio** | 1.48 | 0.77 | 0.91 |
| **Max Drawdown** | -45.7% | -21.5% | -79.7% |
| **Win Rate** | 59.2% | 65.3% | 63.3% |

---

## **Technical Implementation**

### **Libraries Used**
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib/seaborn**: Data visualization
- **scipy**: Optimization algorithms
- **PyPortfolioOpt**: Portfolio optimization
- **yfinance**: Financial data acquisition

### **Mathematical Models**
- **Markowitz Mean-Variance Theory**
- **Capital Asset Pricing Model (CAPM)**
- **Monte Carlo Methods**
- **Value at Risk (VaR) Models**
- **Sharpe Ratio Optimization**

---

## **Visualization Highlights**

The project includes over 20 financial visualizations:

- **Risk-Return Scatter Plots**: Portfolio efficiency analysis
- **Efficient Frontier**: Optimal portfolio combinations
- **Performance Attribution**: Return decomposition
- **Risk Heatmaps**: Correlation and volatility analysis
- **Monte Carlo Distributions**: Scenario analysis
- **Drawdown Analysis**: Risk assessment over time

---

## **Learning Outcomes**

This project demonstrates proficiency in:

- **Quantitative Finance**: Modern portfolio theory and risk management
- **Data Science**: Statistical analysis 
- **Financial Modeling**: Backtesting and performance attribution
- **Risk Management**: VaR, stress testing, and scenario analysis
- **Python Programming**: Advanced data manipulation and visualization
- **Business Intelligence**: Translating technical analysis into business insights

---

## **Contact & Collaboration**

**Author**: Gabriel (Hoang) Nguyen 

**Email**: gabrielnguyen2603@gmail.com

**LinkedIn**:www.linkedin.com/in/gabrielhoangnguyen

**GitHub**: https://github.com/gabrielnguyen2603

---

## **License**

This project is licensed under the MIT License - see the [LICENSE]([LICENSE](https://github.com/gabrielnguyen2603/Stock-Portfolio-Optimization/blob/main/LICENSE)) file for details.

---

## **Acknowledgments**

- **Yahoo Finance** for providing free financial data
- **PyPortfolioOpt** community for excellent portfolio optimization tools
- **Python Data Science** ecosystem for robust analytical tools
- **Financial Markets** for providing real-world data and insights

---

## **Further Reading**

- [Modern Portfolio Theory](https://en.wikipedia.org/wiki/Modern_portfolio_theory)


---

*This project represents a comprehensive application of quantitative finance principles to real-world portfolio management, suitable for both educational and professional purposes.*

--- 
## Important Note on Data

**This notebook fetches live financial data. The results of your analysis will be different from the original author's.**

The analysis window is set to exactly 5 years *prior to the date you run the code*. For example:

 If you run this on **October 18, 2025**, the data will be from **October 18, 2020 – October 18, 2025**.
 If you run this on **December 1, 2025**, the data will be from **December 1, 2020 – December 1, 2025**.

Because the dataset changes every day, all calculations, including **annual returns, volatility, Sharpe ratios, and optimal portfolio weights, will change**. This is expected behavior.








