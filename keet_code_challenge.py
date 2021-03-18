import pandas as pd
from datetime import timedelta
import numpy as np
import sqlalchemy


def read_user_data():
    # Reads "users" table into a pandas dataframe.
    users_cols = ['id', 'first_name', 'last_name', 'age', 'gender', 'visit_date']
    users_query = f"select {','.join(users_cols)} from users"
    engine = sqlalchemy.create_engine(
        'mysql+mysqlconnector://root:root@localhost:3306/keet',
        echo=True)
    users_df = pd.DataFrame(engine.execute(users_query).fetchall(), columns=users_cols)
    return users_df


def create_daily_user_counts_df(users_df):
    # Counts the number of users by day.
    users_per_day_df = users_df.groupby(['visit_date'], as_index=False)['id'].count()
    daily_user_counts_df = pd.DataFrame()
    daily_user_counts_df['year'] = pd.DatetimeIndex(users_per_day_df['visit_date']).year
    daily_user_counts_df['month'] = pd.DatetimeIndex(users_per_day_df['visit_date']).month
    daily_user_counts_df['day'] = pd.DatetimeIndex(users_per_day_df['visit_date']).day
    daily_user_counts_df['observed'] = users_per_day_df['id']
    daily_user_counts_df['counts'] = np.NaN
    return daily_user_counts_df


def update_daily_user_counts_prediction(daily_user_counts_df, users_df):
    next_day = users_df['visit_date'].max() + timedelta(days=1)
    # Calculates the number of users expected to signup 1 day into the future.
    next_day_prediction = int(daily_user_counts_df['observed'].mean())
    next_record = {'year': next_day.year, 'month': next_day.month, 'day': next_day.day, 'observed': np.NaN,
                   'counts': next_day_prediction}
    # Append the new record with the expected count to the dataframe.
    daily_user_counts_df = daily_user_counts_df.append(next_record, ignore_index=True)
    return daily_user_counts_df


def insert_daily_user_counts(daily_user_counts_df):
    # Load/Insert the results of your calculations (the dataframe) into the "daily_user_counts" table.
    daily_user_counts_df['year'] = daily_user_counts_df['year'].astype('Int64')
    daily_user_counts_df['month'] = daily_user_counts_df['month'].astype('Int64')
    daily_user_counts_df['day'] = daily_user_counts_df['day'].astype('Int64')
    daily_user_counts_df['observed'] = daily_user_counts_df['observed'].astype('Int64')
    daily_user_counts_df['counts'] = daily_user_counts_df['counts'].astype('Int64')
    engine = sqlalchemy.create_engine(
        'mysql+mysqlconnector://root:root@localhost:3306/keet',
        echo=True)
    daily_user_counts_df.to_sql(con=engine, name='daily_user_counts', if_exists='replace', index=False)


def main():
    users_df = read_user_data()
    daily_user_counts_df = create_daily_user_counts_df(users_df)
    daily_user_counts_df = update_daily_user_counts_prediction(daily_user_counts_df, users_df)
    insert_daily_user_counts(daily_user_counts_df)


main()
