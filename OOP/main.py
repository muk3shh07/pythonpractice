class laptop:
    def __init__(self,Id,name,ram):
        self.Id = Id
        self.name = name
        self.ram = ram
    def  getInfo(self):
        return f"laptop id :{self.Id} laptop name :{self.name} ram:{self.ram}"

o1 = laptop(Id=123,name="Dell",ram=256)
o2 = laptop(Id=132,name="hp",ram=256)
o3 = laptop(Id=134,name="wer",ram=256)
o4 = laptop(Id=145,name="acer",ram=256)

print(o1.getInfo())