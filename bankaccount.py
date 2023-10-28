class bankAccount:
	def __init__(self,name,surname,AFM):
		self.name=name
		self.surname=surname
		self.AFM=AFM
		self.ypoloipo=0
	def analypsi(self,poso):
		poso=int(poso)
		self.ypoloipo=self.ypoloipo-poso
		return self.ypoloipo	
	def katathesi(self,poso):
		poso=int(poso)
		self.ypoloipo+=poso
		return self.ypoloipo
	def enimerwsi(self):
		return self.name,self.surname,self.AFM,self.ypoloipo

ba1=bankAccount('Panos','Simianakis','0218388655')
ba1.katathesi(800)
print(ba1.analypsi(200))
			
