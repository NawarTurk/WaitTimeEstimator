import pandas as pd
import numpy as np
import random
import string

match_id = "MATCH_ID"
part_size = 'PARTY_SIZE'
queue_duration = 'QUEUE_DURATION_IN_SECS'
rank = 'MMR_GROUP_DECILE'
start_time = 'MATCHMAKING_ATTEMPT_START_TIME_UTC'
day = 'MATCHMAKING_DAY_OF_WEEK'
player_role = 'PLAYER_ROLE'
server_name = 'SERVER_NAME'
platform = 'PLATFORM'
match_outcome="MATCHMAKING_OUTCOME"
char_name = " CHARACTER_NAME"

def random_id():
  return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))

def random_data():
  df = pd.DataFrame([random_id() for i in range(1000)], columns = [match_id])
  df[start_time] = [f"{np.random.randint(0, 24):02d}:{np.random.randint(0, 60):02d}:{np.random.randint(0, 60):02d}" for _ in range(len(df))]
  df[day] = np.random.choice(["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], size=len(df))
  df[player_role] = np.random.choice(["Killer", "Survivor"], p= [0.2, 0.8], size=len(df))
  df[part_size] = df[player_role].apply(lambda x: np.random.randint(1,5) if x=="Survivor" else 1)
  df[server_name] = np.random.choice([" ap-southeast-1", "us-west-2", " eu-central-1", " us-east-1", ], size=len(df))
  df[platform] = np.random.choice(["steam", "egs", "xsx", "ps5"], size = len(df))
  df[queue_duration] = np.random.randint(0, 120,size=len(df))
  df[match_outcome] = df[queue_duration].apply(lambda x: "played_cancelled" if x==0 else "success")
  df[rank] = np.random.randint(1, 21,size=len(df))
  df[char_name] = df[player_role]
  df["Unnamed"] = random.sample(range(2*len(df)), len(df))

  return df

if __name__=="__main__":
  random_data().to_csv("f_data.csv")
