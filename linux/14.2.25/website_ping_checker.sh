#!/bin/bash

read -p 'enter website for pinging: ' ip
echo
echo 'pinging website -' $ip 
echo '________________________________________________________'
echo

while true; do

	# creating variables for pinging and formatting
        ping_site=$(ping -c 1 $ip | awk -F'time=' '{print $2}' | awk '{print $1}')
        rounded=$(printf '%.0f' $ping_site)

	# showing ping
        echo "ping:" $rounded "ms"
        sleep 1
	echo

	# creating condition for ping more than 100
        if [ $rounded -ge 100 ]; then
		echo "ping >= 100 ms"
		echo 'pinging again...'
		echo
		sleep 1
		count=0
		
		# creating cycle for 3 attempts pinging of website
                for i in {1..3}; do
			
			ping_site=$(ping -c 1 $ip | awk -F'time=' '{print $2}' | awk '{print $1}')
			rounded=$(printf '%.0f' $ping_site)

			echo "ping:" $rounded "ms"
			sleep 1
			echo

                        if [ $rounded -ge 100 ]; then
                                echo 'ping >= 100 ms'                           
				echo 'pinging again...'
				echo
				sleep 1
				count=$(($count+1))

			# creating condition if website not answering                   
			elif [ ! $ping_site ]; then
				sleep 1
				echo 'server not answering'
				echo
				break
			fi
			
				
			# creating error file and entering ping errors and date of high ping
			if [ $count -eq 3 ]; then
				sleep 1
				echo "checking if file "ping_errors.txt" exist"
				echo
				sleep 1				

				if [ -f ./ping_errors.txt ]; then
					echo 'file exist'
					echo
				else
					sleep 1
					echo "creating 'ping_errors.txt' file"
					touch ping_errors.txt
					sleep 1
				fi
				
				echo "entering info error in 'ping_errors.txt' file"
				echo 'ping too high:' $rounded "ms" >> ping_errors.txt
				date >> ping_errors.txt
				echo >> ping_errors.txt
				sleep 2
				echo
				echo 'done'
				sleep 1
				echo
			fi
                done
        fi
done
