/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
with cte as (SELECT coll.contest_id, sum(total_submissions) as sum_sub,sum(total_accepted_submissions) as sum_accept from colleges coll join challenges chal on coll.college_id = chal.college_id join Submission_Stats ss on ss.challenge_id = chal.challenge_id group by coll.contest_id),
cte2 as (SELECT coll.contest_id, sum(total_views) as sum_view,sum(total_unique_views) as sum_uniq from colleges coll join challenges chal on coll.college_id = chal.college_id join View_Stats vs on vs.challenge_id = chal.challenge_id group by coll.contest_id )
SELECT cont.contest_id,cont.hacker_id,cont.name,sum_sub,sum_accept, sum_view,sum_uniq from Contests cont join cte on cte.contest_id = cont.contest_id join cte2 on cte2.contest_id = cont.contest_id where sum_sub >0 or sum_accept >0 or sum_view >0 or sum_uniq >0 order by cont.contest_id
