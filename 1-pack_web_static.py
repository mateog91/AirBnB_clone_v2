#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack
    """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    tgz_name = "web_static_" + date + ".tgz"
    archive_path = local("tar -cvzf versions/{} web_static".format(tgz_name))
    if archive_path.failed:
        return None
    return archive_path
