# Keep Mega Accounts Active
# mega deletes inactive accounts
# reads credentials from a file called accounts.csv
# run this once a month to be safe (you'll forget so setup a systemd timer or cron)

import csv
import subprocess


def main():
    with open("accounts.csv") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:

            # CSV Format
            # email, password, username, purpose

            email = row[0].strip()
            password = row[1].strip()

            # login
            login = subprocess.run(
                [
                    "megatools",
                    "ls",
                    "-u",
                    email,
                    "-p",
                    password,
                ],
                universal_newlines=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            if "/Root" in login.stdout:
                print("Logged In", email)
            else:
                print("Error", email)


if __name__ == "__main__":
    main()
