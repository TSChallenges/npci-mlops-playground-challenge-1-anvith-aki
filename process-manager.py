import os
import psutil
import time

def get_top_cpu_processes(sort_by='cpu', limit=5):

    print("\nTop 5 CPU Processes by usage")
    print("------------------------------------------------------------------")
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
        processes.append(proc.info)
    processes = sorted(processes, key=lambda p: p['cpu_percent'], reverse=True)
    for proc in processes[:5]:
        print(f"PID: {proc['pid']}, Name: {proc['name']}, CPU: {proc['cpu_percent']}%")


def get_top_mem_processes(sort_by='mem', limit=5):
    
    print("\nTop 5 Memory Processes by usage")
    print("------------------------------------------------------------------")
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        processes.append(proc.info)
    processes = sorted(processes, key=lambda p: p['memory_percent'], reverse=True)
    for proc in processes[:5]:
        print(f"PID: {proc['pid']}, Name: {proc['name']}, Memory: {proc['memory_percent']:.2f}%")

def get_process_info():
    pid = input("Enter the PID of the process: ")
    try:
        pid = int(pid)
        process = psutil.Process(pid)
        print(f"\nDetails for PID {pid}:")
        print(f"Name: {process.name()}")
        print(f"Status: {process.status()}")
        print(f"CPU Usage: {process.cpu_percent(interval=1.0)}%")
        print(f"Memory Usage: {process.memory_percent():.2f}%")
        print(f"Threads: {process.num_threads()}")
        print(f"Started At: {time.ctime(process.create_time())}")
    except ValueError:
        print("Invalid input! Please enter a number.")
    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid}.")

def search_process():
    name = input("Enter the name of the process to search: ").lower()
    found = False
    for proc in psutil.process_iter(['pid', 'name']):
        if name in proc.info['name'].lower():
            print(f"Found: PID {proc.info['pid']}, Name: {proc.info['name']}")
            found = True
    if not found:
        print(f"No process found with the name '{name}'.")

def kill_process():
    pid = input("Enter the PID of the process to kill: ")
    try:
        pid = int(pid)
        os.kill(pid, 9)  # Signal 9 = SIGKILL
        print(f"Process with PID {pid} has been terminated.")
    except ValueError:
        print("Invalid input! Please enter a number.")
    except ProcessLookupError:
        print(f"No process found with PID {pid}.")
    except PermissionError:
        print(f"Permission denied to kill PID {pid}.")

def monitor_process():
    pid = input("Enter the PID of the process to monitor: ")
    try:
        pid = int(pid)
        process = psutil.Process(pid)
        print(f"\nMonitoring PID {pid} (Press Ctrl+C to stop):")
        while True:
            print(f"CPU: {process.cpu_percent(interval=1.0)}%, Memory: {process.memory_percent():.2f}%")
            time.sleep(1)
    except ValueError:
        print("Invalid input! Please enter a number.")
    except psutil.NoSuchProcess:
        print(f"No process found with PID {pid}.")
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

def main():
    while True:
        print ("\n")
        print("1. Print Top 5 CPU Processes by usage ")
        print("2. Print Top 5 Memory Processes by usage ")
        print("3. Get process info by pid / name ")
        print("4. Search for a process by pid / name ")
        print("5. Kill a process by pid / name ")
        print("6. Monitor a process by pid / name ")
        print("7. Exit Process Manager ")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            get_top_cpu_processes()
        elif choice == "2":
            get_top_mem_processes()
        elif choice == "3":
            get_process_info()
        elif choice == "4":
            search_process()
        elif choice == "5":
            kill_process()
        elif choice == "6":
            monitor_process()
        elif choice == "7":
            print("Exiting Process Manager... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()