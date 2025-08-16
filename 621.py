def task_scheduler(tasks, n ):

    freq = {}

    for i in tasks:

        if i not in freq:
            freq[i] = 1 

        else:
            freq[i] += 1 

    freq = dict(sorted(freq.items(),key = lambda item: item[1], reverse=True))
    
    print(f"freq-{freq}")
    scheduler = {}
    res = 0
    while len(freq) > 0 : 
        freq = dict(sorted(freq.items(),key = lambda item: item[1], reverse=True))
        temp = res 
        break_flag = False
        for k ,v in freq.items():
            if v == 0 : 
                del freq[k]
                break_flag = True
                print(f"break loop")
                break
            else:
                if k not in scheduler:
                    res += 1 
                    freq[k] -= 1
                    scheduler[k] = res + n -1
                    print(f"res - {res}, ran due to not being in scheduler")
                    break_flag = True
                    break
                else:
                    if scheduler[k] < res: 
                        res += 1 
                        scheduler[k] = res + n -1 
                        freq[k] -= 1 
                        print(f" res - {res}, ran  being in scheduler")
                        break_flag = True
                        break
        print(f"freq - {freq}, scheduler - {scheduler}")
        if temp == res and break_flag == False and len(freq) >= 0: 
            res += 1 

    return res

tasks = ["A","A","A","B","B","B"]
n = 2 
tasks2 = ["A","C","A","B","D","B"]
n2 = 1 
tasks3 = ["A","A","A", "B","B","B"]
n3 = 3
tasks4 = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
n4 = 2

        
print(task_scheduler(tasks4, n4))
    
