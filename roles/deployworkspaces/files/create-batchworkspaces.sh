#!/bin/bash

for i in $(ls payload/*.json)
do
  # processing workspaces payload files 
  aws workspaces create-workspaces --cli-input-json  file://$i
  #sleep 33m
done