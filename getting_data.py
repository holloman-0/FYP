import zipfile
import requests
import os
import mysql.connector

urls = {'Crime': "https://www.kaggle.com/datasets/marshallproject/crime-rates/download?datasetVersionNumber=1",
        'Macro': "https://www.kaggle.com/datasets/sarthmirashi07/us-macroeconomic-data/download?datasetVersionNumber=1 ",
        'Wage': 'https://www.kaggle.com/datasets/lislejoem/us-minimum-wage-by-state-from-1968-to-2017/download?datasetVersionNumber=4'}

# Zipped files will be put in current directory
def get_zipped_file():

    cookies = {
    'XSRF-TOKEN':'CfDJ8O8KA6ZuOudEn8EWH0HVxwv9S3i9BnGbqZwEQyqa8LixCy5mE6M8aFW7hbIp2Dgbn2F3BetOZVCcGUAmPZMzNsqyVqUv-NQtCLo8wo5KHSFvKqtghgrfWZfdB8dcA7B-3G6iwUBnO16Snn9DZcdIztI',
    '__Host-KAGGLEID':'CfDJ8O8KA6ZuOudEn8EWH0HVxwtbT3DvI0X860La99e_1b12ToK7KS2L_45rU0J_F4281BLz-e56LZTyqKu9i9Pmp0238KLffygZ9UqyZEFKiSbnf4GS9gmfdkiU',
    'CLIENT-TOKEN':'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJrYWdnbGUiLCJhdWQiOiJjbGllbnQiLCJzdWIiOiJqYWNreWJveTAwOTkiLCJuYnQiOiIyMDIyLTEwLTE3VDE0OjUxOjMxLjc2ODgzNTVaIiwiaWF0IjoiMjAyMi0xMC0xN1QxNDo1MTozMS43Njg4MzU1WiIsImp0aSI6ImJiNDJlYjJhLWViOTgtNGMxMS1iYmEzLTIwMGIwZDcxYmMxMSIsImV4cCI6IjIwMjItMTEtMTdUMTQ6NTE6MzEuNzY4ODM1NVoiLCJ1aWQiOjExOTgyNDMxLCJkaXNwbGF5TmFtZSI6ImphY2t5Ym95MDA5OSIsImVtYWlsIjoiamFja2ZlYXRoZXJzdG9uZTk5QGdtYWlsLmNvbSIsInRpZXIiOiJOb3ZpY2UiLCJ2ZXJpZmllZCI6ZmFsc2UsInByb2ZpbGVVcmwiOiIvamFja3lib3kwMDk5IiwidGh1bWJuYWlsVXJsIjoiaHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL2thZ2dsZS1hdmF0YXJzL3RodW1ibmFpbHMvZGVmYXVsdC10aHVtYi5wbmciLCJmZiI6WyJLZXJuZWxzUmVzdW1lIiwiS2VybmVsc0RyYWZ0VXBsb2FkQmxvYiIsIktlcm5lbHNGaXJlYmFzZUxvbmdQb2xsaW5nIiwiS2VybmVsc1N0YWNrT3ZlcmZsb3dTZWFyY2giLCJDb21tdW5pdHlLbUltYWdlVXBsb2FkZXIiLCJUUFVDb21taXRTY2hlZHVsaW5nIiwiQWxsb3dGb3J1bUF0dGFjaG1lbnRzIiwiS2VybmVsc1NhdmVDZWxsT3V0cHV0IiwiS01MZWFybkRldGFpbCIsIkZyb250ZW5kQ29uc29sZUVycm9yUmVwb3J0aW5nIiwiUGhvbmVWZXJpZnlGb3JDb21tZW50cyIsIlBob25lVmVyaWZ5Rm9yTmV3VG9waWMiLCJMaWhwTmV4dFN0ZXBzTWV0cmljcyIsIkttQ29tcHNTdWJtaXRQYW5lbCIsIkxlYXJuR3VpZGVzIiwiRGF0YXNldHNWYWxpZGF0ZVVwbG9hZGVkWmlwRmlsZXMiLCJLZXJuZWxFZGl0b3JIYW5kbGVNb3VudE9uY2UiXSwiZmZkIjp7Iktlcm5lbEVkaXRvckF1dG9zYXZlVGhyb3R0bGVNcyI6IjMwMDAwIiwiRnJvbnRlbmRFcnJvclJlcG9ydGluZ1NhbXBsZVJhdGUiOiIwLjAxIiwiRW1lcmdlbmN5QWxlcnRCYW5uZXIiOiJ7IH0iLCJDbGllbnRScGNSYXRlTGltaXQiOiI0MCIsIkZlYXR1cmVkQ29tbXVuaXR5Q29tcGV0aXRpb25zIjoiMzUzMjUsMzcxNzQsMzM1NzksMzc4OTgsMzczNTQsMzc5NTkiLCJBZGRGZWF0dXJlRmxhZ3NUb1BhZ2VMb2FkVGFnIjoiZGF0YXNldHNNYXRlcmlhbERldGFpbCJ9LCJwaWQiOiJrYWdnbGUtMTYxNjA3Iiwic3ZjIjoid2ViLWZlIiwic2RhayI6IkFJemFTeUE0ZU5xVWRSUnNrSnNDWldWei1xTDY1NVhhNUpFTXJlRSIsImJsZCI6IjgzZjljNWQyOWMwMWFlNTQ3ODFkZjI5MmE1YTYxOWRkNGU1YzQ5YTYifQ.',
    'CSRF-TOKEN':'CfDJ8O8KA6ZuOudEn8EWH0HVxwu4wPTBvg1yecy5xQ-zKZ8HiJ1pRsU6UaqrVVB-jxSCbYiESSA0EIw94LJVA7EiCtCXaSVO6xsp2cqv8hOfYQ',
    'GCLB':'CPGa__Wb54-SbA',
    '_gid':'GA1.2.150971428.1666000360',
    '_ga':'GA1.2.1947305487.1665676364',
    'ka_sessionid':'8504e3a174469653b119889226b200ab',
    }

    # For loop to cycle through each url we want to get from download_urls
    for x in urls:

        with open('{}.zip'.format(x), 'wb') as file:
            response = requests.get(urls[x],cookies=cookies, stream=True)
            file.write(response.content)

# Unzipped files will be in current directory
def unzip():

    for item in os.listdir(): # loop through items in dir

        if item.endswith(".zip"): # check for ".zip" extension
            zip_ref = zipfile.ZipFile(item) # create zipfile object
            zip_ref.extractall() # extract file to dir
            zip_ref.close() # close file
            os.remove(item) # delete zipped file


# Flow of the program

#zipped_files = get_zipped_file()
#unzip_files = unzip()