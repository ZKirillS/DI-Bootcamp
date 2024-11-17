--this is a comment
-- cntrl + /
create table actors (
actor_id SERIAL PRIMARY KEY, -- serial = 1,2,3,4,5,6 etc.
first_name VARCHAR (50) NOT NULL, -- varchar sets max chars
last_name VARCHAR (100) NOT NULL, -- not null dont acepts empty strings
age DATE NOT NULL,
number_oscars SMALLINT NOT NULL
)