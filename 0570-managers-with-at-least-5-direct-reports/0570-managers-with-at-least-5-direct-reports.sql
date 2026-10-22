select  e.name
from Employee e join Employee r
on e.id=r.managerid
group by e.id,e.name
having count(r.id)>=5; 