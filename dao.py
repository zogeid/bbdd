from articulo import *
from tkinter import *
from tkinter import ttk
import sqlite3




def leer_todos():
    try:
        conn = sqlite3.connect(path + db)
        c = conn.cursor()
        c.execute("select * from articulo;")
        print(c.fetchall())

    except ValueError as err:
        print(err)
    finally:
        conn.close()


def leer_uno(codigo):
    try:
        conn = sqlite3.connect(path + db)
        c = conn.cursor()
        select = "select * from articulo a WHERE codigo = " + codigo + ";"
        c.execute(select)
        print(c.fetchall())

    except ValueError as err:
        print(err)
    finally:
        conn.close()


def insert():

    try:
        articulo = Articulo(codigo.get(), familia.get(), precioCompra.get(), fCompra.get(), refArtProveedor.get(),
                            tipoImpuesto.get(), margen.get(), proveedor.get(), precioVenta.get())
        conn = sqlite3.connect(path + db)
        c = conn.cursor()
#        c.execute("select * from articulo;")
        c.execute("DROP TABLE articulo;")
        c.execute("CREATE TABLE articulo (codigo number, familia number, precioCompra number, fCompra number, "
                  "refArtProveedor number, tipoImpuesto number, margen number, proveedor number, precioVenta number);")

        insert = "insert into articulo (codigo, familia, precioCompra, fCompra, refArtProveedor, tipoImpuesto, margen, proveedor, precioVenta) " \
                 "values (" + articulo.codigo + ", " + articulo.familia + ", " + articulo.precioCompra + ", " + articulo.fCompra + ", " + articulo.refArtProveedor + ", "\
                 + articulo.tipoImpuesto + ", " + articulo.margen + ", " + articulo.proveedor + ", " + articulo.precioVenta +");"
        print(insert)
        c.execute(insert)
        conn.commit()

    except ValueError as err:
        print(err)
    finally:
        conn.close()


# windowConfig 1
root = Tk()
root.title("Alta articulo")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# variables
path = r"C:\Users\dalares\PycharmProjects\SQLITE"
db = "joyeria.db"
codigo = StringVar()
familia = StringVar()
proveedor = StringVar()
margen = StringVar()
tipoImpuesto = StringVar()
refArtProveedor = StringVar()
fCompra = StringVar()
precioCompra = StringVar()
precioVenta = StringVar()
articulo = Articulo(codigo.get(), familia.get(), precioCompra.get(), fCompra.get(), refArtProveedor.get(),
                                    tipoImpuesto.get(), margen.get(), proveedor.get(), precioVenta.get())


ttk.Label(mainframe, text="Código").grid(column=1, row=1, sticky=(W, E))
input_codigo = ttk.Entry(mainframe, width=7, textvariable=codigo)
input_codigo.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Familia").grid(column=1, row=2, sticky=(W, E))
input_familia = ttk.Entry(mainframe, width=7, textvariable=familia)
input_familia.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Proveedor").grid(column=1, row=3, sticky=(W, E))
input_proveedor = ttk.Entry(mainframe, width=7, textvariable=proveedor)
input_proveedor.grid(column=2, row=3, sticky=(W, E))

ttk.Label(mainframe, text="Margen").grid(column=1, row=4, sticky=(W, E))
input_margen = ttk.Entry(mainframe, width=7, textvariable=margen)
input_margen.grid(column=2, row=4, sticky=(W, E))

ttk.Label(mainframe, text="Tipo de impuesto").grid(column=1, row=5, sticky=(W, E))
input_tipoImpuesto = ttk.Entry(mainframe, width=7, textvariable=tipoImpuesto)
input_tipoImpuesto.grid(column=2, row=5, sticky=(W, E))

ttk.Label(mainframe, text="Ref. art. proveedor").grid(column=1, row=6, sticky=(W, E))
input_refArtProveedor = ttk.Entry(mainframe, width=7, textvariable=refArtProveedor)
input_refArtProveedor.grid(column=2, row=6, sticky=(W, E))

ttk.Label(mainframe, text="Fecha compra").grid(column=1, row=7, sticky=(W, E))
input_fCompra = ttk.Entry(mainframe, width=7, textvariable=fCompra)
input_fCompra.grid(column=2, row=7, sticky=(W, E))

ttk.Label(mainframe, text="Precio de compra").grid(column=1, row=8, sticky=(W, E))
input_precioCompra = ttk.Entry(mainframe, width=7, textvariable=precioCompra)
input_precioCompra.grid(column=2, row=8, sticky=(W, E))

ttk.Label(mainframe, text="Precio de venta").grid(column=1, row=9, sticky=(W, E))
input_precioVenta = ttk.Entry(mainframe, width=7, textvariable=precioVenta)
input_precioVenta.grid(column=2, row=9, sticky=(W, E))

# Buttons
ttk.Button(mainframe, text="Guardar", command=insert).grid(column=2, row=10, sticky=W)

# windowConfig 2
input_codigo.focus()
root.bind('<Return>', insert)

# mainloop
root.mainloop()
