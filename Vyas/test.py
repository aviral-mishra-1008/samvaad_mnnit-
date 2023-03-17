# article = "Russia (If not India then why not Russia, the globally isolated country which will be hard to defend on a global political scenario because of the Ukraine special military operation, but after India I would like to represent Russia. If I do not keep Russia at number two then entire first year will cancel me)"

# art = article[0:255]+"......"

# print(art)

def login():
    username = input("Enter Username : ") 
    password = input("Enter Password: ")
    usernames = ['aviral','ayushman','utkarsh','shresth']
    dict_pass = {'aviral':"1234","ayushman":"2345","utkarsh":"1223","shresth":"9223"}
    if username in usernames:
        try:
            dict_pass[username]=password
            print('login')
        except:
            print("Access denied")
    else:
        print('access denied')


login()