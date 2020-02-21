
userModel = {}
activeUser = ''

# data validation function, that takes a type of input and a hint and doesn't return anything untill a right type of entry is inputted
def validateInput(inpType, hint):
    validityCheck = False
    while validityCheck == False:
        usrInp = input(hint)
        if inpType == 'string':
            validityCheck = usrInp != ''
        elif inpType == 'e-mail':
            validityCheck = '@' in usrInp and '.' in usrInp
        elif inpType == 'integer':
            try:
                usrInp = int(usrInp)
                validityCheck = True
            except:
                validityCheck = False
                print('Not a valid number')
        else:
            break
    return usrInp
        

def appController():
    try:
        entryPoint = 0
        print("Please choose which operation you want to conduct: \n 1) Register \n 2) LogIn \n 3) Deposit \n 4) Exit")
        while entryPoint <1 or entryPoint >3:
            entryPoint = int(input("your choice: "))

            # registering a customer
            if entryPoint == 1:
                username = validateInput('string', "please enter your username: ")
                password = validateInput('string', "please enter your password: ")
                email = validateInput('e-mail', "please enter your e-mail: ")
                userModel.update({
                    username : {
                        'password': password,
                        'email': email,
                        'deposit': 0
                    }
                })
                print(userModel)
                print(userModel[username])
                appController()

            # loggingn in a customer
            elif entryPoint == 2:
                global activeUser
                try:
                    username = validateInput('string', "please enter your username: ")
                    password = validateInput('string', "please enter your password: ")
                    user = userModel[username]
                    if user['password'] == password:
                        activeUser = username
                        print("Congratulations, you are now logged in as: ", activeUser)
                    else:
                        print("Password is incorrect")
                except Exception as x:
                    print(x, "No such username")
                appController()


            # charging  a customer
            elif entryPoint == 3:
                if activeUser == '':
                    print('you are not signed in yet!')
                    appController()
                else:
                    deposit = validateInput('integer', 'how much do you wannt to deposit?')
                    userModel[activeUser]['deposit'] += deposit
                    print("Your new balance is: ", userModel[activeUser]['deposit'])
                appController()

            # exit from the program
            elif entryPoint == 4:
                break

            
    except Exception as x:
        print("Gotta choose the right option!", x)
        appController()
        
appController()



