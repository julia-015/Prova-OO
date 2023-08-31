from Classes import *



def main():
    
    while True:
        try:

            print("Bem Vindo(a) a sua ToDoList! \n\n O que deseja realizar? \n\n [1] Adicionar Tarefa \n [2] Excluir Tarefa \n [3] Listar tarefas \n [4] Sair \n")
            menu = int(input(">> "))


            match menu:

                case 1:
                    pass

                case 2:
                    pass

                case 3:
                    pass

                case 4:
                    pass

                case _:
                    print("Valor Inválido.")
                    print("---------------")


        except Exception as erro:
            print("Valor Inválido")
            print(erro.__class__.__name__)
            print("")