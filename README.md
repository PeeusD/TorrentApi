## Torrent API - 
### Now you can download torrent files from this API. 


### Provides you details :
* **Title** - Descriptions of file. 
* **Leechers**- No. of current leechers who is uploading the file. 
* **Seeders** - No. of current seeders who is downloading the file.
* **File size** - File size in MB/GB.
* **Last Updated** - Total time elapsed after uploading the file. 
* **Magnet Links** -  For downloading the file.
* **Uses JWT(Json Webtoken)** for authentication

### How to use this API
* Create your registration into database:
  Method: **POST**
  Example **Json Format:**
  ```json {
    "email":"rahul@gmail.com",
    "name":"Rahul",
    "password": "1234567",
    "password2":"1234567"
      }
      ```
* Login and get your access token: 
    Method **POST**
    Example **JSON format**
  ```json {
    "email":"rahul@gmail.com",
    "password": "1234567"
      }
      ```
* Accessing Torrent Api: 
    Method **GET** 
    ```sh 
      http://127.0.0.1:8000/torrent/ 
    ```
    Method **POST** 
    ```sh 
      http://127.0.0.1:8000/torrent/ Authorization Bearer {your_accesstoken} 
    ```
    **JSON BODY** 
    ```sh 
    {"search" : "your_file_name"}
    ```

## Samples:

![alt text](https://github.com/PeeusD/TorrentApi/blob/main/gitpic/Capture1.PNG) <br>
### Sample - Browsable Api
![alt text](https://github.com/PeeusD/TorrentApi/blob/main/gitpic/Capture2.PNG) <br>
### Response in JSON
![alt text](https://github.com/PeeusD/TorrentApi/blob/main/gitpic/Capture3.png) <br>
### POST Request passing in JSON
