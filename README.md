# 🔒 Phishing URL Detection System

A machine learning-based web application built with Streamlit to detect phishing URLs using Random Forest classification.

## 📋 Features

- Real-time phishing URL detection
- User-friendly web interface
- Confidence score display
- Probability breakdown for predictions
- Feature-based analysis of URLs

## 🛠️ Technologies Used

- **Python 3.x**
- **Streamlit** - Web framework
- **Scikit-learn** - Machine learning model
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/Priyamannem/Phishing-Data.git
cd Phishing-Data
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the Streamlit app:
```bash
streamlit run app.py
```
Or:
```bash
python -m streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## 📊 Features Analyzed

The model analyzes the following URL features:
- Number of dots in URL
- URL length
- Number of dashes
- Presence of @ symbol
- Use of IP address instead of domain
- HTTPS in hostname
- Path depth (number of slashes)
- Path length
- Number of numeric characters

## 📁 Project Structure
```
Phishing-Data/
│
├── app.py                      # Main Streamlit application
├── random_forest_model.pkl     # Trained ML model
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitignore                 # Git ignore file
```

## 🤖 Model Information

- **Algorithm**: Random Forest Classifier
- **Purpose**: Binary classification (Legitimate vs Phishing)
- **Output**: Prediction with confidence scores

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Always verify URLs through multiple methods and exercise caution when accessing unfamiliar websites.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

Priyamannem - [GitHub Profile](https://github.com/Priyamannem)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⭐ Show your support

Give a ⭐️ if this project helped you!
```

## Steps to Add This to Your Repository:

### Using VS Code:

1. **Open your project folder in VS Code**
```
   cd path\to\your\Phishing-Data
   code .