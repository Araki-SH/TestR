import enviroment as en
import action 
import acter 

n = 6
map = en.map_create(n)
en.map_view(map)
p = acter.start
acter.move(n,map,1,p)