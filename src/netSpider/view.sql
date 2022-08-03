SELECT up.device_id, up.university, 
        COUNT(qpd.question_id) AS question_cnt,
        IFNULL(
            (
                SELECT COUNT(qpds.result)
                FROM user_profile AS ups
                INNER JOIN question_practice_detail AS qpds
                ON ups.device_id = qpds.device_id 

                WHERE ups.device_id = up.device_id
                    AND qpds.date BETWEEN '2021-08-01' AND '2021-08-31'
                    AND ups.university = '复旦大学'

                GROUP BY qpds.result 
                HAVING qpds.result = 'right'
            ), 0
        ) AS right_question_cnt
        

FROM user_profile AS up
LEFT JOIN question_practice_detail AS qpd
ON up.device_id = qpd.device_id 
        AND qpd.date BETWEEN '2021-08-01' AND '2021-08-31'

WHERE up.university = '复旦大学'
        

GROUP BY up.device_id