import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def train_and_get_model(file_p) :
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
    char_name = "CHARACTER_NAME"



    #file_p = "uploaded_file/CLIENT_DATASET.csv"
    df = pd.read_csv(file_p, skipinitialspace=True)
    df.columns = df.columns.str.strip()
    df[start_time] = df[start_time].apply(lambda x: (datetime.strptime(x, '%H:%M:%S').strftime('%H:%M:%S') if not isinstance(x, str) else x)[:-6])
    df=df.drop([match_id,match_outcome,char_name], axis=1)  # this column does not exist ___________________________>
    df[[part_size, queue_duration, rank]] = df[[part_size,queue_duration, rank]].astype("int32")
    df = df[df[queue_duration] !=int(0)]

    print("im herererere")
    # df_encoded = pd.get_dummies(df, columns=[day, player_role, server_name, platform])
    df_encoded = encode_dataframe(df)

    # Display the encoded dataframe
  

    # Separate the features and the target
    X = df_encoded.drop(queue_duration, axis=1)  # drop the target column to isolate features
    y = df_encoded[queue_duration]               # isolate the target column

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the Linear Regression model
    model = LinearRegression()
    print(type(model))
    
    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    print("x-test")
    print(X_test)



    # Evaluate the model using Root Mean Squared Error
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    # Output the performance metric
    print("\nModel Performance:")
    print(f"Root Mean Squared Error: {rmse}")

    # Optionally: Save the trained model to a file
    # from joblib import dump
    # dump(model, 'trained_model.joblib')
    return(model, rmse)

def encode_dataframe(df):
    day = 'MATCHMAKING_DAY_OF_WEEK'
    player_role = 'PLAYER_ROLE'
    platform = 'PLATFORM'
    server_name = 'SERVER_NAME'
 

    day_to_num = {
    'Sun': 0,
    'Mon': 1,
    'Tue': 2,
    'Wed': 3,
    'Thu': 4,
    'Fri': 5,
    'Sat': 6
    }

    role_to_num = {
    'Killer': 0,
    'Survivor': 1
    }

    platform_to_num = {
    'steam': 0,
    'egs': 1,
    'xsx': 2,
    'ps5': 3
    }

    server_to_num = {
    'ap-southeast-1': 0,
    'us-west-2': 1,
    'eu-central-1': 2,
    'us-east-1': 3,

    }

    df[day] = df[day].map(day_to_num)
    df[player_role] = df[player_role].map(role_to_num)
    df[platform] = df[platform].map(platform_to_num)
    df[server_name] = df[server_name].map(server_to_num)

    return df



if __name__=="__main__":
    train_and_get_model("../f_data.csv")
