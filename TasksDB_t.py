import datetime #datetime.datetime.now()

class TasksDB_t: #model #экземпляр этого класса будет один на всю программу (если я не захочу одновременно открывать несколько БД)
	def __init__(self):
		self.tasks_list = []
		self.last_id = 0
		
		self.tasks_done_history = [] # [(id, дата-время)]
	
	def addTask(self, name, isEveryday, reward, mulct=0):
		self.last_id+=1
		self.tasks_list.append( Task(self.last_id, name, isEveryday, reward, mulct) )
		
	def doneTask(self, id):
		# Если эта задача Everyday, то проверять не была ли она уже выполнена сегодня
		self.tasks_done_history.append( (id, datetime.datetime.now()) )
		
	def testDB(self):
		if len(self.tasks_list) <= self.last_id: print("Test 1 is OK :)")
		else: print("Error Test 1 >:(")
		
	#def save(self):

	#def load(self):
		#self = pickle.load(file) # А так вообще можно?

class Task:
	def __init__(self, id, name, isEveryday, reward, mulct):
		self.id = id
		self.name = name
		self.isEveryday = isEveryday
		self.reward = reward
		self.mulct = mulct #fine - шраф
		#verision ?