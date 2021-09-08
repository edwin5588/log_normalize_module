
###This dockerfile is copied from GenePattern's Example Module repository. All credits go to genepattern.

FROM genepattern/docker-python36:0.4

RUN useradd -ms /bin/bash gpuser
USER gpuser
WORKDIR /home/gpuser

#switch back to root to create dir
USER root
RUN mkdir /Log_Normalize \
    && chown gpuser /Log_Normalize

#switch to non-root before exiting so that we don't run as root on the server, and copy all of the src files into the container.
USER gpuser
COPY src/*.py /Log_Normalize/

RUN python /Log_Normalize/Log_Normalize.py