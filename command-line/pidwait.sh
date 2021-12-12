# !/bin/bash

pidwait(){
	while :
	do
	kill -0 $1
	if [ $? -eq 1 ]
	then
	    break
	fi
	sleep 1
	done
}

pidwait "$1"
