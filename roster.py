import random

staff = ["Mel","Isaac","Nick","Tina","Shaun","Francois","Ayrton","Natalie","Kelly","James","Warwick"]
monday =[]
tuesday=[]
wednesday=[]
thursday=[]
friday=[]
weekday = []
next_week =[]
stf_week = []

###############  WEEK 1 RANDOMIZE  ####################
Monday = random.sample(staff,5)
weekday.append(Monday)
Tuesday = random.sample(staff,5)
weekday.append(Tuesday)
Wednesday = random.sample(staff,5)
weekday.append(Wednesday)
Thursday = random.sample(staff,5)
weekday.append(Thursday)
Friday = random.sample(staff,5)
weekday.append(Friday)

this_week = (f"Monday :{Monday}\nTuesday :{Tuesday}\nWednesday :{Wednesday}\nThursday :{Thursday}\nFriday :{Friday}")
with open('roster.txt', 'w') as roster:
    roster.write(this_week)
    
###############  WEEK 2 FILLER  ####################
for i in staff:
    if i not in Monday:
        monday.append(i)
for i in staff:
    if i not in Tuesday:
        tuesday.append(i)
for i in staff:
    if i not in Wednesday:
        wednesday.append(i)
for i in staff:
    if i not in Thursday:
        thursday.append(i)
for i in staff:
    if i not in Friday:
        friday.append(i)        

next_week = (f"Monday :{monday}\nTuesday :{tuesday}\nWednesday :{wednesday}\nThursday :{thursday}\nFriday :{friday}")  
with open('roster2.txt', 'w') as roster2:
    roster2.write(next_week)
    
###############  WEEKLY SCHEDULE PER STAFF  ####################
with open('staff.txt', 'w+') as stf_per_week:
    for e in staff:
        stf_per_week.write(f"{e} this week will be working:\n")    
        if e in Monday:
            stf_per_week.write("Monday, ")
        if e in Tuesday:
            stf_per_week.write(f"Tuesday, ")
        if e in Wednesday:
            stf_per_week.write(f"Wednesday, ")
        if e in Thursday:
           stf_per_week.write(f"Thursday, ")
        if e in Friday:
            stf_per_week.write(f"Friday ")  
        stf_per_week.write(f"\nThe following week {e} will be working:\n")
        if e not in Monday:
           stf_per_week.write("Monday, ")
        if e not in Tuesday:
            stf_per_week.write(f"Tuesday, ")
        if e not in Wednesday:
            stf_per_week.write(f"Wednesday, ")
        if e not in Thursday:
            stf_per_week.write(f"Thursday, ")
        if e not in Friday:
            stf_per_week.write(f"Friday ")
        stf_per_week.write("\n\n")