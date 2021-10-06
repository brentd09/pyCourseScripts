class Staff:
  def __init__(self,SPosition,SName,SPay):
    self.position = SPosition
    self.name = SName
    self.pay = SPay
    print('Creating staff member')

  def __str__(self):
    return 'Position = {}, Name = {}, Pay = {}'.format(self.position,self.name,self.pay)

  def CalculatePay(self):
    prompt = '\nEnter the number og hours worked for {} '.format(self.name)
    hours = input(prompt)
    prompt = 'Enter the hourly rate for {} '.format(self.name)
    hourlyrate = input(prompt)
    self.pay = int(hours) * int(hourlyrate)

OfficeStaff = Staff('Admin','Betty',0)
print(OfficeStaff.CalculatePay())
print(OfficeStaff)