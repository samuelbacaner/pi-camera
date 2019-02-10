# pi-camera

# usage

start container (and recording):
docker run -d --privileged -v /opt/vc/lib:/opt/vc/lib -v ~/data:/data --name <container-name> <image-name>

stop recording (and container):
docker exec <container-name> kill -10 1
