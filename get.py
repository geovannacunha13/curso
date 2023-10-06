class Curso:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

class ListaDeCursos:
    def __init__(self):
        self.cursos = []
    
    def get_curso(self):
        return self.cursos
    
    def get_curso_id(self, id):
        for curso in self.cursos:
            if curso.id == id:
                return curso
        return None
    
    def post_curso(self, id, nome, descricao):
        curso = Curso(id, nome, descricao)
        self.cursos.append(curso)
        return curso
    
    def put_curso(self, id, nome, descricao):
        curso = self.get_curso_id(id)
        if curso:
            curso.nome = nome
            curso.descricao = descricao
            return curso
        return None
    
    def delete_curso(self, id):
        curso = self.get_curso_id(id)
        if curso:
            self.cursos.remove(curso)
            return True
        return False




