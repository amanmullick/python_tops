acc=000000
bank = {
    
    "cust1" : {
    "name": "aman",
    "accountNo":acc+1,
    "address":"maninagar"
    },

    "cust2" : {
    "name": "ravi",
    "accountNo":acc+2,
    "address":"maninagar"
    },

    "cust3" : {
    "name": "pranav",
    "accountNo":acc+3,
    "address":"maninagar"
    },
    
    "cust4" : {
    "name": "krish",
    "accountNo":acc+4,
    "address":"maninagar"
    }
    
}
#print(bank)
#print(bank.keys())

print(bank["cust1"]["name"])