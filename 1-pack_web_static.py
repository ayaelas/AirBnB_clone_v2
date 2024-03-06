script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates .tgz archive"""
    try:
        datetim = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        fil = "versions/web_static_{}.tgz".format(datetim)
        local("tar -cvzf {} web_static".format(fil))
        return fil
    except:
        return None
