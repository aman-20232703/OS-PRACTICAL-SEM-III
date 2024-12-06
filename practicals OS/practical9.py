#Priority CPU Scheduling Non Preemptive.
#Process = [Priority,pid,burst_time,arrival_time]

def priority(process):
    t = 0
    gantt= []
    completed = {}
    while process != []:
        available = []
        for p in process:
            # at = p[2]
            if p[2] <= t:
                available.append(p)

        if available == []:
            t += 1
            gantt.append("Idle")
            continue
        else:
            available.sort()
            processes = available[0]
            process.remove(processes)
            
            pid = processes[1]
            gantt.append(pid)
            
            bt = processes[3]
            at = processes[2]
            t += bt
            ct = t
            tt = ct - at
            wt = tt - bt
            completed[pid] = [ct,tt,wt]
    print("Gantt Chart:\n",gantt)
    print("\n Complete Priority Process:\n", completed)
    for pid,details in completed.items():
        print(f"process {pid}: CT= {details[0]}, TAT= {details[1]}, WT= {details[2]}")




if __name__== "__main__":
    #process = [[5,"p1",6,2],[4,"p2",2,5],[1,"p3",0,3],[2,"p4",1,5]]
    #process = [[2,"p1",11,0],[0,"p2",28,5],[3,"p3",2,12],[1,"p4",10,2],[4,"p5",16,9]]
    process = [[10,"p0",0,5],[20,"p1",1,4],[30,"p2",2,2],[40,"p3",4,1]]
    priority(process)