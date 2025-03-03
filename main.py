from fastapi import FastAPI, UploadFile, File
import os
from services import process_data

INPUT_FOLDER = "data"
OUTPUT_FORLDER = "output"

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FORLDER, exist_ok=True)

app = FastAPI()

@app.post("/process")
async  def process_uploaded_file(file: UploadFile = File(...)):
    # my endpoint to process uploaded csv file
    input_path = os.path.join(INPUT_FOLDER, file.filename)
    output_path = os.path.join(OUTPUT_FORLDER, "contract_features.csv")

    # save uploaded file
    with open(input_path, 'wb') as f:
        f.write(await file.read())

    # process file
    df = process_data(input_path, output_path)

    return {
        "message": "your data has been processed",
        "features_saved": output_path,
        "processed_sample": df.head().to_json()
    }

@app.get('/hey')
async def hey():
    return {
        "message": "hello world"
    }