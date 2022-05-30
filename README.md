# NOAA - Weather Data

## Overall
The content of this folder enables an **automated download/feature extraction/upload process**.

- First, data gets downloaded from an Amazon AWS S3 bucket
- Then required features are extracted, in this case:
    - Temperature
    - Humidity
    - Wind speed,

    and saved as a CSV file
- And finally the CSV gets uploaded to a GCP cloud storage.

All downloaded files gets deletet locally after the successfull upload. 

To start the process you have only to specify the variable `curr_date` in *line 49* which indicates the start date of downloading NOAA data from the official AWS S3 bucket. 

You can also specify the cloud buckets you want to download/upload from. The AWS S3 download bucket is specified in ***line 60***, the GCP upload bucket in ***line 43***.

<br>

## Usage
To run the script type:

1)  ``` {python}
    conda create --name noaa python=3.9
    ```
2)  ``` {python}
    conda activate noaa
    ```
3)  ``` {python}
    pip install -r requirements.txt
    ```
4)  ``` {python}
    python main.py
    ```