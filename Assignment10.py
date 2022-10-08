class CellPhone:
    colour = ''
    width = ''
    height = ''
    weight = ''
    resolution = ''

    def set_colour(self, colour):
        self.colour = colour
    
    def get_colour(self):
        return self.colour

    def set_width(self, width):
        self.width = width
    
    def get_width(self):
        return self.width
    
    def set_height(self, height):
        self.height = height
    
    def get_height(self):
        return self.height

    def set_weight(self, weight):
        self.weight = weight
    
    def get_weight(self):
        return self.weight

    def set_resolution(self, resolution):
        self.resolution = resolution
    
    def get_resolution(self):
        return self.resolution

    def receive_message(self):
        print('The phone has just received a message.')
    
    def send_message(self):
        print('The phone has just sent a message.')
    
    def make_a_call(self):
        print('The phone is making a call.')

    def answer_a_call(self):
        print('The phone is answering a call.')

# Creating an object for the cell phone class
cellPhone12 = CellPhone()


# Setting attributes using the object
cellPhone12.set_colour('silver colour')
cellPhone12.set_width('60 millimetre width')
cellPhone12.set_height('130 millimetre height')
cellPhone12.set_weight('200 grams weight')
cellPhone12.set_resolution('3040x1440 resolution')


# Getting attributes using the object
print(cellPhone12.get_colour())
print(cellPhone12.get_width())
print(cellPhone12.get_height())
print(cellPhone12.get_weight())
print(cellPhone12.get_resolution())


# Running the behaviour methods using the object
cellPhone12.receive_message()
cellPhone12.send_message()
cellPhone12.make_a_call()
cellPhone12.answer_a_call()
