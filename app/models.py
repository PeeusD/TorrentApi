from django.db import models
import requests
from bs4 import BeautifulSoup  
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    user_id = models.IntegerField()
    password = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.name



#Class for hangling torrent request
class Torrent:
    def __init__(self, res):
        self.res = res
    
    def handling_request(self):
        r = requests.get(f'https://torrentz2.pics/data.php?q={self.res}')
            # print(r.status_code)
        try: 
            res = {}
            soup = BeautifulSoup(r.text,'html.parser')
            contents = soup.find('table', class_ = 'table')
            for content in contents.find_all('tbody'):
                rows = content.find_all('tr')
                # print(rows[5])
                i=0
                for row in rows:
                    udt = []
                    res_lst={}
                    title = row.find('span').text  #title
                    leeches = row.find('td', attrs={ 'data-title':'Leeches'}).text # no. of leeches
                    for seed in row.findAll('td', attrs={ 'data-title':'Last Updated'}):  #no. of seeders and last updt
                        udt.append(seed)
                    last_updt = (str(udt[0])).strip('<td class="age-data" data-title="Last Updated"></td>')  #last updated
                    seeds = (str(udt[1])).strip('<td data-title="Last Updated"></td>') #seeds
                    
                    file_size = row.find('td', attrs={ 'data-title':'Size'}).text  #file size
                    links = row.find('a').get('href') #magnet links
                    i=i+1
                    
                    # print(f'⭐ {i} {title} -->> |Leeches:{leeches}| |Seeds:{seeds}| |Size:{file_size}| |Last Updated:{last_updt}| \n\n')
                    
                    res_lst.update({
                        'title': title, 
                        'leechers': leeches, 
                        'seeders': seeds, 
                        'file_size':file_size, 
                        'last_updt':last_updt, 
                        'magnets': links
                    })  #appending multiple values into res_lst...
                    res['⭐'+str(i)] = res_lst
                return res
        except Exception as e:
            
            return f'Error: BAD REQUEST'
            # return f'Error'+str(e)

        
                   