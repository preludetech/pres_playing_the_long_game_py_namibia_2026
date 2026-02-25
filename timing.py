timing = """
# intro 

intro 1:20 
me: 3:40

# chapter 1 

ch1_intro: 2:40
ch1_2024: 1:15
deepseek: 2:00
scaling_laws 4:00
gpt5: 4:30

# chapter 2

# ch2_bubble: 4:00

# chapter 3 

ch3 8:44

# chapter 4 
# intro-to-infra: 6:00
# safety 8:00
# cognitive: 1:40
# centaur: 2:05
# Stanford: 1:30
# structure: 2:30
# bubble: 1:00
# individual: 0:30
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