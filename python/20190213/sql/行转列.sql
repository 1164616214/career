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
select DISTINCT (select s_name from student s where s.s_id = st.s_id) "����",
ifnull((select s_score from score ss where ss.s_id = s.s_id and ss.c_id = 01), 0) "����",
ifnull((select s_score from score ss where ss.s_id = s.s_id and ss.c_id = 02), 0) "��ѧ",
ifnull((select s_score from score ss where ss.s_id = s.s_id and ss.c_id = 03), 0) "Ӣ��"
from score s
RIGHT JOIN student st
on s.s_id = st.s_id;

# GROUP_CONCAT��ʽ
select s.s_id, GROUP_CONCAT(s.s_score separator ',')
from score s
group by s.s_id;

