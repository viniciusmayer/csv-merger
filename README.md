# get the script
```
sudo apt-get install git python3 python3-pip
sudo pip3 install virtualenv 
git clone https://github.com/viniciusmayer/csv-merger.git
virtualenv csv-merger
cd csv-merger
source bin/activate
pip install pandas
```

# get the files
```
sudo apt-get install google-cloud-sdk
gcloud auth activate-service-account --key-file <file_name>.json
gsutil -m cp "gs://<bucket_name>/<file_name>.csv" \
  "gs://<bucket_name>/<file_name>.csv" \
  . 
```

# params
edit the `main.py` and fill `dir_name` and `file_name`, where:
- `dir_name`: where are the files to be merged
- `file name`: the desirable name for the merged file

# get the merged file 
```
python main.py
```