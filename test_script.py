import csv
import os

films =  [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]] 
films_csv = os.path.join('Random Files','films.csv')
with open(films_csv,'w',newline='') as c:
    write = csv.writer(c,delimiter=',')
    for film in films:
           write.writerow(film)
    