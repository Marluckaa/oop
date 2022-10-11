class ModelAdmin(object):
    def __init__ (self,name, ID)-> None:
        self.__name = name
        self.__ID = ID
    def introduce(self):
        print('my name is {}'.format(self.__name))
    def getName(self):
        return self.__name
    def _setName(self, new_name):
        self.__name = new_name
        print('{} name changed to {}'.format(self.__name, self.__name)) 
    def getID(self):
        return self.__ID
    def _setID(self, new_ID):
        self.__name = new_ID
        print('{} ID changed to {}'.format(self.__name, self.__name)) 

class Admin(ModelAdmin):
    def __init__ (self, name, ID,permission)-> None:
        super().__init__(name,ID)
        self.__permission = permission
    def introduce(self):
        return super().introduce()

    def SeeInfo(self):
        print()
    def Addpeople():

    def Removepeople():
    
    def FixInformation():
    
    

    def getName(self):
        return super().getName()
    def _setName(self, new_ID):
        return super()._setName(new_ID)
    def getID(self):
        return super().getID()
    def _setID(self, new_ID):
        return super()._setID(new_ID)
    def getPermission(self):
        return self.__permission
    def _setPermission(self):
    
    







class view:
       print("****************************************************************************")
       print("*                                                                          *")
       print("*             Welcome to Hurees hospital system                            *")
       print("*                                                                          *")
       print("****************************************************************************")

       print("choose your mode:")


admin = ModelAdmin('maral','cs21d215')
admin.introduce()