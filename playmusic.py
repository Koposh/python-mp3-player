# Plays the playsound from the playsound library.

from playsound import playsound


# defines a function with the name "music" that will be replaced by and returns plays the song with "playsound (music)"
def musica(musica):
    return playsound(musica)


# The user specifies the song path and converts the string.

esc = str(input("Digite o caminho da musica a ser tocada: "))

# If the program works, it will take the user's music set to "esc" and go through the "music" function

try:
    musica(esc)

# If the program does not find the specified music path, or if there is an error in the program.

except Exception:
    print("Música não encontrada, por favor tente novamente.")
