# CSV to XLSX Streamlit Application

This project is a Streamlit application that allows users to upload a CSV file, clean the data by removing rows with missing values, save the cleaned data to an XLSX file, and visualize the data using bar charts.

## Features

- Upload a CSV file.
- Clean the data by removing rows with missing values.
- Save the cleaned data to an XLSX file.
- Visualize the data using bar charts for numeric columns.

## Requirements

To run this application, you need to have Python installed on your machine. The required libraries are listed in the `requirements.txt` file.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/csv-to-xlsx-app.git
   ```

2. Navigate to the project directory:

   ```
   cd csv-to-xlsx-app
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit application, use the following command:

```
streamlit run src/csv_to_xlsx.py
```

This will start the application and open it in your default web browser.

## Usage

1. Upload a CSV file using the file uploader.
2. Use the provided buttons to clean the data, remove NaN values, and visualize the data.
3. Save the cleaned data to an XLSX file.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.