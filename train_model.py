import pandas as pd
from datetime import datetime

file_p = "/content/drive/MyDrive/Remi.csv"
df = pd.read_csv(file_p)
df.columns = df.columns.str.strip()
df['MATCHMAKING_ATTEMPT_START_TIME_UTC'] = df['MATCHMAKING_ATTEMPT_START_TIME_UTC'].apply(lambda x: (datetime.strptime(x, '%H:%M:%S').strftime('%H:%M:%S') if not isinstance(x, str) else x)[:-6])
df=df.drop(["MATCH_ID","MATCHMAKING_OUTCOME","CHARACTER_NAME","MATCHMAKING_OUTCOME", "Unnamed: 11"], axis=1)
df[['PARTY_SIZE','QUEUE_DURATION_IN_SECS','MMR_GROUP_DECILE']] = df[['PARTY_SIZE','QUEUE_DURATION_IN_SECS','MMR_GROUP_DECILE']].astype("int32")
df = df[df['QUEUE_DURATION_IN_SECS'] !=int(0)]

# debug
print(df)
print(df.dtypes)