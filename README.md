# Weather Prediction Project

This project uses global weather data from Kaggle to explore temperature trends and build simple machine learning models to predict next-day temperature.

## Dataset
Global Weather Repository  
https://www.kaggle.com/datasets/nelgiriyewithana/global-weather-repository

Download manually using:
kaggle datasets download -d nelgiriyewithana/global-weather-repository -p data/ –unzip

## Project Structure
notebooks/      → Jupyter notebooks for exploration
src/            → Python scripts (downloader, EDA helpers, models)
data/           → Dataset (ignored by Git)
README.md       → Project overview

## How to Run
1. Install packages:
pip install -r requirements.txt

2. Set up Kaggle API:
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

3. Download the dataset:
python src/download_data.py

4. Open the main notebook:
notebooks/weatheranalysis.ipynb

## Models
Currently testing:
- Linear Regression  
- Random Forest  
- XGBoost  

## Future Work
- Clean up code structure  
- Add more feature engineering  
- Improve model accuracy  