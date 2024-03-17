#!/bin/bash


show_help() {
    echo "Usage:"
    echo "./dockerhub.sh <REGISTRY>/<REPOSITORY>"
    echo "For example: ./dockerhub.sh sonatype/nexus3"
    echo
    echo "To see which images are available, run:"
    echo "./dockerhub.sh <IMAGE>"
    echo "./dockerhub.sh nexus3"
}

if [ "$1" == "--help" ]; then
    show_help
    exit 0
fi

if [ $# -eq 0 ]; then
    show_help
    exit 0
fi

# For official images:
# REGISTRY is library 
# REPOSITORY is the name of the image

# OTHERWISE, split the image name 
# (e.g. google/cloud-sdk into REGISTRY=google and REPOSITORY=cloud-sdk)


# USAGE: ./dockerhub.sh sonatype/nexus3
# Split iamge at "/"
if [[ ! $1 == */* ]]; then
    IMAGE="$1"
    result=$(curl -s "https://hub.docker.com/api/search/v3/catalog/search?query=$IMAGE")
    echo $result | jq -r '.results[].name'
    exit 0
else
    IFS='/' read -r REGISTRY REPOSITORY <<< "$1"
fi

# REGISTRY=sonatype
# REPOSITORY=nexus3

next_page="https://registry.hub.docker.com/v2/namespaces/$REGISTRY/repositories/$REPOSITORY/tags?page=1&page_size=1000"

while [ "$next_page" != "null" ]
do
    result=$(curl -s "$next_page")
    echo $result | jq -r '.results[].name'
    
    next_page=$(echo $result | jq -r '.next')
done
