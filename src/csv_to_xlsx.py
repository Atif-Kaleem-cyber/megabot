import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

# Title of the app
st.title("CSV Data Cleaning and Visualization App")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the original data
    st.subheader("Original Data")
    st.write(df)

    # Button to clean the CSV (remove rows with missing values)
    if st.button("Clean CSV (Remove Rows with Missing Values)"):
        df_cleaned = df.dropna()
        st.subheader("Cleaned Data")
        st.write(df_cleaned)
        df = df_cleaned  # Update the dataframe to the cleaned version

    # Button to remove NaN values
    if st.button("Remove NaN Values"):
        df_cleaned = df.fillna('')
        st.subheader("Data with NaN Values Removed")
        st.write(df_cleaned)
        df = df_cleaned  # Update the dataframe to the cleaned version

    # Button to save the cleaned data to an XLSX file and provide a download link
    if st.button("Save to XLSX"):
        towrite = BytesIO()
        df.to_excel(towrite, index=False, engine='xlsxwriter')
        towrite.seek(0)
        st.download_button(
            label="Download XLSX",
            data=towrite,
            file_name="cleaned_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        st.success("Data saved to 'cleaned_data.xlsx'")

    # Button to visualize the data
    if st.button("Visualize Data"):
        st.subheader("Data Visualization")
        
        # Example: Bar chart of the first numeric column
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        if len(numeric_columns) > 0:
            column_to_plot = numeric_columns[0]
            st.bar_chart(df[column_to_plot])
        else:
            st.warning("No numeric columns found for visualization.")

else:
    st.info("Please upload a CSV file to get started.")