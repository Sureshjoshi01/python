import csv

file = open("Books.csv","w")
newrecord = "To Kill A Mockingbird,Harper Lee,1960\n"
file.write(str(newrecord))
newrecord2= "A Brief Hisotry of Time, Stephen Hawking,1988\n"
file.write(str(newrecord2))
newrecord3="The Great Gatsby,F.ScottFitzgerald,1922\n"
file.write(str(newrecord3))
newrecord4 = "The Man Who Mistook His Wife for a Hat,Oliver Sacks,1985\n"
file.write(str(newrecord4))
newrecord5 = "Pride and Prejudice,Jane Austen,1813\n"
file.write(str(newrecord5))
file.close()

