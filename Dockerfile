FROM python:3-alpine

# Debugging: install debug library and establish debug port
RUN python3 -m pip install ptvsd==4.2.0
EXPOSE 3000

# Application source
WORKDIR /app
ADD . /app

# Install application dependencies
RUN python3 -m pip install -r requirements.txt

CMD [ "python3", "-u", "run.py", "--dev" ]

