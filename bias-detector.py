import streamlit as st
from google.generativeai import GenerativeModel, configure

# Replace with your actual API key
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
configure(api_key=GOOGLE_API_KEY)

# Load the Gemini Pro model
model = GenerativeModel("gemini-2.5-pro-exp-03-25")

def analyze_bias(text):
    """
    Analyzes the input text for potential gender and cultural biases using Gemini Pro.
    Returns a string with the analysis.
    """
    prompt = f"""Analyze the following text for potential gender and cultural biases.
    Identify specific phrases or words that might be considered biased.
    Explain why these phrases might be biased in the context of gender or culture.

    Text:
    {text}

    Bias Analysis:"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error during bias analysis: {e}"

def suggest_neutral_rephrasing(text, bias_analysis):
    """
    Suggests neutral rephrasing for potentially biased parts of the text using Gemini Pro.
    Considers the bias analysis provided.
    Returns a string with the rephrased suggestions.
    """
    prompt = f"""The following text has been analyzed for bias, and the analysis is provided below.
    Suggest neutral rephrasing for the parts of the text that were identified as potentially biased.
    Maintain the original meaning of the text while making it more neutral in terms of gender and culture.

    Text:
    {text}

    Bias Analysis:
    {bias_analysis}

    Neutral Rephrasing Suggestions:"""
    try:
        response = model.generate_content(prompt)
        return response.text  # This line is crucial
    except Exception as e:
        return f"Error during rephrasing: {e}"

def main():
    st.title("Bias Detect Tool")
    st.subheader("Analyze text for potential gender and cultural biases and get neutral rephrasing suggestions.")

    input_text = st.text_area("Enter text to analyze:", height=200)

    if st.button("Analyze"):
        if input_text:
            with st.spinner("Analyzing text for bias..."):
                bias_analysis_result = analyze_bias(input_text)

            st.subheader("Bias Analysis:")
            st.write(bias_analysis_result)

            with st.spinner("Generating neutral rephrasing suggestions..."):
                rephrasing_suggestions = suggest_neutral_rephrasing(input_text, bias_analysis_result)

            st.subheader("Neutral Rephrasing Suggestions:")
            st.write(rephrasing_suggestions)
        else:
            st.warning("Please enter some text to analyze.")

if __name__ == "__main__":
    main()
