#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""
from os.path import exists
from fabric.api import put, run, env
env.hosts = ['35.196.20.175', '52.23.183.91']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Fabric script that distributes an archive to your web servers,
    using the function do_deploy
    """
    if exists(archive_path) is False:
        return False

    start = archive_path.find("web_static")
    end = archive_path.find(".tgz")
    # Getting filename withouth extension
    filename_woe = archive_path[start:end]
    # Getting filename with extension
    filename_we = archive_path[start:]

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(filename_woe))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename_we, filename_woe))
        run("rm /tmp/{}".format(filename_we))
        run("sudo mv /data/web_static/releases/{}/web_static/* /data/web_sta\
tic/releases/{}/".format(filename_woe, filename_woe))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(filename_woe))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename_woe))
        return True
    except Exception:
        return False
