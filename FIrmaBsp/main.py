import stuff
import random
import string


persons = []
mitarbeiter = []
gruppenleiter = []


def RandomString(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))



def addPerson():
    for x in range(10):
        persons.append(stuff.Person(random.choice(list(stuff.Sex)), random.randint(16,65), RandomString(random.randint(4, 20)), random.choice(list(stuff.Department))))

def addMitarbeiter():
    for x in range(10):
        mitarbeiter.append(stuff.Mitarbeiter(random.choice(list(stuff.Sex)), random.randint(16,65), RandomString(random.randint(4, 20)), random.choice(list(stuff.Department)), random.randint(1000, 5000)))


def addGruppenleiter():
    for x in range(4):
        gruppenleiter.append(stuff.Gruppenleiter(random.choice(list(stuff.Sex)), random.randint(16,65), RandomString(random.randint(4, 20)), random.choice(list(stuff.Department)), random.randint(1000, 5000), "Leiter"))


def getMitarbeiterGruppenleiter():
    return len(mitarbeiter), len(gruppenleiter)


def getDepartments():
    return len(stuff.Department)


def getHighestDepartment(dep):
    count = 0
    for x in mitarbeiter:
        if x.department == dep:
            count += 1
    for x in persons:
        if x.department == dep:
            count += 1
    for x in gruppenleiter:
        if x.department == dep:
            count += 1
    return count



def MaleToFemale():
    male = 0
    female = 0
    for x in persons:
        if(x.sex== stuff.Sex.Male):
            male += 1
        else:
            female += 1
    for x in mitarbeiter:
        if(x.sex== stuff.Sex.Male):
            male += 1
        else:
            female += 1
    for x in gruppenleiter:
        if(x.sex== stuff.Sex.Male):
            male += 1
        else:
            female += 1
    return "Männer in %: " + str(round((male)/(len(persons)+len(mitarbeiter)+len(gruppenleiter)), 2)*100), "Frauen in %: " + str(round((female)/(len(persons)+len(mitarbeiter)+len(gruppenleiter)), 2)*100)


if __name__ == "__main__":
    print()
    addPerson()
    addMitarbeiter()
    addGruppenleiter()
    print("Mitarbeiter: " + str(getMitarbeiterGruppenleiter()[0]))
    print("Gruppenleiter: " + str(getMitarbeiterGruppenleiter()[1]))
    print("Anzahl Abteilungen: " + str(getDepartments()))
    for x in stuff.Department:
        print(str(x) + ": " + str(getHighestDepartment(x)))
    print(MaleToFemale()[0])
    print(MaleToFemale()[1])



