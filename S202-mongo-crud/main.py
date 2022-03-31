from unicodedata import name
from db.database import Database
from helper.WriteAJson import writeAJson

db = Database("db", "Livros")

#db.createLivro(1, "Clean Code", "Robert C. Martin", 2008, 31.0)
#db.createLivro(2, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, 31.0)
#db.createLivro(3, "Harry Potter and The Half Blood Prince", "J.K. Rowling", 2000, 40.0)
#db.createLivro(4, "Harry Potter and The Order of the Phenix", "J.K. Rowling", 2002, 50.0)

db.updateLivro("Clean Code", 100.0)
db.deleteLivro("Harry Potter and The Half Blood Prince")

result = db.read()
writeAJson(result, "Resultado")