# Punto de entrada del programa
from services.user_service import create_user, read_user, update_user, delete_user, list_users, activate_user_by_email, email_exists
from utils.helpers import is_valid_email, is_valid_password
import os

def menu():
    print("\n--- CRUD de Usuarios ---")
    print("1. Crear usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario por ID")
    print("4. Actualizar usuario")
    print("5. Eliminar usuario")
    print("6. Activar usuario")
    print("0. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        os.system('clear')
        if opcion == "1":
            email = input("Email: ")
            if not is_valid_email(email):
                print("Email inválido.")
                continue
            if email_exists(email):
                print("El email ya está registrado.")
                continue
            password = input("Password: ")
            
            if not is_valid_password(password):
                print("Password debe tener al menos 6 caracteres.")
                continue
            user = create_user(email, password)
            print(f"Usuario creado con ID: {user.user_id}")
        elif opcion == "2":
            users = list_users()
            if not users:
                print("No hay usuarios registrados.")
            for user in users:
                print(f"ID: {user['id']}, Email: {user['email']}")
        elif opcion == "3":
            user_id = input("Ingrese el ID del usuario: ")
            user = read_user(user_id)
            if user:
                print(f"ID: {user['id']}, Email: {user['email']}")
            else:
                print("Usuario no encontrado.")
        elif opcion == "4":
            user_id = input("ID del usuario a actualizar: ")
            email = input("Nuevo email (dejar vacío para no cambiar): ")
            password = input("Nuevo password (dejar vacío para no cambiar): ")
            if email and not is_valid_email(email):
                print("Email inválido.")
                continue
            if email_exists(email):
                print("El email ya está registrado.")
                continue
            if password and not is_valid_password(password):
                print("Password debe tener al menos 6 caracteres.")
                continue
            user = update_user(user_id, email if email else None, password if password else None)
            if user:
                print("Usuario actualizado.")
            else:
                print("Usuario no encontrado.")
        elif opcion == "5":
            user_id = input("ID del usuario a eliminar: ")
            if delete_user(user_id):
                print("Usuario eliminado.")
            else:
                print("Usuario no encontrado.")
        elif opcion == "6":
            email = input("Ingrese el correo electrónico del usuario a activar: ")
            if not is_valid_email(email):
                print("Email inválido.")
                continue
            if activate_user_by_email(email):
                print("Usuario activado exitosamente.")
            else:
                print("Usuario no encontrado o ya está activo.")
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
