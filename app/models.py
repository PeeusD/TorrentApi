from django.db import models
import requests
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

        
                   