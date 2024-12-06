#SRJF OR SRTF SCHEDULING ALGORITHM.
#OR
#SJF PREEMPTIVE SCHEDULING
#PROCESS = [burt_time,arrival_time,pid]

def srjf(process):
    t = 0
    gantt = []
    completed = {}
    burst_times = {}
    for i in process:
        burst_times[i[2]] = i[0]  #assign every burst time to their respective process
            #key(process)   #value(burst)
            # burst_times = {"p1": 6, "p2": 2, "p3": 8, "p4": 3, "p5": 4}

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
            copy_process = available.pop(0)
            process.remove(copy_process)
            
            t += processes[0]
            processes[0] -= 1
            
            pid=processes[2]
            gantt.append(pid)

            if processes[0] == 0:
                pid = processes[2]
                at = processes[1]
                bt = burst_times[pid]
            
                ct = t
                tt = ct - at
                wt = tt - bt
                completed[pid] = [ct,tt,wt]
                continue

                
            else:
                process.append(processes)
    print(gantt)
    print(completed)
    for pid,details in completed.items():
        print(f"process {pid}: CT= {details[0]}, TAT= {details[0]}, WT= {details[0]}")
                

if __name__ == "__main__":
    process = [[5,0,"p1"],[3,1,"p2"],[4,2,"p3"],[1,4,"p4"]]
    srjf(process)
    



