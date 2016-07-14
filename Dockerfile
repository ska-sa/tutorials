FROM jupyter/scipy-notebook

MAINTAINER Lindsay Magnus <lindsay@ska.ac.za>

USER root

RUN apt-get -y update && apt-get install -y hdf5-tools

USER $NB_USER

RUN mkdir -p $HOME/nb_root 

COPY . $HOME/nb_root

USER root 

RUN chown -R $NB_USER:users /home/$NB_USER

USER $NB_USER

WORKDIR $HOME/nb_root 

