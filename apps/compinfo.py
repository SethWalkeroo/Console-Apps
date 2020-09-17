import psutil
import GPUtil
import platform
from os import system
from datetime import datetime
from tabulate import tabulate
from welcome import title_card, loading_animation
from colored import fg, bg, attr


class ComputerInformation:

    cold_clr = fg('sky_blue_1')
    hot_clr = fg('red')
    reset = attr('reset')

    def get_size(self, bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    def system_info(self):
        print("="*40, "System Information", "="*40)
        print()
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
        uname = platform.uname()
        print(f"System: {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")

    def cpu_info(self):
        # let's print CPU information
        print("="*40, "CPU Info", "="*40)
        print()
        #cpu temperature
        temperature = psutil.sensors_temperatures()['coretemp'][0].current
        current_temp_c = f"{temperature}°C   "
        current_temp_f = f"{(temperature * 9/5) + 32}°F"
        if temperature <= 45:
            print(f'Current CPU temperature: {self.cold_clr + current_temp_c + current_temp_f + self.reset}')
        else:
            print(f'Current CPU temperature: {self.hot_clr + current_temp_c + current_temp_f + self.reset}')
        # number of cores
        print("Physical cores:", psutil.cpu_count(logical=False))
        print("Total cores:", psutil.cpu_count(logical=True))
        # CPU frequencies
        cpufreq = psutil.cpu_freq()
        print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
        # CPU usage
        print("CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {percentage}%")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")

    def memory_info(self):
        # Memory Information
        print("="*40, "Memory Information", "="*40)
        print()
        # get the memory details
        svmem = psutil.virtual_memory()
        print(f"Total: {self.get_size(svmem.total)}")
        print(f"Available: {self.get_size(svmem.available)}")
        print(f"Used: {self.get_size(svmem.used)}")
        print(f"Percentage: {svmem.percent}%")
        print("="*20, "SWAP", "="*20)
        # get the swap memory details (if exists)
        swap = psutil.swap_memory()
        print(f"Total: {self.get_size(swap.total)}")
        print(f"Free: {self.get_size(swap.free)}")
        print(f"Used: {self.get_size(swap.used)}")
        print(f"Percentage: {swap.percent}%")

    def disk_info(self):
        # Disk Information
        print("="*40, "Disk Information", "="*40)
        print()
        print("Partitions and Usage:")
        # get all disk partitions
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"=== Device: {partition.device} ===")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  File system type: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                # this can be catched due to the disk that
                # isn't ready
                continue
            print(f"  Total Size: {self.get_size(partition_usage.total)}")
            print(f"  Used: {self.get_size(partition_usage.used)}")
            print(f"  Free: {self.get_size(partition_usage.free)}")
            print(f"  Percentage: {partition_usage.percent}%")
        # get IO statistics since boot
        disk_io = psutil.disk_io_counters()
        print(f"Total read: {self.get_size(disk_io.read_bytes)}")
        print(f"Total write: {self.get_size(disk_io.write_bytes)}")

    def network_info(self):
        # Network information
        print("="*40, "Network Information", "="*40)
        print()
        # get all network interfaces (virtual and physical)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"=== Interface: {interface_name} ===")
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  IP Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast MAC: {address.broadcast}")

    def io_stats(self):
        # get IO statistics since boot
        net_io = psutil.net_io_counters()
        print(f"Total Bytes Sent: {self.get_size(net_io.bytes_sent)}")
        print(f"Total Bytes Received: {self.get_size(net_io.bytes_recv)}")

    def gpu_info(self):
        # GPU information
        import GPUtil
        from tabulate import tabulate
        print("="*40, "GPU Details", "="*40)
        print()
        gpus = GPUtil.getGPUs()
        list_gpus = []
        for gpu in gpus:
            # get the GPU id
            gpu_id = gpu.id
            # name of GPU
            gpu_name = gpu.name
            # get % percentage of GPU usage of that GPU
            gpu_load = f"{gpu.load*100}%"
            # get free memory in MB format
            gpu_free_memory = f"{gpu.memoryFree}MB"
            # get used memory
            gpu_used_memory = f"{gpu.memoryUsed}MB"
            # get total memory
            gpu_total_memory = f"{gpu.memoryTotal}MB"
            # get GPU temperature in Celsius
            if gpu.temperature < 85:
                gpu_temperature = self.cold_clr + f"{gpu.temperature} °C" + self.reset
            else:
                gpu_temperature = self.hot_clr + f"{gpu.temperature} °C" + self.reset
            gpu_uuid = gpu.uuid
            list_gpus.append((
                gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
                gpu_total_memory, gpu_temperature, gpu_uuid
            ))

        print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                   "temperature", "uuid")))


    def main(self):
        system('clear')
        info_functions = {'1':self.system_info,
                     '2':self.cpu_info, '3':self.memory_info,
                     '4':self.disk_info, '5':self.network_info,
                     '6':self.gpu_info, '7':self.io_stats}

        display_dict = {'1':'system information',
                     '2':'CPU information', '3':'memory information',
                     '4':'disk information', '5':'network information',
                     '6':'GPU information', '7':'io statistics'}
        while True:
            title_card('ol,System info,CPU info,Memory info,Disk info,Network info,GPU info,IO stats', thickness=1)
            print('Type "exit" to exit')
            print()
            choice = input('What computer info do you need? (enter number): ')
            if choice in info_functions:
                loading_animation(f'loading {display_dict[choice]}', time=1)
                info_functions[choice]()
                print()
                print()
                menu = input('Hit "enter" to return back to the menu... ')
                loading_animation('returning to menu...', time=1)
            elif choice == 'exit':
                break
            else:
                loading_animation('ERROR: that was not in the list. Try again', time=2)
        loading_animation('exiting... ', time=2)

if __name__ == '__main__':
    computer_info = ComputerInformation()
    computer_info.main()
