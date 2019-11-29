# INSTALL REQUIRED PACKAGES
pip3 install -r requirements.txt

# MIGRATE ALL MODELS TO THE DATABASE
python3 manage.py migrate

# CREATE USER TO LOGIN
python3 manage.py createsuperuser
(use this user to login, default: username=bawa, password=7800)

# RUN THE LOCAL SERVER
python3 manage.py runserverver