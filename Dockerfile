FROM ipython/scipyserver

MAINTAINER Lindsay Magnus <lindsay@ska.ac.za>

RUN mkdir /nb_root 

ADD . /nb_root

WORKDIR /nb_root 

CMD ipython2 notebook --no-browser --port 8888 --ip=* 
