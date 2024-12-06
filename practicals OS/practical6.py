#FCFS SCHEDULING ALGORITHM.
#PROCESS = [PID,ARRIVAL_TIME,BURST_TIME].

def fcfs(process):
    t = 0
    gantt = []
    completed = {}
    while process != []:
        if process[0][1] > t:
            t += 1
            gantt.append("idle")
            continue
        else:
            process.sort()
            processes = process.pop(0)
            
            pid = processes[0]
            gantt.append(pid)
            
            t += processes[2]
            ct = t
            tt = ct-processes[1]
            wt = tt-processes[2]
            completed[pid] = [ct,tt,wt]

    print("Gantt Chart:\n",gantt)
    print("\n Complete FSFC Process:\n", completed)
    for pid,details in completed.items():
        print(f"process {pid}: CT= {details[0]}, TAT= {details[1]}, WT= {details[2]}")
    


if __name__ == "__main__":
    process = [["p1",0,2],["p2",1,2],["p3",5,3],["p4",6,4]]
    fcfs(process)