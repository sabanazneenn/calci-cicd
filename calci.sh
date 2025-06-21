#!/bin/bash

num1=$1
num2=$2
operation=$3

if [ "$operation" == "+" ]; then
    result=$((num1 + num2))
    echo "Result: $result"
elif [ "$operation" = "-" ]; then
    result=$((num1 - num2))
    echo "Result: $result"
elif [ "$operation" = "*" ]; then
    result=$((num1 * num2))
    echo "Result: $result"
elif [ "$operation" = "/" ] ; then
    result=$((num1 / num2))
    echo "Result: $result"	
else
    echo "Invalid operation"
fi

