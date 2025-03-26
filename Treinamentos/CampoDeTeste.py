pal1 = input()
pal2 = input()
pal3 = input()

if pal1 == 'vertebrado' and pal2 == 'ave' and pal3 == 'carnivoro':
    print('aguia')
elif pal1 == 'vertebrado' and pal2 == 'ave' and pal3 == 'onivoro':
    print('pomba')
elif pal1 == 'vertebrado' and pal2 == 'mamifero' and pal3 == 'onivoro':
    print('homem')
elif pal1 == 'vertebrado' and pal2 == 'mamifero' and pal3 == 'herbivoro':
    print('vaca')
elif pal1 == 'invertebrado' and pal2 == 'inseto' and pal3 == 'hematofago':
    print('pulga')
elif pal1 == 'invertebrado' and pal2 == 'inseto' and pal3 == 'herbivoro':
    print('largata')
elif pal1 == 'invertebrado' and pal2 == 'anelideo' and pal3 == 'hematofago':
    print('sanguessuga')
else:
    print('minhoca')