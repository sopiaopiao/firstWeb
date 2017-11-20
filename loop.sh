#!/bin/bash
set i=0
set j=0
for((i=0;i<10;))
do
        let "j=j+1"
        echo "-------------j is $j -------------------"
done
