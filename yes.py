
import requests

download_url = 'https://www.kaggle.com/datasets/sarthmirashi07/us-macroeconomic-data/download?datasetVersionNumber=1'

# More efficient by downloading immediately instead of loading whole file in memory
req = requests.get(download_url, stream=True) 

if req.ok:

    with open('file.zip', 'wb') as file:
        for chunk in req.iter_content(1024 * 100):
            file.write(chunk)


else:
    print("Something went wrong :( ")

