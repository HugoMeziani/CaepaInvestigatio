FROM debian:jessie

MAINTAINER Kladgs et Totoche

RUN apt-get update   && \
    apt-get install -y  \
    tor                 \
    build-essential     \
    git                 \
    bison               \
    libexif-dev         \
    python              \
    python-dev          \
    python-pip          \
    curl                \
    pkg-config          \
    vim                  

RUN pip install virtualenv

RUN git clone https://github.com/HugoMeziani/CaepaInvestigatio.git
RUN chmod +x CaepaInvestigatio/start.sh
RUN chmod +x CaepaInvestigatio/caepainvestigatio/onionrunner.py

ADD onion_master_list.txt /

CMD cd CaepaInvestigatio ; bash start.sh ; while true; do sleep 2; df -h; done

