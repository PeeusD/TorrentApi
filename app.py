import requests
from bs4 import BeautifulSoup  
print('''        

█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▀█▀ █▀█ █▀█ █▀█ █▀▀ █░░ █ ▀▄▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ░█░ █▄█ █▀▄ █▀▄ █▀░ █▄▄ █ █░█
 ''')

movie_res = input('Enter your movie to search: ')
movie_res.replace(' ', '+')
r = requests.get(f'https://torrentzeu.org/kick.php?q={movie_res}')
# print(r.status_code)
try:
        soup = BeautifulSoup(r.text,'html.parser')
        contents = soup.find('table', class_ = 'table')
        for content in contents.find_all('tbody'):
            rows = content.find_all('tr')
            # print(rows[5])
            i=0
            for row in rows:
                udt = []
                movie_name = row.find('span').text  #movie name
                leeches = row.find('td', attrs={ 'data-title':'Leeches'}).text # no. of leeches
                for seed in row.findAll('td', attrs={ 'data-title':'Last Updated'}):  #no. of seeders and last updt
                    udt.append(seed)
                last_updt = (str(udt[0])).strip('<td class="age-data" data-title="Last Updated"></td>')  #last updated
                seeds = (str(udt[1])).strip('<td data-title="Last Updated"></td>') #seeds
                
                file_size = row.find('td', attrs={ 'data-title':'Size'}).text  #file size
                links = row.find('a').get('href') #magnet links
                i=i+1
                
                print(f'⭐ {i} {movie_name} >> |Leeches:{leeches}| |Seeds:{seeds}| \n|Size:{file_size}| |Last Updated:{last_updt}| \n\n')

except Exception as e:
    print('Result not found Error: ',e)         

