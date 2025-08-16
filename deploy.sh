NAME_CONTAINER="api-flask-grupo12"
NAME_IMAGE="api-flask-grupo12"
PORT_EXPOSE=5001

docker build -t "$NAME_IMAGE" .
echo 'Compilado correctamente'

docker rm -f "$NAME_CONTAINER"

docker run -e PYTHONUNBUFFERED=1 --restart=unless-stopped --name "$NAME_CONTAINER" \
    -p "$PORT_EXPOSE":5001 -d "$NAME_IMAGE"
echo 'Successfull service'