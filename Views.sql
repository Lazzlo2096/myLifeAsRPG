--
-- ���� ������������ � ������� SQLiteStudio v3.1.1 � �� ��� 2 14:15:12 2018
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������������: doneToday
CREATE VIEW doneToday AS
    SELECT *,
           date(done_tasks_history.date) 
      FROM done_tasks_history
     WHERE date(done_tasks_history.date) == date('now');


-- �������������: isEveryday
CREATE VIEW isEveryday AS
    SELECT *
      FROM tasks
     WHERE tasks.isEveryday == 1;


-- �������������: isEvrdy and not done today
CREATE VIEW [isEvrdy and not done today] AS
    SELECT *
      FROM isEveryday
           LEFT JOIN
           doneToday/* full outer */ ON isEveryday.task_id = doneToday.task_id
     WHERE doneToday.task_id IS NULL;


-- �������������: names of done tasks
CREATE VIEW [names of done tasks] AS
    SELECT tasks.task_id,
           tasks.task_name,
           done_tasks_history.date
      FROM tasks
           INNER JOIN
           done_tasks_history ON tasks.task_id = done_tasks_history.task_id;


-- �������������: view1
CREATE VIEW view1 AS
    SELECT *
      FROM tasks;


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
