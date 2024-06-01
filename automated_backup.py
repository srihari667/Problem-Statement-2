import os
import shutil
import paramiko
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Configurations
SOURCE_DIR = '/path/to/source/directory'
BACKUP_DIR = '/path/to/local/backup/directory'
REMOTE_HOST = 'remote.server.com'
REMOTE_USER = 'username'
REMOTE_PASSWORD = 'password'
REMOTE_DIR = '/path/to/remote/backup/directory'

def local_backup():
    try:
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
        
        backup_name = datetime.now().strftime("%Y%m%d%H%M%S") + '_backup'
        backup_path = os.path.join(BACKUP_DIR, backup_name)
        shutil.copytree(SOURCE_DIR, backup_path)
        
        logging.info(f'Local backup successful: {backup_path}')
        return True
    except Exception as e:
        logging.error(f'Local backup failed: {e}')
        return False

def remote_backup():
    try:
        backup_name = datetime.now().strftime("%Y%m%d%H%M%S") + '_backup.tar.gz'
        local_archive = shutil.make_archive(backup_name, 'gztar', SOURCE_DIR)
        
        transport = paramiko.Transport((REMOTE_HOST, 22))
        transport.connect(username=REMOTE_USER, password=REMOTE_PASSWORD)
        
        sftp = paramiko.SFTPClient.from_transport(transport)
        remote_path = os.path.join(REMOTE_DIR, backup_name)
        sftp.put(local_archive, remote_path)
        
        sftp.close()
        transport.close()
        
        logging.info(f'Remote backup successful: {remote_path}')
        return True
    except Exception as e:
        logging.error(f'Remote backup failed: {e}')
        return False

def main():
    if local_backup():
        print("Local backup completed successfully.")
    else:
        print("Local backup failed.")
    
    if remote_backup():
        print("Remote backup completed successfully.")
    else:
        print("Remote backup failed.")

if __name__ == "__main__":
    main()
