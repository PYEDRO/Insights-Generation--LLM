# Dataset Analysis with Insights Generation via LLM

This project is an interactive web application that allows users to upload a CSV dataset, perform basic exploratory analysis, and generate insights using a language model (LLM). The application integrates the following technologies:

- **Streamlit**: for the interactive web interface.
- **Pandas**: for data manipulation and analysis.
- **Transformers (DistilGPT2)**: for generating insights.
- **Matplotlib**: for data visualization (e.g., histograms).

## Features

- **CSV Dataset Upload:** Easily upload your dataset in CSV format.
- **Data Visualization:** Display the first few rows, descriptive statistics, and data types.
- **Automated Summary:** Generate a textual summary of the dataset based on descriptive statistics and data types.
- **LLM-Generated Insights:** Generate insights by prompting the LLM to analyze the dataset summary.
- **Optional Visualizations:** Visualize numeric data through histograms.

## Prerequisites

- Python 3.7 or higher.
- Internet connection (to load the language model and images, if applicable).

## Installation

1. **Clone the repository** or download the project files.

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   # Activate the environment:
   # On Windows:
   venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install streamlit transformers torch pandas matplotlib
   ```

   > **Note:** If you encounter an error related to Keras (e.g., "Your currently installed version of Keras is Keras 3..."), install the compatible package:
   >
   > ```bash
   > pip install tf-keras
   > ```

## How to Run

1. Save the main code in a file named `app_dataset_insights.py`.

2. Open your terminal and run the following command:

   ```bash
   streamlit run app_dataset_insights.py
   ```

3. A new browser window will open displaying the Streamlit interface, where you can interact with the application.

## How to Use

1. **Upload the Dataset:**  
   Use the file uploader in the interface to select a CSV file.

2. **Data Visualization:**  
   Once the dataset is uploaded, the app displays:
   - The first few rows of the dataset.
   - Descriptive statistics (using `df.describe()`).
   - Data types for each column.

3. **Automated Summary:**  
   A textual summary of the dataset is automatically generated based on the descriptive statistics and data types, and displayed in a text area.

4. **Generating Insights:**  
   Click the "Generate Insights" button to prompt the LLM (DistilGPT2) to analyze the dataset summary and generate insights. The insights will identify patterns, trends, potential issues, and suggest further analysis paths.

5. **Optional Visualization:**  
   If the dataset contains numeric columns, you can select one to visualize its distribution using a histogram.

## Potential Improvements

- Support for other file formats (e.g., Excel).
- Integration with more advanced language models.
- Tuning the prompt and generation parameters for deeper insights.
- Adding additional visualizations and exploratory data analysis features.

