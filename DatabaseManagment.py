import sqlite3

conn = sqlite3.connect('Usernames.db')
x = 0

def CreateDB():
    conn.execute("CREATE TABLE IF NOT EXSISTS Usernames(NAME TEXT, ADMIN BOOL);")

def EditDB(x):
    while(x == 0):
        userInput = input("What would you like to do?\n(a= Add new name, c= Change privileges, d= Delete name) ")
        name = input('Username: ')
        
        if(userInput == 'a'):
            admin = input('Privilege level (1= admin, 0= default): ')
            conn.execute('INSERT INTO IF NOT EXISTS Usernames ((NAME, ADMIN) VALUES (?,?)'(name, admin))
            conn.commit()
            x = 1            
        elif(userInput == 'c'):
            changePriv = input('What would you like to change their privilege to?\n(1= admin, 0= default):')
            conn.execute('UPDATE Usernames set ADMIN = (?) WHERE NAME = (?)'(changePriv,name))
            conn.commit()
            x = 1
        elif(userInput == 'd'):
            conn.execute("DELETE FROM Usernames WHERE NAME = (?)"(name))
            conn.commit()
            x = 1
        else:
            print('That is not a recognised command')

def ViewDB():
    cursor = conn.execute("SELECT * FROM Usernames;")
    for(row in cursor):
        print("Username:", row[0])
        print("Admin:", row[1])


while(x == 0):
    userInput = input("What would you like to do?\n(c= Create, e= Edit, v= View) ")

    if(userInput == 'c'):
        CreateDB()
        x = 1 
    elif(userInput == 'e'):
        EditDB(0)
        x = 1
    elif(userInput == 'v'):
        ViewDB()
        x = 1
    else:
        print('That is not a recognised command')

conn.close()