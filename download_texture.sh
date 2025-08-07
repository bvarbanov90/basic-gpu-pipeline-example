#!/usr/bin/env bash
# Download a sample texture image for the textured cube example.
# Usage: ./download_texture.sh [url] [output]
# Defaults to a small Creative Commons image and saves to texture.jpg.
set -euo pipefail

url=${1:-https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/JPEG_example_flower.jpg/256px-JPEG_example_flower.jpg}
output=${2:-texture.jpg}

curl -L "$url" -o "$output"
echo "Texture saved to $output"
