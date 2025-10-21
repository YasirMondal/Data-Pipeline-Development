🧠 Data Pipeline: Data Preprocessing,Transformation and Loading

This Python script automates the ETL (Extract, Transform, Load) process using pandas and scikit-learn.
It fetches an online dataset, preprocesses it (removes duplicates, handles missing values), transforms it (scaling + encoding), and saves a clean version as a CSV file — ready for further analysis or modeling.


*COMPANY*: CODTECH IT SOLUTIONS PVT.LTD
*NAME*: Yasir Siraj Mondal
*DOMAIN*: Data Science
*DURATION*: 12 weeks
*MENTOR*: Neela Santhosh Kumar



⚙ Steps Performed

1. Extract – Loads the Iris dataset directly from an online URL using pandas.read_csv().

2. Preprocess – Removes duplicate rows and fills missing values with the mean (for numeric) or mode (for categorical).

3. Transform – Uses ColumnTransformer and Pipeline from scikit-learn to:
Standardize numeric columns.
One-hot encode categorical columns.

4. Load – Exports the final transformed dataset as cleaned_data.csv.


🧰 Requirements

Before running the script, install the necessary libraries:

pip install pandas scikit-learn

Optional (if using a virtual environment):

python -m venv .venv
.\.venv\Scripts\activate       # On Windows
# or
source .venv/bin/activate      # On Mac/Linux


▶ How to Run
1. Open the folder containing etl.py in VS Code or a terminal.

2. Run the following command:
python etl.py

3. The script will:
Fetch data from the web.
Clean and transform it.
Save the output file named cleaned_data.csv in the same folder.


🧾 Output

cleaned_data.csv → A fully cleaned and transformed version of the dataset.
Contains scaled numeric values and encoded categorical features.


🧱 Tech Stack

Python 3.8+

pandas

scikit-learn
