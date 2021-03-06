#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Package setup
"""
import os
from setuptools import setup, find_packages

PKG_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

def get_long_description():
    description_files = [f for f in os.listdir(PKG_DIR_PATH) if "readme" in str(f).lower()]
    if not description_files:
        return " "

    with open(description_files[0], encoding="utf-8") as f:
        long_description = f.read()
      
    return long_description

  
def get_script_files():
    script_files = list()

    # executable scripts should be in these directories only
    keywords = ("bin", "script")

    for root, dirs, files in os.walk(PKG_DIR_PATH):
        if str(root).endswith(keywords):

            for exe_file in files:
                exe_path = os.path.join(root, exe_file)
                script_files.append(os.path.relpath(exe_path, PKG_DIR_PATH))

                # TODO: Add logic to check file permissions as well for exe files

    return script_files


def get_dependent_packages():
    """
    check the requirement.txt file on the root directory 
    and parse the packages and dependency links if any
    """
    packages    = list()
    links       = list()

    req_files = [f for f in os.listdir(PKG_DIR_PATH) if "requirements.txt" in str(f).lower()]
    if not req_files:
        return [packages, links]
    
    with open(os.path.join(PKG_DIR_PATH, req_files[0])) as rf:
        requirements = rf.read().splitlines()
    
    if requirements:
        for req in requirements:
            if not req:
                # probably an empty line
                continue

            if str(req).startswith("#"):
                # comment line
                continue
            
            if "git+" in str(req):
                # it's direct dependency for a git project
                # Qt.py-1.1.0

                pkg_info = str(req).split("#egg=")[-1]
                pkg_name, pkg_version = str(pkg_info).split("-")

                packages.append("{}=={}".format(pkg_name, pkg_version))
                links.append(req)
                continue
            
            packages.append(req)

    return [packages, links]



INSTALL_REQUIRE, DEPENDENT_LINKS = get_dependent_packages()


setup(name              = os.path.basename(PKG_DIR_PATH),
      version           = "0.1.0",
      author            = 'Arjun Prasad Namdeo',
      author_email      = 'arjun.namdeo.vfx@gmail.com',
      license           = 'MIT',
      description       = "generic python package for my day to day usage",
      long_description  = get_long_description(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: Human Machine Interfaces',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: User Interfaces',
          'Topic :: System',
          'Topic :: System :: Shells',
          'Topic :: System :: Logging',
          'Topic :: System :: Systems Administration',
          'Topic :: Terminals',
          'Topic :: Utilities'
          ],
      keywords          = "python handy useful",
      packages          = find_packages(exclude=["tests", "contrib", "docs"]),
      
      install_requires  = INSTALL_REQUIRE,
      dependency_links  = DEPENDENT_LINKS,
        
      include_package_data = True,

      scripts           = get_script_files(),
      zip_safe          = False,
      url               = "https://github.com/arjun-namdeo/{}".format(os.path.basename(PKG_DIR_PATH))
    
    )
