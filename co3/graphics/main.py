import graphics.rectangle as rect
import graphics.circle as cir
import graphics.subgraphic.sphere as spr
import graphics.subgraphic.cuboid as cu

print("Area of circle:",cir.area(2))
print("Perimeter of circle:",cir.pere(2))

print("Area of rectangle:",rect.area(2,3))
print("Perimeter of rectangle:",rect.pere(2,3))

print("Area of sphere:",spr.area(2))
print("Perimeter of sphere:",spr.pere(2))

print("Area of cuboid:",cu.area(1,1,2))
print("Perimeter of cuboid:",cu.pere(1,1,2))