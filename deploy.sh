# Create a docker network named aijaz_network if one doesn't already exist.
docker network create --driver bridge aijaz_network || true

docker run -d -it --name aijaz_flask_c    \
       -v "$(pwd)"/document_root:/document_root \
       --network aijaz_network \
       aijaz_flask_i
docker run -d -it --name aijaz_nginx_c    \
       -v "$(pwd)"/document_root:/document_root \
       --network aijaz_network \
       -p 80:80 aijaz_nginx_i

docker run -d -it --name aijaz_ubuntu_c  --network aijaz_network aijaz_ubuntu_i


