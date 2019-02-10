FROM raspbian/stretch

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get upgrade -y
RUN apt-get install -y wget
RUN apt-get install libraspberrypi-bin -y
RUN usermod -a -G video root

# Debugging: install debug library and establish debug port
RUN python3 -m pip install ptvsd==4.2.0
EXPOSE 3000

# Application source
WORKDIR /app
ADD . /app

# Install application dependencies
RUN python3 -m pip install -r requirements.txt

# Allows container to access host firmware. Run container with '-v /opt/vc/lib:/opt/vc/lib' option
ENV LD_LIBRARY_PATH /opt/vc/lib
CMD [ "python3", "-u", "run.py", "--dev" ]

