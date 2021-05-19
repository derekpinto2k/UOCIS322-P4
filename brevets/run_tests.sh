#!/bin/bash

for t in tests/*.py
do
    nosetests $t
done
