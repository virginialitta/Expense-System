import csv
x = True
def csvreader():
    items = [[],[],[],[]]
    with open("items.csv","r") as file:
        filereader = csv.reader(file)
        for row in filereader:
            for i in range(0,4):
                items[i].append(row[i])
    file.close()
    return items
def csvwriter(items):
    with open("items.csv","w",newline = '') as file:
        writer  = csv.writer(file)
        for i in range(len(items[0])):
            print(i)
            writer.writerow([items[0][i],items[1][i],items[2][i],items[3][i]])
    file.close()
    
    
while x == True:
    choice1 = int(input("1.Edit Mode\n2.Analysis Mode\n3.Exit\n"))
    if choice1 == 1:
        choice2 = int(input("1.Add\n2.Delete\n"))
        if choice2 == 1:
            item = input("Enter expense item name:\n")
            Desc = input("Enter expense item Desc:\n")
            Cata = input("Enter expense item category:\n")
            Amou = input("Enter expense item Amount:\n")
            items = csvreader()
            items[0].append(item)
            items[1].append(Desc)
            items[2].append(Cata)
            items[3].append(Amou)
            print(items)
            csvwriter(items)
            print("item added")
            x = True
        elif choice2 == 2:
            item = input("Enter expense item name:")
            items = csv.reader()
            x = items[0].index(item)
            del items[0][x]
            del items[1][x]
            del items[2][x]
            del items[3][x]
            csvwriter(items)
            print("item deleted")
            x = True
        else:
            x = True
    elif choice1 == 2:
        choice3 = int(input("1.Expenditure Breakdown\n2.Average Spend\n3.Total Expenditure\n"))
        if choice3 == 1:
            pass

        if choice3 == 2:
            x = sum(items[3])
            y = len(items[3])
            print("The average spend is: ", x / y)

        if choice3 == 3:
            x = sum(items[3])
            print("The total expenditure is: ", x)
            
    elif choice1 == 3:
        x = False
    else:
        x = True
