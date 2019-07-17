#!/bin/bash

counter=0
for i in $(ls payload/*.json);
do
  ((counter++))
  aws workspaces create-workspaces --cli-input-json  file://$i
  if [ $counter -gt 3 ]
  then 
    counter=0
    sleep 1m
  fi
done
