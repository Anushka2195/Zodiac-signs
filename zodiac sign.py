month=input("enter your birth of month: ")
date=int(input("enter your birth date: "))
if month=='january':
    if date<=19:
        print("u r a capricorn")
    else:
        print("u r a aquarius")
elif month=='february':
    if date<=18:
        print("u r a aquarius")
    else:
        print("u r a pisces")
elif month=='march':
    if date<=20:
        print("u r a pisces")
    else:
        print("u r a aries")
elif month=='april':
    if date<=19:
        print("u r a aries")
    else:
        print("u r a taurus")
elif month=='may':
    if date<=20:
        print("u r a taurus")
    else:
        print("u r a gemini")
elif month=='june':
    if date<=21:
        print("u r a gemini")
    else:
        print("u r a cancer")
elif month=='july':
    if date<=22:
        print("u r a cancer")
    else:
        print("u r a leo")
elif month=='august':
    if date<=22:
        print("u r a leo")
    else:
        print("u r a virgo")
elif month=='september':
    if date<=22:
        print("u r a virgo")
    else:
        print("u r a libra")
elif month=='october':
    if date<=23:
        print("u r a libra")
    else:
        print("u r a scorpio")
elif month=='november':
    if date<=21:
        print("u r a scorpio")
    else:
        print("u r a sagittarius")
elif month=='december':
    if date<=22:
        print("u r a sagittarius")
    else:
        print("u r a capricorn")
else:
    print("Error")
