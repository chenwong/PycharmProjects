import csv

def deal_director():
    with open('豆瓣电影top250.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        new = []
        for row in spamreader:
            new.append(row)

    with open('new.csv', 'w') as newfile:
        writer = csv.writer(newfile)
        for row in new:
            if "/" not in row[4]:
                writer.writerow(row)
            else:
                a = row[4].strip().split("/")
                i = 0
                while i < len(a):
                    writer.writerow([row[0],row[1],row[2],row[3],a[i].strip(),row[5],row[6],row[7],row[8],row[9],row[10]])
                    i=i+1
def deal_writer():
    with open('豆瓣电影top250.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        new = []
        for row in spamreader:
            new.append(row)

    with open('new1.csv', 'w') as newfile:
        writer = csv.writer(newfile)
        for row in new:
            if "/" not in row[5]:
                writer.writerow(row)
            else:
                a = row[5].strip().split("/")
                i = 0
                while i < len(a):
                    writer.writerow([row[0],row[1],row[2],row[3],row[4],a[i].strip(),row[6],row[7],row[8],row[9],row[10]])
                    i=i+1

def deal_actor():
    with open('豆瓣电影top250.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        new = []
        for row in spamreader:
            new.append(row)

    with open('new2.csv', 'w') as newfile:
        writer = csv.writer(newfile)
        for row in new:
            if "/" not in row[6]:
                writer.writerow(row)
            else:
                a = row[6].strip().split("/")
                i = 0
                while i < len(a):
                    writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],a[i].strip(),row[7],row[8],row[9],row[10]])
                    i=i+1
if __name__ == '__main__':
    # deal_director()
    # deal_writer()
    deal_actor()