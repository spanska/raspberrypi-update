#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import fabric.api
import fabric.utils

fabric.api.env.roledefs = {
    'cluster': ['', '']
}


def update():
    """
    update all the rasberrypies
    """

    fabric.utils.puts("mise à jour de la machine %s" % fabric.api.env.host)

    fabric.api.run("sudo apt-get update")
    fabric.api.run("sudo apt-get upgrade -y")
    fabric.api.run("sudo apt-get dist-upgrade -y")

    fabric.api.run("sudo apt-get clean")
    fabric.api.run("sudo apt-get autoclean")

    fabric.api.run("sudo rpi-update")

    fabric.api.run("sudo sync")
    fabric.api.run("sleep 30s")

    fabric.api.run("sudo reboot")
