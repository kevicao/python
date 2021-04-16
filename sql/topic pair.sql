
video_topic - video_id, topic_list


- 123 | ('dog', 'grass', 'tennis ball')
- 321 | ('dog', 'grass')

## order does not matter, (a,b) is same as (b,a)

=========
expand topic list to
table T
id, topic
123 'dog'
123 'grass'
123 'tennis ball'
321 'dog'
321 'grass'


select a.id
	, a.topic as topic_a
	, b.topic as topic_b 
	, concat(a.topic, b.topic) as pair

from T as a
join T as b
	on a.id = b.id
where a.topic != b.topics

pair_table
id topic_a  topic_b  pair
123 'dog', 'dog'  #filter out, not topic pair
123 'dog', 'grass'
123 'dog' 'tennis ball'
123 'grass' 'tesnnies ball'
123 'grass', 'dog'


select pair,
	count(*)/2 as pair_count
from pair_table
group by pair