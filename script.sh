#!/bin/bash
for I in {1..20}
do
if [ $(expr $I % 2) -eq 0 ]
then
echo "$I is even"
fi
done
