# !/bin/bash

count=0
err=0
while true
do
	./rarely-fail.sh 1>/dev/null 2>err.log
	err=$?
	count=$((count+1))
	if [[ $err -eq 1 ]]; then
	    break
	fi
done
cat err.log
echo "The script ran $count times."




