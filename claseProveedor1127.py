class proveedor1127:
    id_proveedores1127 = 0
    Producto1127 = ""
    Cantidad1127 = 0
    Sucursal1127 = ""
    Num_Telefono1127 = 0
    Correo1127 = ""
    Horario1127 = 0

    def mostrarDatos1127(self):
        print(f" Id del proveedor: {self.id_proveedores1127}")
        print(f" Nombre del producto: {self.Producto1127}")
        print(f" Cantidad: {self.Cantidad1127}")
        print(f" Sucursal: {self.Sucursal1127}")
        print(f" Num. de telefono: {self.Num_Telefono1127}")
        print(f" Correo: {self.Correo1127}")
        print(f" Horario: {self.Horario1127}")
    def Lista_proveedor1127(self):
        id_proveedor = [12567, 17272, 82828, 87654, 848543, 65435, 76554]
        print("Id de los proveedores: ")
        print(id_proveedor) 
        for prov in id_proveedor:
            print (prov)
    def Tupla_Correo(self):
        print("Correos electronicos:")
        Correo = ("Jorge@gmail.com", "Jhon@gmail.com", "Mark@gmail.com", "noob@gmail.com", "Aldo@gmail.com", "Sequi@gmail.com", "Rick@gmail.com" )
        for correo in Correo:
            print(correo)
    def Diccionario_Cantidad(self):
        print("Cantidad de los productos: ")
        Cantidad =	{
    "De la rosa": 32,
    "Nucita": 56,
    "Mazapan": 45,
    "Chocolate": 67,
    "Paleta": 32,
    "Pulparindo": 22,
    "Pelon pelo rico": 49,
}
        print(Cantidad)
        for x,y in Cantidad.items():
            print(x,y)
    def altas1127(self):
        print("\nLa operacion altas se realizo correctamente")
    def bajas1127(self):
        print("La operacion bajas se realizo correctamente\n")

objeto = proveedor1127()

objeto.id_proveedores1127=2345
objeto.Producto1127="Paletas"
objeto.Cantidad1127=32
objeto.Sucursal1127="Sucursal No 214"
objeto.Num_Telefono1127 = 6564871285
objeto.Correo1127="GAbriel@gmail.com"
objeto.Horario1127="12:30 am a 6:00pm"

print("\nDatos de lista")
objeto.Lista_proveedor1127()
print("\nDatos de tupla")
objeto.Tupla_Correo()
print("\nDatos de diccionario")
objeto.Diccionario_Cantidad()

objeto.altas1127()
objeto.bajas1127()
