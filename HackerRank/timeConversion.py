# To conver 12 hrs to 24 hrs 
# In case of PM lets say 1PM in 12 hrs , so in 24 hrs it will be 1+12=13hrs
# For times in the AM period, 12 AM is the only case that needs conversion to 0. All other AM hours (from 01 to 11) remain unchanged in the 24-hour format.



s = "12:05:45AM"
am_pm = s[-2:]
time = s[:-2].strip()
time_part=time.split(':')
hrs=int(time_part[0])
min=int(time_part[1])
sec=int(time_part[2]) if len(time_part) > 2 else 0

if am_pm == 'PM':
    if hrs != 12:
        hrs=hrs+12
elif am_pm == 'AM':
    if hrs == 12:
        hrs =0
        
hrs=f"{hrs:02}"
min=f"{min:02}"
sec=f"{sec:02}"

final=f"{hrs}:{min}:{sec}"                

print(final)    

