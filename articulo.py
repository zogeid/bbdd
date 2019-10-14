class Articulo:

    def __init__(self, codigo, familia, proveedor, margen, tipoImpuesto,
                 refArtProveedor, fCompra, precioCompra, precioVenta):
        self.codigo = codigo  # id
        self.familia = familia  # numerico y buscas
        self.proveedor = proveedor  # numerico y buscar
        self.margen = margen  # %
        self.tipoImpuesto = tipoImpuesto  # Joyeria 21%, Plata 26,2% y Reloj 26,2%
        self.refArtProveedor = refArtProveedor  # numerico y buscar
        self.fCompra = fCompra
        self.precioCompra = precioCompra
        self.precioVenta = precioVenta

    def imprimir(self):
        print(int(self.codigo))
        print(self.familia)
        print(self.proveedor)
        print(self.margen)
        print(self.tipoImpuesto)
        print(self.refArtProveedor)
        print(self.fCompra)
        print(self.precioCompra)
        print(self.precioVenta)
