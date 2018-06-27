import pickle

class TasksDB_t: #экземпл€р этого класса будет один на всю программу (если € не захочу одновременно открывать несколько Ѕƒ)
	def __init__(self):
		self.tasks_list = []
		self.last_id = 0
	
	def addTask(self, name, isEveryday, reward):
		self.last_id+=1
		self.tasks_list.append( Task(self.last_id, name, isEveryday, reward) )
		
	def testDB(self):
		if len(self.tasks_list) <= self.last_id: print("Test 1 is OK :)")
		else :  print("Error Test 1 >:(")

class Task:
	def __init__(self, id, name, isEveryday, reward):
		self.id = id
		self.name = name
		self.isEveryday = isEveryday
		self.reward = reward

fileWriteName = "TasksDB"
#commands_list = ["nlat", "exit"]

class Repl:
	def __init__(self):
		self.TasksDB = TasksDB_t()

	def run(self):
		isExit = False
		while not isExit:
			#print('>', end='')
			input_command = input(">")

			if input_command=="nlat" : #nameLastAddTask
				if len(self.TasksDB.tasks_list) != 0:
					print(self.TasksDB.last_id, self.TasksDB.tasks_list[0].name)
				else:
					print("Tasks list is empty!")

			elif input_command=="exit":
				isExit = True

			elif input_command=="save":
				#file = open(fileWriteName, 'wb')
				with open(fileWriteName, 'wb') as file:
					pickle.dump(self.TasksDB, file)
					file.close()

			elif input_command=="load":
				with open(fileWriteName, 'rb') as file:
					self.TasksDB = pickle.load(file)
					file.close()

			else:
				print("Unknown command!")
				#print(commands_list)
	
if __name__ == "__main__":
	Repl().run()