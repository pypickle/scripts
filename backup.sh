# /bin/bash

# First argument is the device ID
read -p "Enter mass storage device name: " DEVICE

DIR="/media/$USER/$DEVICE"
if [ -d "$DIR" ]; then
	# Back up take into consideration the PC Name + Backup date
	BACKUP_DIR="$DIR/backups/$(uname -n)_$(date +%d_%m_%Y)"
	if [ ! -d "$BACKUP_DIR" ]; then
		echo "\033[1;33mWARNING\033[0m: \"$BACKUP_DIR\" does not exist. creating ..."
		mkdir -p "$BACKUP_DIR"
		echo "$BACKUP_DIR ... Created."
	fi
	echo "Backing up files to \"$BACKUP_DIR\" ..."
	
	rsync -arz --no-owner --no-group --info=progress2 --exclude 'Trash' --exclude '.local' --exclude 'node_modules' --exclude 'env' --exclude 'logs' --exclude '.env' --exclude 'env' --exclude 'venv' ~/ "$BACKUP_DIR"

else
	echo "\033[1;33mWARNING\033[0m: \"$DIR\" does not exist."
	exit 1
fi
