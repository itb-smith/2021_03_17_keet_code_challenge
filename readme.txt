### Ian Tad Smith - Keet Code Challenge - 20210317

keet_code_challenge.py is the script I made to perform the prediction of number of users.
db_setup.sql contains the statements I used to create my local mySQL instance for testing the script.

How to run:
python3.8 is needed to run the script, as well as the sqlalchemy, numpy, and pandas libraries.  All other libraries are standard.
In order to run successfully an instance of mySQL DB should also be running locally with the user:password:port root:root:3306 and the given tables created in a database named 'keet'.
The code can be run in command line by typing "python keet_coding_challenge.py" after navigating to the directory containing the script.

Possible Improvements:

This solution could be improved by having additional database security, externalizing passwords, and adding a merge operation on the daily_user_counts table.
I ran this against a local mySQL instance that was only temporary and had little security as seen by my username and password in the script.
The table created, daily_user_counts, will currently be recreated every time the script is run and thus overwrite any previous predictions.