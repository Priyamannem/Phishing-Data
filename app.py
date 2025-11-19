import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🔒",
    layout="wide"
)

# Title and description
st.title("🔒 Phishing URL Detection System")
st.markdown("""
This application uses a Random Forest machine learning model to detect phishing URLs.
Enter the URL features below to check if a URL is legitimate or a phishing attempt.
""")

# Load the model
@st.cache_resource
def load_model():
    try:
        with open('random_forest_model.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("Model file 'random_forest_model.pkl' not found. Please ensure the file is in the same directory.")
        return None
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

# Load the model
loaded_model = load_model()

if loaded_model is not None:
    st.success("✅ Model loaded successfully!")
    
    # Create two columns for better layout
    col1, col2 = st.columns(2)
    
    # Feature inputs
    with col1:
        st.subheader("URL Structure Features")
        num_dots = st.number_input("Number of Dots", min_value=0, max_value=20, value=3, 
                                   help="Number of dots/periods in the URL")
        url_length = st.number_input("URL Length", min_value=0, max_value=500, value=50,
                                     help="Total length of the URL in characters")
        num_dash = st.number_input("Number of Dashes", min_value=0, max_value=20, value=0,
                                   help="Number of dashes/hyphens in the URL")
        at_symbol = st.selectbox("@ Symbol Present", [0, 1], 
                                help="Whether @ symbol is present in URL (0=No, 1=Yes)")
        ip_address = st.selectbox("Uses IP Address", [0, 1],
                                 help="Whether URL uses IP address instead of domain (0=No, 1=Yes)")
    
    with col2:
        st.subheader("Additional Features")
        https_in_hostname = st.selectbox("HTTPS in Hostname", [0, 1],
                                        help="Whether 'https' appears in hostname (0=No, 1=Yes)")
        path_level = st.number_input("Path Level", min_value=0, max_value=20, value=3,
                                     help="Depth of URL path (number of slashes)")
        path_length = st.number_input("Path Length", min_value=0, max_value=200, value=20,
                                      help="Length of the path component in characters")
        num_numeric_chars = st.number_input("Number of Numeric Characters", min_value=0, max_value=100, value=5,
                                           help="Number of numeric characters in the URL")
    
    # Create prediction button
    st.markdown("---")
    if st.button("🔍 Analyze URL", type="primary", use_container_width=True):
        # Create input dictionary
        user_input = {
            'NumDots': num_dots,
            'UrlLength': url_length,
            'NumDash': num_dash,
            'AtSymbol': at_symbol,
            'IpAddress': ip_address,
            'HttpsInHostname': https_in_hostname,
            'PathLevel': path_level,
            'PathLength': path_length,
            'NumNumericChars': num_numeric_chars
        }
        
        # Create DataFrame
        user_df = pd.DataFrame([user_input])
        
        # Display input data
        with st.expander("📊 View Input Data"):
            st.dataframe(user_df, use_container_width=True)
        
        # Make prediction
        try:
            prediction = loaded_model.predict(user_df)
            prediction_proba = loaded_model.predict_proba(user_df)
            
            # Display results
            st.markdown("---")
            st.subheader("🎯 Prediction Results")
            
            if prediction[0] == 1:
                st.error("⚠️ **WARNING: This appears to be a PHISHING attempt!**")
                st.markdown(f"**Confidence:** {prediction_proba[0][1]*100:.2f}%")
                st.markdown("""
                **Recommendation:** 
                - Do NOT visit this URL
                - Do NOT enter any personal information
                - Report this URL to your IT security team
                """)
            else:
                st.success("✅ **This appears to be LEGITIMATE (not phishing)**")
                st.markdown(f"**Confidence:** {prediction_proba[0][0]*100:.2f}%")
                st.markdown("""
                **Note:** While the model predicts this is legitimate, always exercise caution online.
                """)
            
            # Show probability breakdown
            st.markdown("---")
            st.subheader("📈 Probability Breakdown")
            prob_col1, prob_col2 = st.columns(2)
            with prob_col1:
                st.metric("Legitimate Probability", f"{prediction_proba[0][0]*100:.2f}%")
            with prob_col2:
                st.metric("Phishing Probability", f"{prediction_proba[0][1]*100:.2f}%")
                
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")

# Sidebar information
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This application uses machine learning to detect phishing URLs based on their structural features.
    
    **Features Used:**
    - Number of dots in URL
    - URL length
    - Number of dashes
    - Presence of @ symbol
    - Use of IP address
    - HTTPS in hostname
    - Path depth and length
    - Numeric characters count
    
    **Model:** Random Forest Classifier
    """)
    
    st.markdown("---")
    st.markdown("**⚠️ Disclaimer**")
    st.caption("This tool is for educational purposes. Always verify URLs through multiple methods before accessing them.")