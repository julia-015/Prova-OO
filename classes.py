class ToDoList():
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        tarefas = self.tarefas
        self.descricao = descricao

        self.descricao = input("Digite sua nova tarefa >> ")
        tarefas.append(self.descricao)

        print(f"A tarefa: {self.descricao} foi adicionada a sua ToDoList!")

    def excluir_tarefa(self, indice):
        self.indice = indice

        self.indice = input("Digite qual tarefa deseja excluir >> ")

    def listar_tarefas(self):
        self.tarefas.items()