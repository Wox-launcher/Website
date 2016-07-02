import os
from fabric.api import local
from fabric.context_managers import lcd
import time

BASE_DIR = os.path.dirname(__file__)

def __is_windows():
    return os.name == "nt"

def __get_python():
    if __is_windows():
        return os.path.join(BASE_DIR,"venv/Scripts/python.exe")
    else:
        return os.path.join(BASE_DIR,"venv/bin/python")

def __get_pip():
    if __is_windows():
        return os.path.join(BASE_DIR,"venv/Scripts/pip.exe")
    else:
        return os.path.join(BASE_DIR,"venv/bin/pip")

def __get_manage():
    return os.path.join(BASE_DIR,"api/manage.py")

def __python(command):
    local("{} {}".format(__get_python(),command))

def __pip(command):
    local("{} {}".format(__get_pip(),command))

def __manage(command):
    __python("{} {}".format(__get_manage(),command))

####################################### Commands ###################################################

def requirements():
    """install requirements via pip"""
    env = os.environ.get("woxenv", "prod")
    r = os.path.join(BASE_DIR,"api","requirements", "{}.txt".format(env))
    __pip("install -r {}".format(r))

def migrate():
    """make migrations and migrate db"""
    __manage("makemigrations")
    __manage("migrate")

def test():
    """run all tests"""
    oldenv = os.environ.get("woxenv", "prod")
    os.environ["woxenv"] = "test"
    __manage("test {}".format(os.path.join(BASE_DIR,"api")))
    os.environ["woxenv"] = oldenv

def installDependency():
    local("sudo apt-get install nginx supervisor python-virtualenv uwsgi uwsgi-plugin-python postgresql libpq-dev")

def deploy():
    """deploy wox (including update) in prod"""
    local("git pull")
    requirements()
    migrate()
    test()
    __manage("collectstatic --noinput")
    run()
    buildclient()
    builddoc()

def buildclient():
    """build client"""
    with lcd(os.path.join(BASE_DIR,"client")):
        local("bower install --allow-root")
        local("grunt build --force")

def run():
    """run app"""
    env = os.environ.get("woxenv", "prod")
    if env == "prod":
        local("supervisorctl restart wox")
    else:
        __manage("runserver 0.0.0.0:7000")

def builddoc():
    """build gitbook doc"""
    with lcd("/app/wox_doc"):
	local("git pull")
  	local("gitbook build")

def backup():
    """Backup DB and Media files to Dropbox (require dropbox-uploader installed)"""
    backup_folder = os.path.join(BASE_DIR,"backup")
    backup_name = time.strftime("%Y%m%d") + ".zip"
    local("rm -r {}".format(backup_folder))
    if not os.path.exists(backup_folder):
	os.mkdir(backup_folder)

    with lcd("/app"):
	local("zip -r {} {}".format(os.path.join(backup_folder,"media.zip"),"wox_media"))
    with lcd(backup_folder):
	local("PGPASSWORD=scott pg_dump -U wox wox > {}".format("woxdb.dump"))
	local("zip {} woxdb.dump media.zip".format(backup_name))
    	local("/root/github/Dropbox-Uploader/dropbox_uploader.sh upload {} {}".format(backup_name,backup_name))

