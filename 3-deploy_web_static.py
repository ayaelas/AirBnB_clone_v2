#!/usr/bin/python3
# Fabric script generates a .tgz archive

from datetime import datetime
from fabric.api import local, put, run, env
from os.path import exists
env.hosts = ['18.206.208.89', '100.25.145.25']


def do_pack():
    try:
        dt = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
	fil = "versions/web_static_{}.tgz".format(dt)
        local("tar -cvzf {} web_static".format(fil))
        return fil
    except Exception as e:
        return None


def do_deploy(archive_path):
    """distributes archive remotely"""
    if exists(archive_path) is False:
        return False
    try:
        """Extract Filename and No Extension"""
        fil = archive_path.split("/")[-1]
        na = fi.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, na))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fil, path, na))
        run('rm /tmp/{}'.format(fil))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, na))
        run('rm -rf {}{}/web_static'.format(path, na))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, na))
        return True
    except Exception as e:
        return False


def deploy():
    """deploy func"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
