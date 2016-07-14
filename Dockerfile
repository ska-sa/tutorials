<<<<<<< HEAD
FROM jupyter/scipy-notebook

MAINTAINER Lindsay Magnus <lindsay@ska.ac.za>

USER root

RUN apt-get -y update && apt-get install -y hdf5-tools

USER $NB_USER

RUN mkdir -p $HOME/nb_root 

ADD . $HOME/nb_root

WORKDIR $HOME/nb_root 

=======
FROM ipython/scipyserver

MAINTAINER Lindsay Magnus <lindsay@ska.ac.za>

RUN apt-get -y update && apt-get install -y hdf5-tools

RUN mkdir /nb_root 

ADD . /nb_root

WORKDIR /nb_root 

CMD ipython2 notebook --no-browser --port 8888 --ip=* 
>>>>>>> e9884ae364e8fdd9c7d53dabf0bc9b5bd87085c4
