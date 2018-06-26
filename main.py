#typedef struct {
#	name_task,
#}

class TasksDB_t: #экземпляр этого класса будет один на всю программу (если я не захочу одновременно открывать несколько БД)
	def __init__(self):
		self.tasks_list = []
		self.last_id = 0
	
	def addTask(self, name, isEveryday, reward):
		self.last_id+=1
		self.tasks_list.append( Task(self.last_id, name, isEveryday, reward) )
		

class Task:
	def __init__(self, id, name, isEveryday, reward):
		self.id = id
		self.name = name
		self.isEveryday = isEveryday
		self.reward = reward
	

TasksDB = TasksDB_t()
TasksDB.addTask("get this", True, 5)

print(TasksDB.last_id, TasksDB.tasks_list[0].name)