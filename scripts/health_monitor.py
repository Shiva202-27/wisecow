import psutil
import datetime

LOG_FILE = "system_health.log"

CPU_LIMIT = 80
MEM_LIMIT = 80
DISK_LIMIT = 80


def write_log(message):
    with open(LOG_FILE, "a") as file:
        file.write(
            f"{datetime.datetime.now()} - {message}\n"
        )


cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent


print("System Health Report")
print("--------------------")
print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")
print(f"Disk Usage: {disk}%")


if cpu > CPU_LIMIT:
    write_log(f"High CPU Alert: {cpu}%")

if memory > MEM_LIMIT:
    write_log(f"High Memory Alert: {memory}%")

if disk > DISK_LIMIT:
    write_log(f"High Disk Alert: {disk}%")