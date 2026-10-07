def pedir_nombre():
    name = input("Ingrese su nombre: ")

    if name.isdigit():
        raise ValueError("El nombre no puede ser un número")

    return name


def pedir_edad():
    age = int(input("Ingrese su edad: "))
    return age


def main():
    try:
        name = pedir_nombre()
        age = pedir_edad()

        print(f"Hola {name}, su edad es {age}")

    except ValueError as error:
        if str(error) == "El nombre no puede ser un número":
            print(error)
        else:
            print("Número no válido")


if __name__ == "__main__":
    main()
    