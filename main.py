import getpass

from compipy import repl


def main() -> None:
    username = getpass.getuser()
    print("********************************************")
    print("**                                        **")
    print("**  -- BIENVENIDO A CATCOMPILER REPL --   **")
    print("**                                        **")
    print("**      /\\_/\\     ¡Miau! Soy Limón,       **")
    print("**     ( o.o )    tu asistente felino.    **")
    print("**      > ^ <     ¡Dame esos tokens!      **")
    print("**                                        **")
    print("********************************************\n")
    print(f"¡Hola {username}! Estás en CatCompiler.")
    print("Escribe algún comando y deja que la magia ocurra...")
    try:
        repl.start()
    except KeyboardInterrupt:
        print("\n¡Miau! Nos vemos. Saliendo de CatCompiler...")


if __name__ == "__main__":
    main()
