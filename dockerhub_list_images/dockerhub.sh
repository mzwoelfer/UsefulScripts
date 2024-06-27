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

search_image() {
    IMAGE="$1"
    result=$(curl -s "https://hub.docker.com/api/search/v3/catalog/search?query=$IMAGE")
    echo "NAME, ID"
    echo $result | jq -r '.results[] | "\(.name)\t\(.id)"'
}

search_tags() {
    IFS='/' read -r REGISTRY REPOSITORY <<< "$1"
    next_page="https://registry.hub.docker.com/v2/namespaces/$REGISTRY/repositories/$REPOSITORY/tags?page=1&page_size=1000"
    
    while [ "$next_page" != "null" ]
    do
        result=$(curl -s "$next_page")
        echo $result | jq -r '.results[].name'
        
        next_page=$(echo $result | jq -r '.next')
    done
}


if [ "$1" == "--help" ]; then
    show_help
    exit 0
fi

if [ $# -eq 0 ]; then
    show_help
    exit 0
fi

if [[ ! $1 == */* ]]; then
    search_image "$1"
else
    search_tags "$1"
fi
