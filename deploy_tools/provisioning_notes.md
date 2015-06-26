Provisioning a new site
======================

## Required packages

* nginx
* Miniconda3 (python 3)
* Git
* conda (pip)

eg, on ubuntu:
sudo apt-get install nginx git

## Miniconda install
* try AWS AMI_ID iniconda3-3.9.1-on-ubuntu-14.04-lts mi-7c6b5314
* or docker:
$ docker search continuumio
$ docker pull continuumio/miniconda
$ docker run -t -i continuumio/miniconda /bin/bash
$ conda info

* or do it manually
$ wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda3.sh
$ bash miniconda3.sh -b
#in the same directory as the environment.yml file
$ conda env create
$ conda list env

* conda environment management
conda env export -n ENVNAME -f environment.yml

source activate ENVNAME
source deactivate ENVNAME

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg: staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg: staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
   └── SITENAME
       ├── database
       ├── source
       ├── static
       └── virtualenv (replaced by /home/username/miniconda3/)


