#!/bin/bash

# script for sorting files of odd and even numbers

temp_dir=/opt/111124-ptm/Klymentii/homeworks/25.2.25/temp/
even_dir=/opt/111124-ptm/Klymentii/homeworks/25.2.25/even_nums/

echo 'checking all files in directory' $temp_dir
sleep 2

echo 'moving files with even number in another folder' $even_dir
sleep 3

for file in $temp_dir/*; do
        filename=$(basename $file)
        if [[ $filename =~ ^[0-9]+$ ]]; then
                if (( $filename % 2 == 0 )); then
                        mv $file $even_dir/$filename
                fi
        fi
done

echo 'done! have a nice day! ;)'
