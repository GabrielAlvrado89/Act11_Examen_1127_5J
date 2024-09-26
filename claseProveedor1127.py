class proveedor1127:
    id_proveedores1127 = 0
    Nombre_Producto1127 = ""
    Cantidad1127 = 0
    Sucursal1127 = ""
    Num_Telefono1127 = 0
    Correo1127 = ""
    Horario1127 = 0
    def mostrarDatos1127(self):
        print(f" Nombre producto: {self.Diccionario_Cantidad}")
    def Lista_proveedor1127(self):
        id_proveedor = [12567, 17272, 82828, 87654, 848543, 65435, 76554]
        print(id_proveedor) 
        for prov in id_proveedor:
            print (prov)
    def Tupla_Correo(self):
        Correo = ("Jorge@gmail.com", "Jhon@gmail.com", "Mark@gmail.com", "noob@gmail.com", "Aldo@gmail.com", "Sequi@gmail.com", "Rick@gmail.com" )
        for correo in Correo:
            print(correo)
    def Diccionario_Cantidad(self):
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
            print("La operacion se realizo correctamente")
    def bajas1127(self):
        print("La operacion se realizo correctamente")

objeto = proveedor1127()
objeto.altas1127()
objeto.bajas1127()
print("")
objeto.Lista_proveedor1127()
print("")
objeto.Tupla_Correo()
print("")
objeto.Diccionario_Cantidad()
