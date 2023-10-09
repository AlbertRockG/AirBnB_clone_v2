#!/usr/bin/python3
"""Creates and distributes an archive to web servers."""
import os.path
from datetime import datetime
from fabric.api import *


env.user = "ubuntu"
env.hosts =  ["54.209.135.247", "3.90.85.92"]
env.key_filename = "~/.ssh/known_hosts"

def do_pack():
    """Creates a tar gzipped archive of the directory web_static"""
    dt = datetime.utcnow()
    myfile = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                           dt.month,
                                                           dt.day,
                                                           dt.hour,
                                                           dt.minute,
                                                           dt.second)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if (local("tar -cvzf {} web_static".format(myfile)).failed) is True:
        return None
    return myfile

def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        False, if the file doesn't exist at the given archive_path,
        True, otherwise.
    """
    if os.path.isfile(archive_path) is False:
        return False
    myfile = archive_path.split("/")[-1]
    name = myfile.split(".")[0]

    print("New version deployment started at!")
    with cd("/tmp"):
        if put(local_path=archive_path,
                remote_path="{}".format(myfile),
                mirror_local_mode=True, use_sudo=True).failed is True:
            return False
    if run("ls -l /tmp/").failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/\
        ".format(name)).failed is True:
        return False
    if run("tar -xvzf /tmp/{} -C /data/web_static/releases/{}\
        ".format(myfile, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(myfile)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run(
        "rm -rf /data/web_static/releases/{}/web_static/".format(name)
        ).failed is True:
        return False
    if run("ln -sfn /data/web_static/releases/{}/\
        /data/web_static/current".format(name)).failed is True:
            return False
    print("New version deployed!")
    return True


def deploy():
    """Creates and distributes an archive to web servers.
    """
    archive_path = do_pack()
    if os.path.isfile(archive_path) is False:
        return False
    return do_deploy(archive_path)
