import os
import shutil
import zipfile

DATASET = "nelgiriyewithana/global-weather-repository"   # Kaggle dataset ID
DOWNLOAD_DIR = "data"
DOWNLOAD_ZIP = f"{DOWNLOAD_DIR}/dataset.zip"

def download_latest():
    # Make sure data folder exists
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    print("➡️ Downloading latest dataset from Kaggle...")

    # Download the dataset ZIP
    exit_code = os.system(
        f"kaggle datasets download -d {DATASET} -p {DOWNLOAD_DIR} -o --force --quiet"
    )

    if exit_code != 0:
        print("❌ Download failed. Make sure Kaggle API is installed and your API key is set up.")
        return

    # Find the downloaded zip file
    zip_files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(".zip")]
    if not zip_files:
        print("❌ No ZIP file found after download.")
        return

    zip_path = os.path.join(DOWNLOAD_DIR, zip_files[0])

    print(f"📦 Extracting: {zip_path}")

    # Extract and overwrite files
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(DOWNLOAD_DIR)
    except Exception as e:
        print("❌ Error extracting ZIP:", e)
        return

    # Remove the ZIP after extraction
    os.remove(zip_path)

    print("✅ Dataset downloaded and updated successfully.")
    print(f"📁 Files available in: {DOWNLOAD_DIR}/")

if __name__ == "__main__":
    download_latest()

# run: python src/download_data.py