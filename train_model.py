import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

part_size = 'PARTY_SIZE'
queue_duration = 'QUEUE_DURATION_IN_SECS'
rank = 'MMR_GROUP_DECILE'
start_time = 'MATCHMAKING_ATTEMPT_START_TIME_UTC'
day = 'MATCHMAKING_DAY_OF_WEEK'
player_role = 'PLAYER_ROLE'
server_name = 'SERVER_NAME'
platform = 'PLATFORM'



file_p = "Remi.csv"
df = pd.read_csv(file_p)
df.columns = df.columns.str.strip()
df[start_time] = df[start_time].apply(lambda x: (datetime.strptime(x, '%H:%M:%S').strftime('%H:%M:%S') if not isinstance(x, str) else x)[:-6])
df=df.drop(["MATCH_ID","MATCHMAKING_OUTCOME","CHARACTER_NAME","MATCHMAKING_OUTCOME", "Unnamed: 11"], axis=1)  # this column does not exist ___________________________>
df[[part_size, queue_duration, rank]] = df[[part_size,queue_duration, rank]].astype("int32")
df = df[df[queue_duration] !=int(0)]

print(df)
# Apply one-hot encoding to the dataframe
# Assuming 'col1', 'col2', 'col3' are the categorical columns that need encoding
df_encoded = pd.get_dummies(df, columns=[day, player_role, server_name, platform])

# Display the encoded dataframe
print("\nEncoded DataFrame:")
print(df_encoded)

# Separate the features and the target
X = df_encoded.drop(queue_duration, axis=1)  # drop the target column to isolate features
y = df_encoded[queue_duration]               # isolate the target column

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)
print("X_test")
print(X_test)

print("X_Train")
print(X_train)
print("y_pred")
print(y_pred)
print("y_test")
print(y_test)
# Evaluate the model using Root Mean Squared Error
rmse = mean_squared_error(y_test, y_pred, squared=False)

# Output the performance metric
print("\nModel Performance:")
print(f"Root Mean Squared Error: {rmse}")

# Optionally: Save the trained model to a file
# from joblib import dump
# dump(model, 'trained_model.joblib')

print(type(X_test))