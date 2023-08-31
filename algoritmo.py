from Classes import *
import os

toDo = ToDoList()

def cancelar_tarefa():
    exc = input("Digite qual tarefa deseja excluir >> ")
    if toDo.excluir_tarefa(exc):
        print(f"Tarefa {exc} foi excluida.")
    else:
        print(f"Não foi encontrada essa tarefa {exc}.")

def main():
    
    sair = False
    while sair == False:
        try:

            print("Bem Vindo(a) a sua ToDoList! \n\n O que deseja realizar? \n\n [1] Adicionar Tarefa \n [2] Excluir Tarefa \n [3] Listar tarefas \n [0] Sair \n")
            menu = int(input(">> "))


            match menu:

                case 1:
                    os.system("cls")
                    print("Você está prestes a adicionar uma nova tarefa!")
                    toDo.adicionar_tarefa()
                    os.system("pause")
                    os.system("cls")

                case 2:
                    os.system("cls")
                    print("Você está prestes a excluir uma tarefa!")
                    toDo.listar_tarefas()
                    toDo.excluir_tarefa()
                    os.system("pause")
                    os.system("cls")

                case 3:
                    os.system("cls")
                    print("Tarefas:")
                    toDo.listar_tarefas()
                    os.system("pause")
                    os.system("cls")

                case 0:
                    print("SAINDO...")
                    print("---------")
                    sair = True

                case _:
                    print("Valor Inválido.")
                    print("---------------")


        except Exception as erro:
            print("Valor Inválido")
            print(erro.__class__.__name__)
            print("")