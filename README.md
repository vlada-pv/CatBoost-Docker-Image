# CatBoost-Docker-Image

The project should include the front and back parts. Communication between front and back is implemented via API.  The front of the container is available at port :3000 The front part offers the option of uploading a scoring file in the format.csv dataset from the competition. And the option to upload the file after scoring by the model in the sample_submission<time>.csv format.   

The service performs the following stages of the ML project inside the container with separate scripts: 
* API
* Input file loading and data preprocessing
* Scoring of the processed dataset
