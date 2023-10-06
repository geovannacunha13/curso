from fastapi import FastAPI, HITPException
from pydantic import BaseModel
# Criar classe curso FastAPI
app = FastAPI()

class curso:
    def __init__(self, id, titulo, aulas, horas, dia):
        self.id = id
        self.titulo = titulo
        self.aulas = aulas
        self.horas = horas
        self.dia = dia

    def mostrar_informacoes(self):
        print(f"ID do Curso: {self.id}")
        print(f"Título do Curso: {self.titulo}")
        print(f"Número de Aulas: {self.aulas}")
        print(f"Horas de Duração: {self.horas}")
        print(f"Dia do Curso: {self.dia}")

    def atualizar_aulas(self, novo_titulo):
        self.titulo = novo_titulo

    def atualizar_aulas(self, novas_aulas):
        self.aulas = novas_aulas

    def atualizar_aulas(self, mostrar_horas):
        self.aulas = mostrar_horas

    def atualizar_aulas(self, novo_dia):
        self.aulas = novo_dia


