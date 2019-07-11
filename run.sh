#!/usr/bin/env bash

set -ex

echo "use conan version: $1"

docker stop speedtest || echo "ok"
docker rm -f speedtest || echo "ok"
docker run -dt --name speedtest conanio/gcc5 /bin/bash

docker exec speedtest pip install conan==$1
docker exec speedtest sudo apt-get update -y
docker exec speedtest sudo apt-get install -y time --no-install-recommends
docker exec speedtest conan remote add bc https://api.bintray.com/conan/bincrafters/public-conan
docker cp conanfile.py speedtest:/conanfile.py

docker exec speedtest time conan create /conanfile.py bincrafters/testing -k
