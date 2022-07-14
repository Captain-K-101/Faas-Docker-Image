#!/bin/sh -l

echo "First number to add is $1"
echo "Second number to add is $2"
let result=$1+$2
echo "$1 plus $2 equals $result"