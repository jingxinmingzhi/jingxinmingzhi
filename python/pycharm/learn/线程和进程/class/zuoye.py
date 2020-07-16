import turtle
class MyRectangle:
    def __init__(self,x=0,y=0,width=100,height=100):
        self.__x=x
        self.__y =y
        self.__width = width
        self.__height = height
    def getArea(self):
        print('面积是：{0}'.format(self.__width*self.__height))
    def getPerimeter(self):
        print('周长是：{0}'.format(2*(self.__width + self.__height)))
    def draw(self):
        turtle.penup()
        turtle.goto(self.__x,self.__y)
        turtle.pendown()
        turtle.goto(self.__x+self.__width,self.__y)
        turtle.goto(self.__x + self.__width, self.__y+self.__height)
        turtle.goto(self.__x , self.__y + self.__height)
        turtle.goto(self.__x, self.__y)
        turtle.done()
MR=MyRectangle(2,3)
MR.getArea()
MR.getPerimeter()
MR.draw()





