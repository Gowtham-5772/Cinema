import sqlite3

g=sqlite3.connect("test.db")

try:
    g.execute("CREATE TABLE MOVIES(NAME, ACTOR, ACTRESS, DIRECTOR, YEAR);")
except:
    pass

Dis=''

while(Dis !='D'):
    print(" A-Insert \n B-Search \n C-Show \n D-Quit ")
    
    Dis = input("ENTER OPTION:")
    if(Dis == 'A'):
        NAME =input("ENTER THE NAME:")
        ACTOR = input("ACTOR NAME:")
        ACTRESS =input("ACTRES NAME:")
        DIRECTOR = input("DIRECTOR NAME:")
        YEAR = input("YEAR:")
        g.execute(f'INSERT INTO MOVIES VALUES("{NAME}","{ACTOR}","{ACTRESS}","{DIRECTOR}","{YEAR}");')
        g.commit()
    elif(Dis == 'C'):
        print("(NAME, ACTOR, ACTRESS, DIRECTOR, YEAR)")
        for a in g.execute("SELECT * FROM MOVIES;"):
            for b in a:
                print(b +" | ", end='')
                print()
    elif(Dis == 'B'):
        b = input("COLUMN NAME:")
        d = input("ENTER VALUES:")
        print("(NAME, ACTOR, ACTRESS, DIRECTOR, YEAR)")
        for a in g.execute(f'SELECT * FROM MOVIES WHERE {b}={d}";'):
            print(a)
