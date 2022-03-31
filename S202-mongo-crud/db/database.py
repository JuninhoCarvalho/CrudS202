import pymongo

class Database:
    def __init__(self, database, collection, dataset=None):
        connectionString = "mongodb+srv://adm:adm@cluster0.ktkjq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.clusterConnection = pymongo.MongoClient(
            connectionString,
            # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
            tlsAllowInvalidCertificates=True
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]
        if dataset:
            self.dataset = dataset

    def resetDatabase(self):
        self.db.drop_collection(self.collection)
        self.collection.insert_many(self.dataset)

    def create(self, nome, idade):
        return self.collection.insert_one({"nome": nome, "idade": idade})

    def createLivro(self, id, titulo, autor, ano, preco):
        return self.collection.insert_one({"id": id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco})    

    def read(self):
        return self.collection.find({})

    def update(self, nome, idade):
        return self.collection.update_one(
            {"nome": nome},
            {
                "$set": {"idade": idade},
                "$currentDate": {"lastModified": True}
            }
        )

    def updateLivro(self, titulo, preco):
        return self.collection.update_one(
            {"titulo": titulo},
            {
                "$set": {"preco": preco},
                "$currentDate": {"lastModified": True}
            }
        )

    def delete(self, nome):
        return self.collection.delete_one({"nome": nome})

    def deleteLivro(self, titulo):
        return self.collection.delete_one({"titulo": titulo})
