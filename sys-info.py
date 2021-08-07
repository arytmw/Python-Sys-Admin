mport platform
import psutil #pip3.6 install psutil
import humanize #pip3.6 install humanize
import time
import subprocess

print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"Name: {uname.node}")
print(f"System: {uname.system}")
print(f"Kernel: {uname.release}")
print(f"Architecture: {uname.machine}")
boot_time_timestamp = psutil.boot_time()
print(f"Boot time: {time.ctime(boot_time_timestamp)}")

print("="*40, "CPU Information", "="*40)
print(f"Physical Cores: {psutil.cpu_count(logical=False)}")
print(f"Total Cores: {psutil.cpu_count(logical=True)}")
cpufreq = psutil.cpu_freq()
print(f"Current Frequency: {cpufreq.current} Mhz")
print(f"Total CPU usage: {psutil.cpu_percent()} %")

print("="*40, "Memory Information", "="*40)
sysmem = psutil.virtual_memory()
print(f"Total Memory: {humanize.naturalsize(sysmem.total)}")
print(f"Available Memory: {sysmem.available}")
print(f"Used Memory: {sysmem.used}")
print(f"Total Memory Usage: {sysmem.percent} %")

print("="*40, "Swap Information", "="*40)
swap = psutil.swap_memory()
print(f"Total Swap: {swap.total}")
print(f"Available Swap: {swap.free}")
print(f"Used Swap: {swap.used}")
print(f"Percentage Usage: {swap.percent} %")

print("="*40, "Disk Information", "="*40)
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"Device: {partition.device}")
    print(f"Mountpoint: {partition.mountpoint}")
    print(f"Filesystem: {partition.fstype}")
    partition_usage = psutil.disk_usage(partition.mountpoint)
    print(f"Total Size: {partition_usage.total}")
    print(f"Used Size: {partition_usage.used}")
    print(f"Available Size: {partition_usage.free}")
    print(f"Percentage Usage: {partition_usage.percent} %")
    print("-----")

print("="*40, "Network Information", "="*40)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    print(f"Interface Name: {interface_name}")
    for address in interface_addresses:
        if str(address.family) == "AddressFamily.AF_INET":
            print(f"IP Address: {address.address}")
            print(f"Netmask: {address.netmask}")
            print(f"Broadcast: {address.broadcast}")
            print("-----")

print("="*40, "Process Information", "="*40)
#for proc in psutil.process_iter():
#    try:
#        processname = proc.name()
#        processID = proc.pid
#        print(f"{processname} : {processID}")
#    except psutil.AccessDenied:
#        pass
command = ['ps','-eo','pid,ppid,cmd,%mem,%cpu','--sort=-%mem','| head']
#cmd = subprocess.run(command)
#print(cmd)
process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
stdout_list = process.communicate()[0]
print(stdout_list.decode())
