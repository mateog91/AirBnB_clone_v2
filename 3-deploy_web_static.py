#!/usr/bin/python3
"""Fabric script that creates and distributes an archive
to your web servers, using the function deploy
"""
from genericpath import isdir
from os.path import exists
from fabric.api import local, put, run, env
from datetime import datetime
env.hosts = ['35.196.20.175', '52.23.183.91']
env.user = 'ubuntu'


def do_pack():
    """Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack
    """
    try:
        if isdir('versions') is False:
            local("mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        tgz_name = "web_static_" + date + ".tgz"
        local("tar -cvzf versions/{} web_static".format(tgz_name))
        return "versions/{}".format(tgz_name)
    except Exception:
        return None


def do_deploy(archive_path):
    """Fabric script that distributes an archive to your web servers,
    using the function do_deploy
    """
    if exists(archive_path) is False:
        return False

    try:
        start = archive_path.find("web_static")
        end = archive_path.find(".tgz")
        # Getting filename withouth extension
        filename_woe = archive_path[start:end]
        # Getting filename with extension
        filename_we = archive_path[start:]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(filename_woe))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename_we, filename_woe))
        run("rm /tmp/{}".format(filename_we))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_sta\
tic/releases/{}/".format(filename_woe, filename_woe))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(filename_woe))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename_woe))
        return True
    except Exception:
        return False


def deploy():
    """Fabric script that creates and distributes an archive
    to your web servers, using the function deploy
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
