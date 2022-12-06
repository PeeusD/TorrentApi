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
### _REGISTER_
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

![alt text](https://github.com/PeeusD/TorrentApi/blob/main/gitpic/CaptureRegister.JPG) <br>


### _LOGIN_
* **Step-2 Login and get your access token | Method : POST**


     ```sh 
      http://127.0.0.1:8000/login/ 
    ```
  **Pass key value Json Format:**

  ```json 
  {
    "email":"rahul@gmail.com",
    "password": "1234567"
  }
    ```

![alt text](https://github.com/PeeusD/TorrentApi/blob/main/gitpic/CaptureLogin.JPG) <br>


### Searching files - Response in JSON into ThunderClient
* **Step-3 Searching and getting the torrent files details. Use Step-A (using PostMan/ThunderClient) or Step-B(Using DRF (Browsable Api) or HTTPIE client)**

  
  Method **POST** 
  
  *Step A: If you are using PostMan or ThunderClient then copy - paste your access token into "Authorization" tab with json key-value format. Eg: {"search" : "your_file_name"}*

    ```sh 
      http://127.0.0.1:8000/torrent/
    ```
    **Pass key value Json Format:**
    
    ```json
      {"search" : "your_file_name"}
   ```
   
    ![alt text](https://github.com/PeeusD/TorrentApi/blob/main/gitpic/CaptureSearch.JPG) <br>

**or**

### Getting Response in JSON in DRF Browsable Api
  *Step B: If you are using DRF (Browsable Api) or HTTPIE client; then copy and paste your access token as ApiKey into {your_accesstoken} with json key-value format. Eg:     {"search" : "your_file_name"}*
    
    ```sh 
      http://127.0.0.1:8000/torrent/Authorization Bearer {your_accesstoken} 
    ```

   **Pass key value Json Format:**
   
    ```json
      {"search" : "your_file_name"}
    ```
    
   ![alt text](https://github.com/PeeusD/TorrentApi/blob/main/gitpic/Capture1.PNG)








