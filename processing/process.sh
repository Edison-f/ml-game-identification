#!/usr/bin/env bash

width=1280
height=720

# Process Images
for file in './processing/input/*'; do
    echo $file
    if identify $file 1> /dev/null 2> /dev/null; then
        echo 'hello'
        out=`sed -e s/\.[a-zA-Z0-9]+$/\.bmp/g <<< "$file"`
        echo $out
        # convert $file $out
    fi
done


# Process Videos
# screenshotCount=10
