# Animax Development

If you've made it this far, thank you! We appreciate your contribution, and hope that this document helps you along the way. If you have any questions or problems, don't hesitate to [file an issue](https://github.com/zuri-training/anima_lib_team98/issues/new).

## Structure

The library has been compressed compressed into a zip file as `animax.zip`. The library contains two primary files:

  - animax.css : Animation codes are written and implemented using CSS Animations and saved in the `animax.css` file. This file contains all our available animations that user can apply into their web projects using the corresponding CSS selector such as the ID.
  - animation-usage-guide.md : This provides the user with a user-friendly manual of sort that shows the ID they can use to apply a particular CSS animation and their variations contained in `animax.css`. This provides the user with an offline support so they do not have to memorize any code or visit the web library eveytime they want to make use of our product.

## Timeline

* [x] Develop the product designs; the UI/UX, Lo-Fi & Hi-Fi, reusables and web page designs.
* [x] Develop the database schema to help illustrate how we use Django's models to store and access the database.
* [x] Develop the library using plain CSS.
* [x] Deploy a static web application on a server, using Heroku.
* [ ] Implement the static pages, database and authentication to build the web application.
* [ ] Implement the interactive funtionality on the web application for users to generate and save code combinations. 
* [ ] Deploy the web application on the server provisioned by Zuri.
* [ ] Publish animax to npm as `animax-css`.

h<h1 align="center">
    <a class="anim-pulse" href="https://animax-static.herokuapp.com/"><img src="./Logo.svg" width="175px" alt="animax logo"></a>
</h1>

<h1 align="center"> Deployment Instructions, Database & Architecture </h1>

---

<p align="center">The Animax database is MySQL and it will be deployed on the server using Ubuntu (Nginx) </p>

---

## Technologies

<p align="center">
   <img src="https://img.shields.io/badge/html5-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white" alt="html" />
  <img src="https://img.shields.io/badge/css3-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white" alt="css" />
  <img src="https://img.shields.io/badge/javascript-%23F7DF1E.svg?&style=for-the-badge&logo=javascript&logoColor=black" alt="JS" />
</p>
<p align="center">
 <img src="https://img.shields.io/badge/django-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white" />
 <img src="https://img.shields.io/badge/mysql-%234479A1.svg?&style=for-the-badge&logo=mysql&logoColor=white" />

## Resources/Links
 - [MySQL database](https://www.youtube.com/watch?v=WT8MKH9QACY&list=PL_dB_X6LL9RDprjk2BFV_Er2q6ao0Ii0m&index=2)
 - [Server setup with Ubuntu(Nginx)](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)


<h3 align="center"> Architecture </h3>

The architecture we are using is Monolith which is the Django Templating 


 <h3 align="center"> Database </h3>

- The database we used is MySQL because it was user friendly 

The details to accessour database which can be found in our project.setings.py: 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'animaxdatabase',
        'USER': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'PASSWORD':'Mustybalogs-1'
    }
}

 <h3 align="center"> Deployment Instructions to the server </h3>

## Setting up the server

-  To set up your server for log in, you will need to know your server's public IP adress, password or the private key for the user's account. The deployment will be done using Powershell IDE

- Then you log in as the root user using this command:

ssh root@your_server_ip

- then you will nedd to input your root password. If this is your first time logging into the server with a password, then you might want to change the root password. 

## Creating new user

- To create a new user (in our case, our username will be team98), the command line to input is :

adduser team98

## Admin privileges

- In order to set your user up as a superuser for our normal acccount, we need to add our account to the sudo group

- We log in back to the root account and run this command: 

usermod -aG sudo team98

## Login server using your new user

- To login into the server:

ssh team98@your_sever_ip

## Update latest versions of what is in your server

- To update your installed packages to the latest versions, run this command:

sudo apt-get update && sudo apt-get upgrade

## Configure and Enable Firewall

- It is important you configure firewall before enabling it

- We want to have HTTP, HTTPS AND SSH access

- We make sure to configure the SSH, this is the only way you log in to our server

- Ubuntu comes with the UFW firewall, run this commands to have access: 

sudo ufw allow http
sudo ufw allow https
sudo ufw allow ssh

- the port can also be used to configure, http 80, http 443, ssh 22:

sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 22

- To enable the firewall

sudo ufw enable

- To see the app configured items and the status of our firewall, run command:

ufw status


## Connecting device to the server to serve webpages

- To connect your device to the server, we can use nginx or Apache but we used nginx. Installing nginx, run:

sudo apt-get install nginx

## Locating our root directory in nginx

-To locate our root folder for all of our web applications,we need to go to where we are going to place allour files, run:

cd var/www/

