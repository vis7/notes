Link for tutorial : https://cloud-blogs.com/index.php/oracle-cloud/oracle-cloud-iaas/oracle-cloud-infrastructure-oci-blogs/setting-up-django-python-web-environment-on-oracle-cloud/

Link for Ingress Rules : https://oracle-base.com/articles/vm/oracle-cloud-infrastructure-oci-amend-firewall-rules

- Create Instance
- Add Ingress Rules under Security List in Network Security Groups.
- Use  SSH with Private Key

Commands
- `chmod 400 <private_key>`
- `ssh -i <private_key> <username@ip_address>`

- `sudo iptables --list --line-numbers`
- `sudo iptables -D INPUT 6`
- `sudo netfilter-persistent save`
- `sudo netfilter-persistent reload`

- `sudo apt update`
- `sudo apt install python3-pip`
 

- `ssh-keygen -t rsa`
- `cat /home/ubuntu/.ssh/id_rsa.pub` Will return an SSH key, add it into your GitHub SSH Keys to download Private Repositories.
- `git clone git@github.com:kairavkkp/VFW-API-Django.git`
- `python3 -m pip install --user virtualenv`
- `python3 -m virtualenv django-env`
- `cd VFW-API-Django`
- `pip install -r requirements.txt`
- `cd vfw`
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`
- `python3 manage.py runserver 0.0.0.0:8080`
- Access the admin panel using http://152.67.166.124:8080/admin/. Admin UserName : `kkp` and Password : `toor`. (Can be changed Later)

####
install apache2
- `sudo apt update`
- `sudo apt install apache2`
check installation of wsgi
- `sudo a2enmod wsgi`

install wsgi
- `sudo apt-get install -python3-pip apache2 libapache2-mod-wsgi-py3`


create superuser
- `sudo adduser <admin_name> # vfw_admin`
then create password and reenter it
provide name and phone number

making user superuser
- `sudo usermod -aG sudo vfw_admin`

verifying user type
- `sudo whoami`




create virtualenv and install requirements

clone repository
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py collectstatic`
- `python manage.py migrate --run-syncdb`

make apache2 owner of directory and give it required permission
- `sudo chown -R www-data:www-data demo_site`
- `sudo chmod -R 755 demo_site`

take copy of config file and do change bellow edits and put it inside "/etc/apache2/sites-available/"
a2ensite demosite.conf 

reload server 
sudo service apache2 reload/restart
sudo systemctl restart apache2









