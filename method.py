class Account():

    accounts = []
    
    def __init__(self, name, accountNumber, password, type):
        self.name = name
        self.accountNumber = accountNumber
        self.password = password
        self.type = type

        Account.accounts.append(self)


    def changeName(self, name):
        self.name = name

    # overloads method in line 14
    def changeName(self, name, password):
        self.name = name
        self.password = password

# এখানে আমরা যদি changeNmae মেথডকে কল করি তাহলে প্যারামিটার অনুযায়ী কল হবে ।
# অর্থাৎ যদি কেবল name দিই তাহলে প্রথমটা এবং যদি সাথে পাসওয়ার্ড দেওয়া হয় তাহলে দ্বিতীয়টা
