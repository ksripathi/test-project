#!/bin/sh

status=0
for f in $(find . -name '*test_*.py')
do 
    python "$f"
     if [ $? -ne  0 ];
     then
	 status=1
     fi
done
if [ $status -ne 1 ] ;
then
    exit 0
else
    exit 1
fi
