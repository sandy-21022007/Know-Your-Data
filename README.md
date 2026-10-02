# 📊 Know Your Data — EDA Tool

A professional, interactive Exploratory Data Analysis (EDA) web application built with Streamlit and Plotly. 
Quickly understand your datasets through beautiful visualizations, statistical summaries, and smart insights.

## ✨ Features

- **Data Overview**: Quick summary of dataset dimensions, memory usage, and sample data.
- **Missing Values Analysis**: Detailed breakdown and visualizations of missing data.
- **Statistical Summary**: Descriptive statistics for both numerical and categorical features.
- **Distributions**: Interactive histograms and box plots to explore data distributions.
- **Correlations**: Interactive correlation matrices and scatter plots for numerical variables.
- **Duplicates**: Automatic detection and display of duplicate rows.
- **Outlier Analysis**: Identification of outliers using robust statistical methods.
- **Type Recommendations**: Smart suggestions for memory optimization through data type downcasting.
- **Export Report**: Generate fully self-contained HTML reports of your analysis.

## 🚀 Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the application locally using Streamlit:
```bash
streamlit run app.py
```
Then open your browser and navigate to `http://localhost:8501`.

## 🛠️ Tech Stack

- **Framework**: [Streamlit](https://streamlit.io/)
- **Data Manipulation**: [Pandas](https://pandas.pydata.org/)
- **Visualizations**: [Plotly Express](https://plotly.com/python/plotly-express/)
- **Styling**: Custom CSS and HTML with Glassmorphism elements

## 📁 Project Structure

```
Know-Your-Data/
├── app.py                      # Main Streamlit application entry point
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── src/                        # Core analysis modules
│   ├── correlations.py         # Correlation analysis section
│   ├── data_loader.py          # Data upload and parsing
│   ├── distributions.py        # Distribution plots section
│   ├── duplicates.py           # Duplicate rows section
│   ├── missing_values.py       # Missing values analysis
│   ├── outliers.py             # Outlier detection
│   ├── overview.py             # Data overview section
│   ├── report_generator.py     # HTML report generation
│   ├── statistics.py           # Statistical summary section
│   └── type_recommendations.py # Data type optimization
└── utils/                      # Utility functions and helpers
    ├── helpers.py              # UI components and data utilities
    ├── plotting.py             # Plotly chart configuration
    └── styles.py               # Custom CSS injection
```

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for new features, bug fixes, or enhancements.

## 📄 License

This project is licensed under the MIT License.
