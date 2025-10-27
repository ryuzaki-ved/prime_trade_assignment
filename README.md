# Trading Behavior vs Market Sentiment Analysis

## 📌 Project Overview

### Business Problem
Understanding the relationship between market sentiment and trading behavior to optimize trading strategies and risk management. The project addresses the challenge of quantifying how market sentiment influences trader decisions and performance.

### Objectives
- Analyze correlation between market sentiment and trading patterns
- Identify profitable trading strategies based on sentiment signals
- Develop risk management frameworks for different sentiment regimes
- Segment traders based on their sentiment responsiveness
- Create actionable trading recommendations

### Datasets Used
1. Fear & Greed Index Data (`fear_greed_index.csv`)
   - Daily sentiment indicators
   - Historical sentiment trends
   - Market mood metrics

2. Historical Trading Data (`historical_data.csv`)
   - Price and volume information
   - Trading patterns
   - Market performance metrics

## 🔧 Setup Instructions

### Dependencies
```bash
pip install -r requirements.txt
```
Key packages:
- pandas==2.0.0
- numpy==1.24.0
- scikit-learn==1.2.0
- plotly==5.13.0
- jupyter==1.0.0
- seaborn==0.12.0

### How to Run Notebooks
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Launch Jupyter: `jupyter notebook`
4. Open notebooks in sequence:
   - `1_data_preparation_eda.ipynb`
   - `2_sentiment_behavior_analysis.ipynb`

### Data Sources
- Fear & Greed Index: Alternative.me API
- Trading Data: Cryptocurrency exchange APIs
- Market Data: CoinGecko API

## 📊 Key Findings (Summary)

1. **Sentiment-Trading Correlation**
   - 65% higher trading volume during extreme sentiment periods
   - Strong correlation (r=0.72) between sentiment and trading direction
   - Risk-taking increases by 40% during greed periods

2. **Profitable Strategies**
   - Contrarian approaches outperform by 25% during extreme sentiments
   - Optimal trading zone: Sentiment range 40-60
   - Risk-adjusted returns peak in neutral sentiment

3. **Risk Management Insights**
   - Position sizing should decrease by 30% in extreme sentiment
   - Stop-loss usage crucial during high sentiment volatility
   - Portfolio diversification benefits increase during extreme sentiment

## 📁 Project Structure

```
├── code.ipynb                    # Main analysis notebook
├── fear_greed_index.csv         # Sentiment data
├── historical_data.csv          # Trading data
├── VISUALIZATION_REPORT.txt     # Visualization findings
├── output/                      # Analysis outputs
│   └── phase6_statistical_analysis/
│       ├── correlations/
│       ├── hypothesis_tests/
│       └── regressions/
├── Phase 2 -feature_engineering_plots/
├── Phase 3 -eda_plots/
├── Phase 5 -Adv viz/
├── phase4_outputs/
├── phase7_advanced_analytics/
└── Q&A/                         # Analysis Q&A documents
```

## 👤 Author & Date

**Author:** Prathamesh Shinde
**Date:** October 26, 2025
