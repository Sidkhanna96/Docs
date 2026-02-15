# Design a banking system to facilitate account creation, deposits, transfers, and listing 
# the most active accounts by total monetary activity, 
# with commands entered via parsing CSV/JSON.


'''
The implementation for the system gets broken up into three parts:

Implement creating accounts and depositing money into an account by ID
Implement transferring money with validation to ensure the accounts for the transfer both exist and that the account money is being removed from has enough money in it to perform the transfer
Implement finding the top n active accounts by the total amount of money that has been moved in and out of the accounts
Some pre-answer information that may be useful:

The system will work by reading a list of transactions and you get to choose how to that data is ingested. The options are CSV, JSON, and a native list of raw data. I chose the native list because it was the easiest for me to go off of given the time constraint.
There is no database involved in the system and there's no need to over-complicate the solution. I chose to implement the data store as a hashmap of account ID's to account details. My goal for the data store was to allow for maximum flexibility.
Each transaction will contain an action and parameters for that specific action. Let those define the function signatures for interacting with your data store.
CREATE_ACCOUNT, ACCOUNT_ID
DEPOSIT, AMOUNT
TRANSFER, FROM_ID, TO_ID, AMMOUNT
TOP_ACTIVITY, N

My approaches using Python:

Data Storage
The only "thing" you need to store are accounts and again, I went with a dead simple approach of using a dictionary to map account ID to the account data. This gives me look-up by ID by default for easier "IO" and prevented any kind of iteration for simple operations like creating accounts, deposits, etc...

Account metadata
You only need two details, balance and transaction total. I used a map for the account metadata, a class would be more "ideal" I think though. Again, when under pressure, I used a dictionary for everything because it's the default setting for my brain. A strong OOP design will push you towards creating a class Account with an ID, a balance, and a transaction total. A constructor for creating new accounts and setting the appropriate defaults and methods for the account actions (deposit and transfer) will be filled in as you go. If you go the dictionary route, you'll be implementing functions that operate on maps instead. To each their own.

The entry point and the shape of the system
I had three layers of system in place; The entry point function, the "router" function, and the handler functions.

The entry point function iterated over the list of operations (ledger) and for each operation, called the router function. The router function was a match/case that would match on the operation and send the data (after proper type casting) to the respective handler. The handler functions were very small units that performed isolated actions but were a great point for debugging and logging (neither were necessary but it was a nice shape to work with).

Most of my experience has been building rest and graphql APIs so I went with a structure that was similar to a REST API, router -> endpoint -> handler. This also gave me some space to tell my interviewer about how this structure would be able to adapt to being used as a REST API and how I could implement testing even though it's not a part of the interview. They seemed to enjoy that bit of conversation.

Building the actions
Action 1a: Create an account The account ID was a parameter and the data behind it was sensible defaults (balance and transaction total set to 0). The function itself just shoved that into the storage dictionary.

Action 1b: Create a deposit by account ID Update the balance by doing something like storage_dict[account_id]["balance"] += deposit_amount. Easy peasy.

Action 2: Create a transfer This handler was built in two pieces. First, make sure the transfer can happen by ensuring that both accounts exist and that the "from" account's balance was >= the transfer amount. Second, decrease the from account's balance by the transfer amount and increase the to accounts balance by the transfer amount. Again, we got this.

Action 3a: Add a transaction total to the accounts Whenever a deposit or transfer happened for an account, that accounts transaction total would increase by the amount of money moved. The trick here is to always add the "amount" in play to the transaction total, even if the money is being moved out of an account, the transaction total gets increased.

Action 3b: Find the n most active accounts by transaction total I'm bad at implementing sorting algorithms and this part stumped me so don't let it stump you. Go get that perfect 3/3!

To achieve this part, you're going to sort all of the accounts by transaction total and then alphabetically. If account_a and account_b have the same transaction total, account_a needs to show up in that list first! After that, take the top n accounts and return them. If n is larger than the total number of accounts, return all of the accounts.

I stumbled through this part a bit but the interviewer assured me that this is a bonus points round and not a requirement for passing. I still wish I answered it though.
'''
# ...existing code...


class AccountStore:
    def __init__(self):
        self.dbData = {}
    
    def createAccountStore(self, accountId):
        self.dbData[accountId] = {"banking": 0, "activity": 0}

# Interface
class Command:
    def __init__(self):
        pass
    
    def execute(self, parts):
        action = parts[0]

        if action == "CREATE_ACCOUNT":
            return createAccountCommand(parts[1])
        else:
            raise print(f"Value Error {action}")
        
class createAccountCommand:
    def __init__(self, accountId):
        self.accountId = accountId

    def execute(self, store):
        store.createAccountStore(self.accountId)


class BankDataRepo:
    def __init__(self):
        self.fileDir = "./Repo/banking.txt"
    
    def parseText(self):

        store = AccountStore()
        with open(self.fileDir, mode="r", encoding="utf-8") as file:
            line = file.readlines()
            count = 0

            for f in line:
                lineData = f.strip().split(",")
                cmd = Command().execute(lineData)
                cmd.execute(store)
                
                count += 1
                if count == 1:
                    break

        print(store.dbData)


if __name__ == "__main__":
    print(BankDataRepo().parseText())




