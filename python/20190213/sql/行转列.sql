# ��ѯÿ��ѧ��ѧ�Ŀγ���ÿ�ųɼ�
select stu.s_name "ѧ����", c.c_name "�γ���", s.s_score "����"
from student stu left JOIN score s
on stu.s_id = s.s_id
left JOIN course c
on s.c_id = c.c_id;

# ��ת��(group by��case��䷽ʽ)
select st.s_name "����",
max(case c.c_id when 01 then s.s_score else 0 end) "����",
max(case c.c_id when 02 then s.s_score else 0 end)	"��ѧ",
max(case c.c_id when 03 then s.s_score else 0 end)	"Ӣ��"
from student st 
left join score s
on st.s_id = s.s_id
left join course c
on s.c_id = c.c_id
GROUP BY st.s_id;

# ��ת��(�Ӳ�ѯ)
select DISTINCT st.s_name "����",
(select s.s_score from course c where s.c_id=c.c_id and c.c_id = 01) "����",
(select s.s_score from course c where s.c_id=c.c_id and c.c_id = 02) "��ѧ",
(select s.s_score from course c where s.c_id=c.c_id and c.c_id = 03) "Ӣ��"
from student st
left join score s
on st.s_id = s.s_id;

# GROUP_CONCAT��ʽ
select s.s_id, GROUP_CONCAT(s.s_score separator ',')
from score s
group by s.s_id;

