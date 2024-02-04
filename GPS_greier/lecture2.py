
def calculate_distance(list):
    lengde = 0
    for e in list:
        lengde+=int(e)
    return lengde


liste = []

checkpoints = 5
teller = 0
while teller<checkpoints:
    lengde_på_etappen = input("Skriv inn hvor lang etappen var: ")
    liste.append(lengde_på_etappen)
    teller+=1

print(liste)
print("Total distance: " + str(calculate_distance(liste)))
print("Gjennomsnitts distansen var:  " + str((calculate_distance(liste))/checkpoints))
