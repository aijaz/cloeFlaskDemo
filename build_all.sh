#!/bin/bash

docker-remove-all.sh
docker network rm aijaz_network

pushd flask || exit
./build.sh
popd || exit

pushd nginx || exit
./build.sh
popd || exit

pushd postgres || exit
./build.sh
popd || exit

pushd ubuntu || exit
./build.sh
popd || exit