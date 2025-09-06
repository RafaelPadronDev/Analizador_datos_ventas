class Venta:
    def __init__(self,producto,cantidad,precio_unitario):
        self.producto=producto
        self.cantidad=cantidad
        self.precio_unitario=precio_unitario
    
    def obtener_valor_total(self):
        return self.cantidad*self.precio_unitario

class Analizador_Ventas:
    def __init__(self):
        self.ventas=[]
    
    def cargar_datos(self,datos_crudos):
        for venta_dict in datos_crudos:
            nueva_venta = Venta(
                producto=venta_dict["producto"],
                cantidad=venta_dict["cantidad"],
                precio_unitario=venta_dict["precio_unitario"]
            )
            self.ventas.append(nueva_venta)

    def obtener_venta_total_del_dia(self):
        suma=0
        for venta in self.ventas:
            suma+=venta.obtener_valor_total()
        return suma
    
    def obtener_producto_mas_vendido(self):
        total_productos={}
        for venta in self.ventas:
            if venta.producto not in total_productos:
                total_productos[venta.producto]=venta.cantidad
            else:
                total_productos[venta.producto]+=venta.cantidad

        if not total_productos:
            return None
        
        producto_mas_vendido = max(total_productos, key=total_productos.get)
        return producto_mas_vendido
    
    def generar_reporte(self):
        total_ventas = self.obtener_venta_total_del_dia()
        producto_top = self.obtener_producto_mas_vendido()
        
        print("--- Reporte de Ventas ---")
        print(f"Venta total del día: ${total_ventas:.2f}")
        if producto_top:
            print(f"Producto más vendido: {producto_top}")
        else:
            print("No hay datos de ventas disponibles.")

# Datos tomados como prueba para el codigo
datos_de_prueba = [
        {"producto": "Manzana", "cantidad": 5, "precio_unitario": 2.50},
        {"producto": "Banana", "cantidad": 2, "precio_unitario": 1.75},
        {"producto": "Manzana", "cantidad": 3, "precio_unitario": 2.50},
        {"producto": "Naranja", "cantidad": 1, "precio_unitario": 3.00},
        {"producto": "Banana", "cantidad": 4, "precio_unitario": 1.75}
    ]

analizador_tienda = Analizador_Ventas()

analizador_tienda.cargar_datos(datos_de_prueba)

analizador_tienda.generar_reporte()