import psutil
import logging

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80  # in percent
MEMORY_THRESHOLD = 80  # in percent
DISK_THRESHOLD = 80  # in percent

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
    return cpu_usage

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High Memory usage detected: {memory_usage}%')
    return memory_usage

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'High Disk usage detected: {disk_usage}%')
    return disk_usage

def check_running_processes():
    process_count = len(psutil.pids())
    logging.info(f'Running processes: {process_count}')
    return process_count

def main():
    cpu = check_cpu_usage()
    memory = check_memory_usage()
    disk = check_disk_usage()
    processes = check_running_processes()
    
    print(f'CPU Usage: {cpu}%')
    print(f'Memory Usage: {memory}%')
    print(f'Disk Usage: {disk}%')
    print(f'Running Processes: {processes}')

if __name__ == "__main__":
    main()
