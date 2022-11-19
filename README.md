## Torrent API [Unofficial]
### Now you can download torrent files from this API. 

<img src="https://github.com/PeeusD/TorrentApi/blob/main/gitpic/magnet.png" width="500" title="hover text">

### Currently the API can get the following details for a specific files in JSON format:
* **Title** - Descriptions of file. 
* **Leechers**- No. of current leechers who are downloading the file. 
* **Seeders** - No. of current seeders who are uploading the file.
* **File size** - File size in MB/GB.
* **Last Updated** - Total time elapsed after uploading the file. 
* **Magnet Links** -  Torrent/Magnet links for downloading the file.


### How to use this API
* **Step-1 Create your registration into database | Method:POST**


   ```sh 
      http://127.0.0.1:8000/register/ 
    ```
  **Example:** pass key value **Json Format:**
  
  ```json 
  {
    "email":"rahul@gmail.com",
    "name":"Rahul",
    "password": "1234567",
    "password2":"1234567"
  }
    ```

* **Step-2 Login and get your access token | Method : POST**


     ```sh 
      http://127.0.0.1:8000/login/ 
    ```
  **Example:** pass key value **Json Format:**

  ```json 
  {
    "email":"rahul@gmail.com",
    "password": "1234567"
  }
    ```

* **Step-3 Copy your access token and paste into "Authorization" tab and pass Json format Eg. {"search" : "your_file_name"}**

  
  Method **POST** 
  Step A: If you are using PostMan or ThunderClient then copy - paste your access token into "Authorization" tab with json key-value format. Eg: {"search" : "your_file_name"}

    ```sh 
      http://127.0.0.1:8000/torrent/
    ```

  Step B: If you are using DRF (Browsable Api) or HTTPIE client; then copy and paste your access token into "Authorization" tab with json key-value format. Eg: {"search" : "your_file_name"}
    
    ```sh 
      http://127.0.0.1:8000/torrent/ Authorization Bearer {your_accesstoken} 
    ```

    ```sh 
    {"search" : "your_file_name"}
    ```

## Samples:

![alt text](https://github.com/PeeusD/TorrentApi/blob/main/gitpic/CaptureRegister.JPG) <br>
### _REGISTER_
![alt text](https://github.com/PeeusD/TorrentApi/blob/main/gitpic/CaptureLogin.JPG) <br>
### _LOGIN_
![alt text](https://github.com/PeeusD/TorrentApi/blob/main/gitpic/Capture3.png) <br>
### _POST Request passing in JSON_
![alt text](https://github.com/PeeusD/TorrentApi/blob/main/gitpic/CaptureSearch.JPG) <br>
### Searching files - Response in JSON into ThunderClient
![alt text](https://github.com/PeeusD/TorrentApi/blob/main/gitpic/Capture1.PNG) <br>
### _Getting Response in JSON in DRF Browsable Api_

