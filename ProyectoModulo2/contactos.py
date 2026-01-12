# =========================
# Sistema de Gestión de Contactos
# =========================

class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "correo": self.correo,
            "direccion": self.direccion
        }


class AgendaContactos:
    def __init__(self):
        self.contactos = []  # lista de diccionarios

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto.to_dict())
        print("✅ Contacto agregado correctamente.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("📭 No hay contactos guardados.")
            return

        print("\n📒 Lista de contactos:")
        for i, c in enumerate(self.contactos):
            print(f"{i+1}. {c['nombre']} - {c['telefono']}")

    def buscar_contacto(self, dato):
        encontrados = []
        for c in self.contactos:
            if dato.lower() in c["nombre"].lower() or dato in c["telefono"]:
                encontrados.append(c)

        if not encontrados:
            print("❌ No se encontraron contactos.")
        else:
            print("\n🔍 Resultados:")
            for c in encontrados:
                print(c)

    def eliminar_contacto(self, nombre):
        for c in self.contactos:
            if c["nombre"].lower() == nombre.lower():
                self.contactos.remove(c)
                print("🗑️ Contacto eliminado.")
                return
        print("❌ Contacto no encontrado.")

    def editar_contacto(self, nombre):
        for c in self.contactos:
            if c["nombre"].lower() == nombre.lower():
                print("✏️ Deja vacío para mantener el dato actual.")

                nuevo_tel = input("Nuevo teléfono: ")
                nuevo_correo = input("Nuevo correo: ")
                nueva_dir = input("Nueva dirección: ")

                if nuevo_tel:
                    c["telefono"] = nuevo_tel
                if nuevo_correo:
                    c["correo"] = nuevo_correo
                if nueva_dir:
                    c["direccion"] = nueva_dir

                print("✅ Contacto actualizado.")
                return

        print("❌ Contacto no encontrado.")


# =========================
# Menú principal
# =========================

def menu():
    agenda = AgendaContactos()

    while True:
        print("\n===== 📞 SISTEMA DE CONTACTOS =====")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Eliminar contacto")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            direccion = input("Dirección: ")

            contacto = Contacto(nombre, telefono, correo, direccion)
            agenda.agregar_contacto(contacto)

        elif opcion == "2":
            agenda.mostrar_contactos()

        elif opcion == "3":
            dato = input("Buscar por nombre o teléfono: ")
            agenda.buscar_contacto(dato)

        elif opcion == "4":
            nombre = input("Nombre del contacto a editar: ")
            agenda.editar_contacto(nombre)

        elif opcion == "5":
            nombre = input("Nombre del contacto a eliminar: ")
            agenda.eliminar_contacto(nombre)

        elif opcion == "6":
            print("👋 Saliendo del programa...")
            break

        else:
            print("❌ Opción inválida.")


# =========================
# Ejecutar programa
# =========================

if __name__ == "__main__":
    menu()