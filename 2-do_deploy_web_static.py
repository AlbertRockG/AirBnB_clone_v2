#!/usr/bin/python3
"""Fabfile to distribute an archive to a web server."""
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        False, if the file doen't exist at the given archive_path,
        True, otherwise.
    """
    if os.path.isfile(archive_path) is False:
        return False
    myfile = archive_path.split("/")[-1]
    name = myfile.split(".")[0]

    if put(archive_path, "/tmp/{}/\
           ".format(myfile)).failed is True:
        return False
    
    if run("mkdir -p /data/web_static/releases/{}/\
           ".format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/\
           ".format(myfile, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(myfile)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/\
        web_static".format(name)).failed is True:
        return False
    if run("ln -sf /data/web_static/releases/{}/\
        /data/web_static/current".format(name)).failed is True:
        return False
    return True