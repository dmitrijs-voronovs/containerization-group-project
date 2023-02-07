#!/bin/bash

# assign version to the first argument or default to 'latest'
version=$1
[ -z "$version" ] && version=latest

# name=localhost:32000/fe:$version
name=dmitrylv/todo-fe:$version

echo building $name


cd /mnt/c/Users/Dmitrijs/Documents/myDocs/masters/courses/containerization/FE
docker build . -t $name
docker push $name