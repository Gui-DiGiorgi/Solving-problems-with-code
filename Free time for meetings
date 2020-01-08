# Inspired by https://www.youtube.com/watch?v=3Q_oYDQ2whs

# format for a and b => [["10:30","11:30"],["13:00","14:30"],["16:00","17:30"],["09:00","18:30"]]
# busy times throughout the day (ex: ["10:30","11:30"], that is, busy time from 10:30 to 11:30) and 
# their max start and end time for the day for meetings is at the end (ex: ["09:00","18:30"], that is 
# the person is free starting at 09:00, but no more meetings past 18:30)

# Before watching the full interview:

def times(hue):
    # this turns the busy times into the times of the day they are free
    hue_plus = []
    for i in hue:
        for j in i:
            hue_plus.append(j)
    hue_plus.sort()
    hue_plus_plus = []
    for i in range((int(len(hue_plus)/2))):
        hue_plus_plus.append([hue_plus[2*i],hue_plus[2*i+1]])
    return hue_plus_plus

def clear_times(a,b):
    a_plus = times(a) # see function times
    b_plus = times(b)
    
    # this part see is a start or finish of the first list free time is between or included in any of the the other list free times,
    # if it is, it compares the start and end times to set where both are free 
    # and add that to the possible meetings time (time_plus) if it's not there already
    
    time_plus = []
    
    for i in a_plus:
        for j in b_plus:
            member = [max(i[0],j[0]),min(i[1],j[1])]
            if j[0]<=i[0]<=j[1]:
                if (max(i[0],j[0]) != min(i[1],j[1])) and member not in time_plus:
                    time_plus.append([max(i[0],j[0]),min(i[1],j[1])])
            if j[0]<=i[1]<=j[1]:
                if max(i[0],j[0]) != min(i[1],j[1]) and member not in time_plus:
                    time_plus.append([max(i[0],j[0]),min(i[1],j[1])])

    return time_plus
    

# After watching the full interview:

def meeting_time(a,b):
    
    a_bound = a[len(a)-1]
    a.remove(a_bound)
    b_bound = b[len(b)-1]
    b.remove(b_bound)

    all_time = []
    for i in a:
        all_time.append(i)
    for i in b:
        all_time.append(i)

    all_time.sort()

    n = 0

    while n == 0:
        for i in range(len(all_time)):
            if i != len(all_time)-1:
                if all_time[i][1]>=all_time[i+1][0]:
                    fail = [True,i]
                    break
            else:
                fail = [False,0]
        if fail[0]:
            all_time[fail[1]][1] = all_time[fail[1]+1][1]
            all_time.remove(all_time[fail[1]+1])
        else:
            n = 1

    start_time = max(a_bound[0],b_bound[0])
    finish_time = min(a_bound[1],b_bound[1])

    free_times = []

    for i in range(len(all_time)-1):
        free_times.append([all_time[i][1],all_time[i+1][0]])

    if start_time<all_time[0][0]:
        free_times.append([start_time,all_time[0][0]])

    if all_time[len(all_time)-1][1]<finish_time:
        free_times.append([all_time[len(all_time)-1][1],finish_time])

    return free_times
