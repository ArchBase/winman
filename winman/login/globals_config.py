import json
import atexit

print("Started")

config = None

# Read 
# the JSON file
with open("C:/Users/aksha/Projects/creative_under_ends/winman/winman/winman/login/config.json", "r") as file:
    config = json.load(file)



def close():
    #print("Closed after saving weights")
    # Write the updated dictionary back to the JSON file
    with open("C:/Users/aksha/Projects/creative_under_ends/winman/winman/winman/login/config.json", "w") as file:
        json.dump(config, file, indent=4)
    print()

def progress_bar(label, progress, total):
    percent = 100 * (progress / float(total))
    print(f"{label}: {progress}/max     {round(percent, 3)}%" ,end='\r')

atexit.register(close)