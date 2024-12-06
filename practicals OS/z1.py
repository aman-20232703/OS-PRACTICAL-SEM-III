# process = [pid,arrival_time,burst_time]

"""def fcfs(process):
    t= 0
    gantt=[]
    completed={}
    process.sort()
    while process != []:
        if process[0][1] >t:
            t+=1
            gantt.append("idle")
            continue
        else:
            processes=process.pop(0)
            pid = processes[0]
            gantt.append(pid)
            t += processes[2]
            # pid = processes[0]
            ct=t
            tt=ct-processes[1]
            wt=tt-processes[2]
            completed[pid]=[ct,tt,wt]
            
    print("gantt chart: /n",gantt)
    print("complete fcfs process/n",completed)
    
if __name__ == "__main__":
    process=[["p1",4,9],["p2",4,5],["p3",2,7],["p4",6,2]]
    fcfs(process)"""
    

"""
def srjf(process):
    t=0
    gantt=[]
    completed={}
    burst_times={}
    for i in process:
        burst_times[i[0]]=i[2]
        
    while process !=[]:
        available=[]
        for p in process:
            if p[1]<=t:
                available.append(p)
                
        if available==[]:
            t+=1
            gantt.append("idle")
            continue
        else:
            available.sort()
            processes=available[0]
            copy_process=available.pop(0)
            
            t+=1
            
            gantt.append(processes[0])
            processes[2]-=1
            process.remove(copy_process)
            
            
            if processes[2]==0:
                pid=processes[0]
                at=processes[1]
                bt=burst_times[pid]
        
                ct=t
                tt=ct-at
                wt=tt-bt
                completed[pid]=[ct,tt,wt]
                continue
            else:
                process.append(processes)
                
    print("gantt chart: /n",gantt)
    print("/n completet srjf: /n",completed)
    
if __name__ == "__main__":
    process=[["p1",4,6],["p2",2,4],["p3",1,3],["p4",5,9]]
    srjf(process)
    """
    
    
"""
def priority(process):
    t=0
    gantt=[]
    completed={}
    while process!=[]:
        available=[]
        for p in process:
            # at = p[2]
            if p[2] <= t:
                available.append(p)
                
        if available==[]:
            t+=1
            gantt.append("idle")
            continue
        else:
            available.sort()
            processes=available[0]
            process.remove(processes)
            
            pid=processes[0]
            gantt.append(pid)
            
            bt=processes[3]
            at=processes[2]
            t+=bt
            ct=t
            tat=ct-at
            wt=tat-bt
            completed[pid]=[ct,tat,wt]
            
    print(gantt)
    print(completed)
    
if __name__ == "__main__":
    process=[[1,"p1",2,0],[4,"p2",8,2],[3,"p3",4,1],[1,"p4",6,3]]
    priority(process)
    """
    
    
    
"""
import os
import stat
import time
def file_details(file_path):
    try:
        file_stat=os.stat(file_path)
        file_owner=(file_stat.st_uid)
        access_permission=stat.filemode(file_stat.st_mode)
        access_time=time.ctime(file_stat.st_atime)
        
        print(f"file :{file_path}")
        print(f"owner :{file_owner}")
        print(f"permission :{access_permission}")
        print(f"time :{access_time}")
        
    except FileNotFoundError:
        print(f"{file_path} does not exit")
    except Exception as e:
        print(f"error :{e} occur")
        
file_path="z1.py"
file_details(file_path)
        """
"""


import shutil
def copy_files(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File {source} copied to {destination} file")
    except IOError as e:
        print(f"Error {e}")
source_file = "C:/Users/lenovo/Downloads/practicals OS/aman.txt"
destination_file = "C:/Users/lenovo/Downloads/practicals OS/New folder"

copy_files(source_file, destination_file)
"""



