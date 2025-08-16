import heapq
def meeting_rooms_iii( meetings, n):

    meetings.sort()
    
    print(meetings)
    res = {i:0 for i in range(n)}

    ongoing_queue = []
    available_rooms = n
    heapq.heappush(ongoing_queue, [meetings[0][1],n - available_rooms ])
    res[0] += 1 

    available_rooms -= 1 
    
    idx = 1
    rooms_availability = {_ : True for _ in range(n)} 
    rooms_availability[0] = False

    print(f" Before Loop - res - {res} , ongoing_queue - {ongoing_queue}")
    while ongoing_queue and idx < len(meetings):

        while len(ongoing_queue) > 0 and ongoing_queue[0][0] <= meetings[idx][0]:

            pop_room = heapq.heappop(ongoing_queue) 
            rooms_availability[pop_room[1]] = True
            available_rooms += 1 

        if available_rooms != 0 : 
            print(f"Ran because rooms were available , idx - {idx} , available_rooms - {available_rooms}")
            print(rooms_availability)
            for k,v in rooms_availability.items():
                
                if v == True:
                    
                    room_to_allot = k

                    heapq.heappush(ongoing_queue, [meetings[idx][1] ,room_to_allot])
                    res[room_to_allot] += 1 
                    available_rooms -= 1 
                    rooms_availability[room_to_allot] = False
                    idx += 1
                    print(f"ongoing_queue - {ongoing_queue} , res - {res}")
                    break
        else: 
             
            print(f"Ran because rooms were not not available., idx - {idx} , available_rooms - {available_rooms}")
            curr_free_room = heapq.heappop(ongoing_queue)
            heapq.heappush(ongoing_queue, [curr_free_room[0] + (meetings[idx][1] - meetings[idx][0]) , curr_free_room[1]])
            res[curr_free_room[1]] += 1 
            idx += 1  
            print(f"ongoing_queue - {ongoing_queue} , res - {res}")

    print(f"res - {res}")
    max_res = 0 

    for k,v in res.items():
        if v > res[max_res]:
            max_res = k 
    return max_res

n = 2 
meetings = [[0,10],[1,5],[2,7],[3,4]]
n1 = 3
meetings1 = [[1,20],[2,10],[3,5],[4,9],[6,8]]
n2 = 2
meetings2 = [[0,10],[1,2],[12,14],[13,15]]
n3 = 4
meetings3 = [[19,20],[14,15],[13,14],[11,20]]

print(meeting_rooms_iii(meetings, n))
print(meeting_rooms_iii(meetings1, n1 ))
print(meeting_rooms_iii(meetings2, n2 ))
print(meeting_rooms_iii(meetings3, n3 ))


    

    