this comes with a file from nginx titled index.html

-Make a new folder for you project (animax is the name of our product/project), run: mkdir animax

# Introducing our editor
- There are different types of editor out there, Nano and Vim is an example, but we will go with Nano

- We can create a file named index.html in the animax folder, run the command: sudo nano index.html

# Configure your new project to be served

- To do that you need to write your own server block, go into: cd /etc/nginx/sites-available/

- To open your default server block, which shows us how the index.html was deployed. It will show us our port in which it will run. it will also show us our root folder run: sudo nano default

- From this server block we can change our default server port, default file to deploy on our landing page, domain name we are using.

- We  can create a new server block also by running the command: sudo cp default animax.test


## Restarting Nginx

- To save any change on our block, we need to restart our nginx, run: sudo service nginx restart

# Enabling your site to be served

- We want to make sure our sites can be served and be deployed, we need to go back to the nginx folder directory, and find our to sites enabled-folder,to enable our site, we do a sym link, run: sudo ln-s /etc/nginx/sites-avaliable/animax.test

# Restart Nginx

To save your changes on the site, restart Nginx: sudo service nginx restart

## DNS (Domain Name System) Configuration

- To point your domain to your server: goto your domain platform and point your domain name to the ip address of your server so that whenever someone visits the domain name it displays what is on the ip address. In our case we are using zurifordummies.com

- Go back to our server terminal and run : ping zurifordummies.com

- When we type in zurifordummies.com in our browser now we can access our web page using domain name instead of IP address. 

-If you want it to be a subdomain, go to our domain platform and enable our domain to take a sub domain

- go to server block, and edit our server_name to our new domain (zurifordummies.com), we cant also  forget to restart nginx to save our changes 

## Insert a Certbot

- To secure your website we need to install a certbot, run the command:

sudo snap install core; sudo snap refresh core
sudo apt- get remove certbot 
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot/usr/bin/certbot
sudo certbot --nginx

then we restart our nginx to save our changes

## Deploy your project

- we go back to our www directory folder

- Now that we have our domain & our server block has been edited also, we can now deploy the project.

- Make sure git is installed on the server and clone your project from github to the server. 

- Go to the www directory: cd /var/www/

- Create our project folder: mkdir animax

- Open the folder: cd animax

- Create an index.html file, run: sudo nano index.html

- Go into the directory of sites-availabl,run: cd etc/nginx/sites-available/

- Create a new site : sudo cp default animax.zurifordummies.com

- Go to our server block and specify the directory of our project that we want to deploy as our site 

- Change the server name to your subdomain address

- will make the port listen to port 80: listen 80

- We need to enable our site now by going to the site enabled folder, run : cd sites-enabled 

- Create a symlink in the sites-enabled folder, run:  sudo ln -s etc/nginx/sites-available/animax.zurifordummies.com

- Create our SSL(certbot), run: sudo certbot --nginx, and select for which of the domain you want secured

- Restart your server, run:sudo service nginx restart

## Database Installation and configuration on the server

### To install MySQL database which was used for our projecty, run:

sudo apt-get install mysql
sudo systemctl start mysql.service

### To configure, open mySql prompt run: sudo mysql

-To chnage the rusers authentication method to one that uses a password, run: ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

-after this, exit MySQL prompt, run: exit 

- Run a security script that will take us to a series of prompt to make changes to MySQL installation : sudo mysql_secure_installation

- The above prompt will include, the strength type of password you want to use and also inputting your password 

### Creating a specific MySQL User and granting privileges

-Open MySQL prompt, run: sudo mysql
- To acces MySQL shell, run: mysql -u root -p

- To create a user, run: CREATE USER 'team98'@'host' IDENTIFIED WITH authentication_plugin BY 'password';

- To authenticate user and password, run: CREATE USER 'team98'@'localhost' IDENTIFIED BY 
'Mustybalogs-1';

- To grant privileges on database and table, run: GRANT PRIVILEGE ON animaxdatabase.table TO 'team98'@'host';

- To grantprivileges to our user, run: GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'team98'@'localhost' WITH GRANT OPTION;

-To free up any memory that the server has cached, run: FLUSH PRIVILEGES;

- Exit MySQL, run: exit

- To log into MySql, run: mysql -u team98 -p

### Testing MySQL

- To test run it, run: sudo systemctl status mysql.service

- To run administrative commands you can log in by running: sudo mysqladmin -p -u team98 version


## Active Members


|     Developers    | 
|       :----:      |
| Charles Precious  |
| Mustapha Balogun  |
|  Aroso Emmanuel Adedeji |
| Oguagu Ekenechukwu Daniel |
|   David Alatishe   |
|  Oluji Onyekachukwu |



