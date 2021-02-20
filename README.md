# Mega Scripts
Create and manage mega accounts in bulk. (with automatic email verification)

**NOTE: You need megatools installed on your computer for this to work.**

Install from your distro's repos like `dnf install megatools` or install from https://megatools.megous.com/ 

* `new_mega_account.py` - Create new mega accounts in bulk. It takes care of email verification so you just have to run this script and wait. Change the account password and number of accounts to be created in the script. Saves credentials to a file called `accounts.csv`
* `keep_account_active.py` - Keep mega accounts alive. Mega deletes inactive accounts after 3 months so this script logs in to your accounts to keep them active. Run this once a month to be safe. (You'll forget so setup a systemd timer or cron.) It reads credentials from `accounts.csv`