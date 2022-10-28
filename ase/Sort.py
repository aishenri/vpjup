from ase.io import read, write
from ase.visualize import view

my_list = []

atoms = read('POSCAR_messy')

atoms.set_constraint()

for atom in atoms:
	tmp_list = []
	sym = atom.symbol
	x = atom.position[0]
	y = atom.position[1]
	z = atom.position[2]
	tmp_list.append(sym)
	tmp_list.append(x)
	tmp_list.append(y)
	tmp_list.append(z)
	#print tmp_list

	my_list.append(tmp_list)

my_list = sorted(my_list, key = lambda x: x[0])

#print my_list

for i, atom in enumerate(atoms):
	atom.symbol = my_list[i][0]
	atom.position[0] = my_list[i][1]
	atom.position[1] = my_list[i][2]
	atom.position[2] = my_list[i][3]

print 'Remember that all constraints must be readded!'

write('POSCAR_clean', atoms)
