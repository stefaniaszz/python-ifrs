p1 = input()
p2 = input()
p3 = input()
animal = 0
if p1 == 'vertebrado':
    if p2 == 'ave':
        if p3 == 'carnivoro':
            animal = 'aguia'
        elif p3 == 'onivoro':
            animal = 'pomba'
    elif p2 == 'mamifero':
        if p3 == 'herbivoro':
            animal = 'vaca'
        elif p3 == 'onivoro':
            animal = 'homem'
elif p1 == 'invertebrado':
    if p2 == 'inseto':
        if p3 == 'hematofago':
            animal = 'pulga'
        elif p3 == 'herbivoro':
            animal = 'lagarta'
    elif p2 == 'anelideo':
        if p3 == 'hematofago':
            animal = 'sanguessuga'
        elif p3 == 'onivoro':
            animal = 'minhoca'

print(animal)