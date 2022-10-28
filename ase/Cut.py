from ase.io import read, write
from ase.visualize import view
from ase.lattice.surface import surface

cut = (1,0,0)

atoms = read('POSCAR_SiO2')

surf = surface(atoms, cut, 3, 10)

write('POSCAR_orig', surf)

view(atoms)

