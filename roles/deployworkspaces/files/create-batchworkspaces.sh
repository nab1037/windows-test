#!/bin/bash

counter=0
for i in $(ls payload/*.json);
do
  ((counter++))
  aws workspaces create-workspaces --cli-input-json  file://$i --region us-east-1
  if [ $counter -gt 22 ]
  then 
    counter=0
    sleep 32m
  fi
done
