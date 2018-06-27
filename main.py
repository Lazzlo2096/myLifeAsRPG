
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

fileWriteName = "TasksDB"
class Repl:
	
	def __init__(self):
	#---
		self.TasksDB = TasksDB_t()
		self.TasksDB.addTask("get this", True, 5)
	#---
	#print(TasksDB.last_id, TasksDB.tasks_list[0].name)
	
	#commands_list = ["nlat", "exit"]
	
	
	def run(self):
		isExit = False
		while not isExit:
			#print('>', end='')
			input_command = input(">")
			if input_command=="nlat" : #nameLastAddTask
				print(self.TasksDB.last_id, self.TasksDB.tasks_list[0].name)
			elif input_command=="exit":
				isExit = True
			elif input_command=="read":
				pass
			elif input_command=="write":
				#f = open(fileWriteName, 'w')
				#f.write(self.TasksDB);
				pass
			else:
				print("Unknown command!")
				#print(commands_list)
	

if __name__ == "__main__":
	Repl().run()