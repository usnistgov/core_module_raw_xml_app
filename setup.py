""" Setup core raw xml module app
"""

from os import chdir, pardir
from os.path import join, exists, dirname, normpath, abspath

from setuptools import find_packages, setup

reqs_default = join(dirname(__file__), "requirements.txt")
reqs_core = join(dirname(__file__), "requirements.core.txt")
required = []

if exists(reqs_default):
    with open(reqs_default) as f:
        required += f.read().splitlines()

if exists(reqs_core):
    with open(reqs_core) as f:
        required += f.read().splitlines()

with open(join(dirname(__file__), "README.rst")) as f:
    long_desc = f.read()

# Allow setup.py to be run from any path
chdir(normpath(join(abspath(__file__), pardir)))

setup(
    name="core_module_raw_xml_app",
    version="2.17.0",
    description="Raw xml module for the parser core project",
    long_description=long_desc,
    author="NIST IT Lab",
    author_email="itl_inquiries@nist.gov",
    url="https://github.com/usnistgov/core_module_raw_xml_app",
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
)
