DELETE_MODE=true

printf "\nLooking for EC2 instances\n"
printf	"*********************************************************************\n"
ID_LIST1=$(aws ec2 describe-instances --filters Name=instance-state-name,Values=running,stopped | grep InstanceId | awk '{printf "%s" , $2}')
ID_LIST2=${ID_LIST1//\"} #Get rid of double quotes
ID_LIST3=${ID_LIST2//\,/ } #Replace comma with a space
if [ "x$ID_LIST3" = "x" ]; then
	printf "No instances found to be terminated\n"
else
	printf "Terminating instance $ID_LIST3"
	if [ "$DELETE_MODE" = true ]; then
		aws ec2 terminate-instances --instance-ids $ID_LIST3
		echo "Done! "
	else
		echo " Skiped "
	fi
fi
