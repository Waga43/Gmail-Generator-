import random
import time

#PASSWORD SECURITY_____________________________________

pass_combos = ['1','2','3','4','5','6','7','8','9','10','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
               'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','-','!','@','#','$','%','^','&','*','(',')']



def pass1():
    pas1 = f'{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}'
    print (pas1)

#FIRST/LAST NAME_____________________________________

first_n = ['Jimmy','Edward','Sheldon','Robert','Ben','James','George','Brian','Gary','Larry','Daniel','Mark','David','William','Joshua','Ralph','Keith','Fred','Todd','Shawn','Jesse','Dale','Jacob','Ray','Clifford','Jim',
           'Alex','Greg','Tim','Zachary','Rick','Nathaniel','Brad','Cory','Neil','Cody','Chase','Jordan','Wade','Seth','Andy','Ross','Julian','Morris','Kirk','Bob','Christian','Javier','Raul','Arnold','Hairy','Ralph',
           'Logan','Jack','Aiden','Owen','Elijah','Luke','Isaac','Gabriel','Miles','Jeremiah','Ian','Carson','Axel','Bryson','Kai','Brayden','Gavin','Tyler','Diego','Kevin','Brody','Patrick','Felix','Enzo','Jaden',
           'Mia','Ella','Scarlett','Emily','Victoria','Layla','Grace','Madison','Leah','Zoe','Stella','Hazel','Bella','Aurora','Audrey','Sarah','Caroline','Alice','Eva','Sadie','Alexa','Willow','Piper','Quinn',
           'Eliana','Rylee','Taylor','Mary','Faith','Kayla','Arya','Lily','Morgan','Trinity','Reese','Molly','Alina','Fiona','Angelina','Amara','Juliet','Dakota','Lola','Maggie','Olvie','Thea','Ruby','Gabriela']

last_n = ['Smith','Greyson','Jones','Brown','Lopez','Johnson','Lee','Clark','Martin','Davis','Miller','Young','Torres','Evans','Cruz','Gomez','Adams','Reed','Peterson','Price','West','Ford','Pitts','Woods','Owens',
          'Olson','Simmons','Long','Bell','Peterson','Ochoa','Robbins','Higgins','Strong','Giles','Ramirez','Wilson','Roberts','Hall','Jones','Hernandez','Butler','Perez','Turner','Walker','Flores','Reed','Rogers']

def full_n():
    name = f'{random.choice(first_n)} {random.choice(last_n)}'
    print (name)


#EMAIL USERNAME_____________________________________

word_1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0',]

word_2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0','.']

word_3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0','.']

word_4 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0','.']

word_5 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0','.']

word_6 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0','.']

word_7 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0','.']

word_8 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0','.']

word_9 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0',]

def em_c1():
    em1 = f'{random.choice(word_1)}{random.choice(word_2)}{random.choice(word_3)}{random.choice(word_4)}{random.choice(word_5)}{random.choice(word_6)}@gmail.com'
    print (em1)

def em_c2():
    em2 = f'{random.choice(word_1)}{random.choice(word_2)}{random.choice(word_3)}{random.choice(word_4)}{random.choice(word_5)}{random.choice(word_6)}{random.choice(word_7)}@gmail.com'
    print (em2)

def em_c3():
    em3 = f'{random.choice(word_1)}{random.choice(word_2)}{random.choice(word_3)}{random.choice(word_4)}{random.choice(word_5)}{random.choice(word_6)}{random.choice(word_7)}{random.choice(word_8)}@gmail.com'
    print (em3)

def em_c4():
    em4 = f'{random.choice(word_1)}{random.choice(word_2)}{random.choice(word_3)}{random.choice(word_4)}{random.choice(word_5)}{random.choice(word_6)}{random.choice(word_7)}{random.choice(word_8)}{random.choice(word_9)}@gmail.com'
    print (em4)


#BIRTH_____________________________________

months = ['January','Feburary','March','April','May','June','July','August','September','October','November','December']
days = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28']
years = ['2000','1999','1998','1997','1996','1995']

def bir_t():
    bday = f'{random.choice(months)} {random.choice(days)} {random.choice(years)}'
    print (bday)

#BANNER_____________________________________

print ('    ')
print ('   ______                _ __   ______                           __            ')
print ('  / ____/___ ___  ____ _(_) /  / ____/__  ____  ___  _________ _/ /_____  _____')
print (' / / __/ __ `__ \/ __ `/ / /  / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/')
print ('/ /_/ / / / / / / /_/ / / /  / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    ')
print ('\____/_/ /_/ /_/\__,_/_/_/   \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     ')
print ('-------------------------------------------------------------------------------')                                                                               
print ('    ')
print('                 ``...``                          __GMAIL BURNER GENERATOR__  ') 
print('            .:/+oooooooo+/:.                  ') 
print('         `:+oooooooooooooooo+-                ') 
print('       `:+ooooo++/::::/++oo+-                 ') 
print('      .+ooooo+:.        `--                   ')
print('     `yyyooo:`                                ')
print('     +hhhhy/        .-------------`           ')
print('     yhhhhh.        +ooooooooooooo-           ')
print('     yhhhhh.        +ooooooooooooo-           ')
print('     +hhhhy/        --------+ooooo.           ')
print('     `yyso++:`             :ooooo+            ')
print('      .+++++++:.`       `-+ooooo+`            ')
print('       `:++++++++/:::://+++oooo/`             ')
print('         `-/+++++++++++++++++:.               ')
print('            `-:/+++++++++/:.`          WARNING- These accounts can be very insecure.       ')
print('                 ``````                       ')
print ('    ')
start = input('eneter to start> ')

def accountf():
    print ('-------------------------------------')
    print ('Name_________')
    full_n()
    print ('  ')
    print ('Email________')
    em_c1()
    print ('  ')
    print ('Password_____')
    pass1()
    print ('  ')
    print ('Birth________')
    bir_t()
    print ('-------------------------------------')
    time.sleep(1)
    print ('-------------------------------------')
    print ('Name_________')
    full_n()
    print ('  ')
    print ('Email________')
    em_c2()
    print ('  ')
    print ('Password_____')
    pass1()
    print ('  ')
    print ('Birth________')
    bir_t()
    print ('-------------------------------------')
    time.sleep(1)
    print ('-------------------------------------')
    print ('Name_________')
    full_n()
    print ('  ')
    print ('Email________')
    em_c1()
    print ('  ')
    print ('Password_____')
    pass1()
    print ('  ')
    print ('Birth________')
    bir_t()
    print ('-------------------------------------')
    time.sleep(1)
    print ('-------------------------------------')
    print ('Name_________')
    full_n()
    print ('  ')
    print ('Email________')
    em_c3()
    print ('  ')
    print ('Password_____')
    pass1()
    print ('  ')
    print ('Birth________')
    bir_t()
    print ('-------------------------------------')
    time.sleep(1)
    print ('-------------------------------------')
    print ('Name_________')
    full_n()
    print ('  ')
    print ('Email________')
    em_c4()
    print ('  ')
    print ('Password_____')
    pass1()
    print ('  ')
    print ('Birth________')
    bir_t()
    print ('-------------------------------------')
    time.sleep(1)
    accountf()


accountf()