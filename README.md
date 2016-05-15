#How to Deploy

* pip install virtualenv
* virtualenv venv

#How to Prod
* `pip install fabric`
* fab init_prod_env

##supervisor
modify /etc/supervisor/supervisord.conf and change include section to `files = /etc/supervisor/conf.d/*.conf /var/www/wox/config/supervisor.conf`

##nginx
modify /etc/nginx/nginx.conf and add `include /var/www/wox/config/*.conf;` to http section


#Connect to Wox DB
`sudo -u postgres psql -d wox`