"""
def sjf_non_preemptive(processes):
    # Sort processes by Arrival Time first, then by Burst Time
    processes.sort(key=lambda x: (x[1], x[0]))  # Sort by Arrival Time, then by Burst Time
    
    n = len(processes)  # Number of processes
    t = 0  # Current time (time tracker)
    gantt = []  # Gantt chart to store the order of process execution
    completed = {}  # To store completion time, turnaround time, and waiting time for each process
    
    waiting_times = []  # To store waiting times for calculating average waiting time
    turnaround_times = []  # To store turnaround times for calculating average turnaround time
    
    while processes:
        # Select the processes that have arrived by current time (t)
        available = [p for p in processes if p[1] <= t]
        
        if not available:
            t += 1  # If no processes are available, increment time (idle)
            gantt.append("Idle")
            continue
        
        # Sort the available processes by their burst time
        available.sort(key=lambda x: x[0])  # Sort by burst time (SJF)
        
        # Select the process with the shortest burst time
        current_process = available[0]
        processes.remove(current_process)  # Remove the selected process from the list
        
        # Execute the selected process (add its burst time to current time)
        t += current_process[0]  # Increase time by the burst time of the selected process
        gantt.append(current_process[2])  # Add the process ID to Gantt chart
        
        # Calculate Completion Time, Turnaround Time, and Waiting Time
        ct = t  # Completion time is the current time after executing the process
        at = current_process[1]  # Arrival time of the process
        bt = current_process[0]  # Burst time of the process
        
        tt = ct - at  # Turnaround time
        wt = tt - bt  # Waiting time
        
        # Store the process details (completion time, turnaround time, waiting time)
        completed[current_process[2]] = [ct, tt, wt]
        
        # Store waiting and turnaround times for average calculation
        waiting_times.append(wt)
        turnaround_times.append(tt)
    
    # Calculate the average waiting time and average turnaround time
    avg_waiting_time = sum(waiting_times) / n
    avg_turnaround_time = sum(turnaround_times) / n
    
    # Output the Gantt chart and process completion details
    print("Gantt Chart:", gantt)
    print("\nCompleted Processes:" ,completed)
    for pid, details in completed.items():
        print(f"Process {pid}: Completion Time = {details[0]}, Turnaround Time = {details[1]}, Waiting Time = {details[2]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")


if __name__ == "__main__":
    # Process format: [Burst Time, Arrival Time, Process ID]
    processes = [
        [6, 2, "p1"],  # Process p1: Burst Time = 6, Arrival Time = 2
        [2, 5, "p2"],  # Process p2: Burst Time = 8, Arrival Time = 1
        [8, 1, "p3"],  # Process p3: Burst Time = 7, Arrival Time = 3
        [3, 0, "p4"],  # Process p4: Burst Time = 3, Arrival Time = 0
        # [4, 4, "p5"]   # Process p5: Burst Time = 4, Arrival Time = 4
    ]
    
    sjf_non_preemptive(processes)
"""

#SJF NON-PREEMPTIVE SCHEDULING
#PROCESS = [burt_time,arrival_time,pid]

def sjf(process):
    t = 0
    gantt = []
    completed = {}
    while process != []:
        available = []
        for p in process:
            if p[1] <= t:
                available.append(p)

        if available == []:
            t += 1
            gantt.append("Idle")
            continue
        else:
            available.sort()
            processes = available[0]
            process.remove(processes)
            
            t += processes[0]
            
            pid=processes[2]
            gantt.append(pid)

            pid = processes[2]
            at = processes[1]
            bt = processes[0]
        
            ct = t
            tt = ct - at
            wt = tt - bt
            completed[pid] = [ct,tt,wt]

    print(gantt)
    print(completed)
    for pid,details in completed.items():
        print(f"process {pid}: CT= {details[0]}, TAT= {details[0]}, WT= {details[0]}")
                

if __name__ == "__main__":
    process = [[3,1,"p1"],[4,2,"p2"],[2,1,"p3"],[4,4,"p4"]]
    sjf(process)
    




