#PostgreSQL query
SELECT  a1.machine_id,
        ROUND(AVG(a1.timestamp - a2.timestamp)::numeric, 3) as processing_time
FROM Activity as a1, Activity as a2
WHERE   a1.activity_type = 'end' and
        a2.activity_type = 'start' and
        a1.process_id = a2.process_id and
        a1.machine_id = a2.machine_id
GROUP BY a1.machine_id