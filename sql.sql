-- Medium SQL

-- Describe [Table]

-- Name        Null? Type         
-- ----------- ----- ------------ 
-- USERID            VARCHAR2(64) 
-- FLAGGEDSPAM       NUMBER       
-- STATSDATE         TIMESTAMP(6) 
-- UPVOTES           NUMBER       
-- READS             NUMBER       
-- VIEWS             NUMBER       
-- CLAPS             NUMBER       
-- SUBSCRIBERS       NUMBER  

select sum(READS), concat(EXTRACT(year FROM statsdate), EXTRACT(month FROM statsdate))
from ADMIN.MEDIUMSTATS
group by EXTRACT(year FROM statsdate), EXTRACT(month FROM statsdate)
order by EXTRACT(year FROM statsdate) asc, EXTRACT(month FROM statsdate) asc;

select sum(views), concat(EXTRACT(year FROM statsdate), EXTRACT(month FROM statsdate))
from ADMIN.MEDIUMSTATS
group by EXTRACT(year FROM statsdate), EXTRACT(month FROM statsdate)
order by EXTRACT(year FROM statsdate) asc, EXTRACT(month FROM statsdate) asc;

select sum(claps), concat(EXTRACT(year FROM statsdate), EXTRACT(month FROM statsdate))
from ADMIN.MEDIUMSTATS
group by EXTRACT(year FROM statsdate), EXTRACT(month FROM statsdate)
order by EXTRACT(year FROM statsdate) asc, EXTRACT(month FROM statsdate) asc;

select sum(SUBSCRIBERS), concat(EXTRACT(year FROM statsdate), EXTRACT(month FROM statsdate))
from ADMIN.MEDIUMSTATS
group by EXTRACT(year FROM statsdate), EXTRACT(month FROM statsdate)
order by EXTRACT(year FROM statsdate) asc, EXTRACT(month FROM statsdate) asc;

-- Twitter SQL 

describe ADMIN.TWITTERSTATS 

Name                        Null? Type   
--------------------------- ----- ------ 
STATSDATE                         DATE   
TOP_TWEET_IMPRESSIONS             NUMBER 
TOP_MENTION_ENGAGEMENTS           NUMBER 
TWEETS                            NUMBER 
TWEET_IMPRESSIONS                 NUMBER 
PROFILE_VISITS                    NUMBER 
MENTIONS                          NUMBER 
NEW_FOLLOWERS                     NUMBER 
TOP_FOLLOWED_BY                   NUMBER 
TOP_MEDIA_TWEET_IMPRESSIONS       NUMBER 

select TOP_TWEET_IMPRESSIONS, concat(EXTRACT(year FROM statsdate), EXTRACT(month FROM statsdate))
from ADMIN.TWITTERSTATS
order by EXTRACT(year FROM statsdate) asc, EXTRACT(month FROM statsdate) asc;

select TWEET_IMPRESSIONS, concat(EXTRACT(year FROM statsdate), EXTRACT(month FROM statsdate))
from ADMIN.TWITTERSTATS
order by EXTRACT(year FROM statsdate) asc, EXTRACT(month FROM statsdate) asc;

select PROFILE_VISITS, concat(EXTRACT(year FROM statsdate), EXTRACT(month FROM statsdate))
from ADMIN.TWITTERSTATS
order by EXTRACT(year FROM statsdate) asc, EXTRACT(month FROM statsdate) asc;

select NEW_FOLLOWERS, concat(EXTRACT(year FROM statsdate), EXTRACT(month FROM statsdate))
from ADMIN.TWITTERSTATS
order by EXTRACT(year FROM statsdate) asc, EXTRACT(month FROM statsdate) asc;

-- LinkedIn SQL

-- describe ADMIN.LINKEDINCONNECTIONSSTATS 

-- Name        Null? Type          
-- ----------- ----- ------------- 
-- FIRSTNAME         VARCHAR2(64)  
-- LASTNAME          VARCHAR2(64)  
-- EMAIL             VARCHAR2(64)  
-- COMPANY           VARCHAR2(256) 
-- POSITION          VARCHAR2(256) 
-- CONNECTDATE       DATE  

select count(connectdate), concat(EXTRACT(year FROM connectdate), EXTRACT(month FROM connectdate))
from ADMIN.LINKEDINCONNECTIONSSTATS 
group by EXTRACT(year FROM connectdate), EXTRACT(month FROM connectdate)
order by EXTRACT(year FROM connectdate) asc, EXTRACT(month FROM connectdate) asc;

select connectdate, concat(EXTRACT(year FROM connectdate), EXTRACT(month FROM connectdate))
from ADMIN.LINKEDINCONNECTIONSSTATS 
group by EXTRACT(year FROM connectdate), EXTRACT(month FROM connectdate)
order by EXTRACT(year FROM connectdate) asc, EXTRACT(month FROM connectdate) asc;
