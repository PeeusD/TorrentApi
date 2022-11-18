from django.db import models
import requests,random
from bs4 import BeautifulSoup  
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, password2=None):
        """
        Creates and saves a User with the given email, name
         and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email, name and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom User model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin






#Class for hangling torrent request
class Torrent:
    def __init__(self, res):
        self.res = res
    
    def handling_request(self):
        
        headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'},
                        { 'User-Agent' :'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'},
                                            { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'},
                                            { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'},
                                            { 'User-Agent' :'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'},
                                            { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}]
        try:
        
            r = requests.get(f'https://torrentz2.nz/search?q={self.res}', headers=headers[random.randint(0,4)])
            # print(r.status_code)
            soup = BeautifulSoup(r.text,'html.parser')
            contents = soup.find('div', class_ = 'results')
            i=1
            res = {}
            for content in contents.find_all('dl'):
                
                title = content.find('a').text
                torr_pg = content.find('a').get('href')
                magnet = content.find_all('a')[1].get('href')
                last_updt = content.find_all('span')[1].text
                file_size = content.find_all('span')[2].text
                seeders = content.find_all('span')[3].text
                leechers = content.find_all('span')[4].text
                # print(title , magnet, last_updt, file_size, seeders, leechers)
            
                res_dict = {
                        'title': title, 
                        'leechers': leechers, 
                        'seeders': seeders, 
                        'file_size':file_size, 
                        'last_updt':last_updt, 
                        'torPgLink': torr_pg,
                        'magnet': magnet
                    }  #appending multiple values into res_dict...
                res['⭐ '+ str(i)] = res_dict
                i+=1  
            return res
        except Exception as e:
            # print(e)
            return f'Error: BAD REQUEST'

        
                   