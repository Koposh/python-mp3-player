# Importa da biblioteca do playsound o playsound.
from playsound import playsound


# define uma função com o nome "musica" que será substituida pela  e retorna executa a música com o "playsound(musica)"
def musica(musica):
    return playsound(musica)


# Manda o usuário especificar o caminho da música, e converte em string.
esc = str(input("Digite o caminho da musica a ser tocada: "))

# Se o programa funcionar irá pegar a música do usuario definida como "esc" e passar pela função "musica"
try:
    musica(esc)

# Se o programa não encontrar o caminho da música especificado, ou der algum erro no programa.

except Exception:
    print("Música não encontrada, por favor tente novamente.")
