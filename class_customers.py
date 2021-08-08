class cliente:
    def __init__(self, name="Cliente", surname="Cliente", dni="0000000A",correo="ninguno" , telefono="000 00 00 00"):
        self.name = name
        self.surname = surname
        self.dni = dni
        self.correo = correo
        self.telefono = telefono

    def show_client(self):
        print(f"name: {self.name} \nsurname: {self.surname} \nDNI: {self.dni} \nCorreo: {self.correo} \nTeléfono: {self.telefono}")
