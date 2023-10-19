pip install pyPMML
from google.colab import drive
drive.mount('/content/drive')
from pypmml import Model
# Load the PMML model
model = Model.fromFile('/content/drive/MyDrive/Data Analytics/Revenue Prediction/revenue_prediction_model.pmml')
# Assuming you have some input data as a dictionary
input_data = {
    "Sum(Qty)": 886, #Qty tire michelin yang akan di billing dalam 1 bulan
    "Sum(EM)": 616, #Qty tire Michelin Earthmover yang akan dibilling dalam 1 bulan
    "Count(PODate)": 125, #Qty PO Michelin yang akan di billing dalam 1 bulan
    "Mean(Leadtime)": 295.806, #Target lead time (satuan hari) dari Factory ke CP
}

# Make prediction
result = model.predict(input_data)

print(result)
