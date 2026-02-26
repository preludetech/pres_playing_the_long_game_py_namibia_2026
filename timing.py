timing = """
# intro 

intro 4:30

# chapter 1 

eng 10:23


# ch 2

t 12:00

ch3 8:00
ep 4:00
"""



def parse_time(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

total_seconds = 0
for line in timing.strip().split('\n'):
    line = line.strip() 
    if not line:
        continue
    if line.startswith('#'):
        continue
    if line.strip():
        time_part = line.split()[-1]
        total_seconds += parse_time(time_part)

total_minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

print(f"total time = {total_minutes}:{remaining_seconds:02d}")