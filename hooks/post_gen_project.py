"""Define hooks to be run after project generation."""

import subprocess


def create_apps():
    subprocess.run("./scripts/init.sh")


create_apps()
