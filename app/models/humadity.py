from config.mongo import MongoDB

class HumadityModels(MongoDB):
    
    def __init__(self):
        super().__init__();
    
    @property
    def humadity_collection(self):
        db = self._database # Database
        my_collections = db['Humadity'] # Collection Name

        return my_collections
    
    def example_insert(self):
        hum_1 = {'humadity':'199','temperature':'55'}
        hum_2 = {'humadity':'73', 'temperature':'45'}

        self.humadity_collection.insert_many([hum_1, hum_2])

    def example_read(self):
        return self.humadity_collection.find()
