from datetime import datetime, time, timedelta

print(datetime.now() + datetime.now()+timedelta(minutes="20"))

startTime = "4pm"
endTime = "10pm"

turnAroundTime = "20min"

# # therefore the (10-4)*60 mins get divided into slots of 20

# numOfSlots = int((endTime-startTime)/turnAroundTime)
# slots = [0 for x in range(numOfSlots)]
# def todayIsPackedUp(slots):
#     return 0 not in slots
# def availableAppointments(slots, startTime, endTime, turnAroundTime):
#     if(todayIsPackedUp(slots)):
#         return False
#     numOfSlots = int((endTime-startTime)/turnAroundTime)

    
#     for i in range(numOfSlots):
#         pass        
    
# def main():
#     pass

#     # get todays slots

