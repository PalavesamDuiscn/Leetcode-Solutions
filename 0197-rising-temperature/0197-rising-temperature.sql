select t.id
from Weather t join weather y
on datediff(t.recordDate,y.recordDate)=1
where t.temperature >y.temperature;