# You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

# Return this maximum sum.

def maxTwoEvents( events) -> int:
    sorted_array = sorted(events, key=lambda x: (x[0]))
    sortedBasedOnValue = sorted(events, key=lambda x:(x[2]))
    maxV=sortedBasedOnValue[-1][2]
    myEvents = []
    print(sorted_array)
    for i in range(len(events)):
        event1=sorted_array[i]
        for j in range(i+1, len(events)):
            event2 = sorted_array[j]
            if(event2[0]>event1[1] and event1[2]+event2[2]>=maxV ):
                myEvents.append(event1[2]+event2[2])
                

    if(len(myEvents)==0):
        return maxV
    s=sorted(myEvents)
    
    return s[-1]

e=[[1,5,3],[1,5,1],[6,6,5]]

answer= maxTwoEvents(e)
print("ANSWER",answer)