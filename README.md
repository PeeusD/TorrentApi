## Torrent API - 
### Now you can download torrent files from this API. 

### Libraries used:
* Django-Framework
* Django Rest Framework
* Beautiful Soup
* Requests

### Provides you details :
* Title - Descriptions of file. 
* Leechers- No. of current leechers who is uploading the file. 
* Seeders - No. of current seeders who is downloading the file.
* File size - File size in MB/GB.
* Last Updated - Total time elapsed after uploading the file. 
* Magnet Links -  For downloading the file.

### How to use this API
* Method GET = ""
* Method POST = Pass the key value in JSON
    `{"search" : "your_file_name"}`
    
## Samples:

![alt text](https://github.com/PeeusD/TorrentApi/blob/main/gitpic/Capture1.PNG) <br>
### Sample - Browsable Api
![alt text](https://github.com/PeeusD/TorrentApi/blob/main/gitpic/Capture2.PNG) <br>
### Response in JSON
![alt text](https://github.com/PeeusD/TorrentApi/blob/main/gitpic/Capture3.png) <br>
### POST Request passing in JSON
