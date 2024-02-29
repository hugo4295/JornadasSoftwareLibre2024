import tkinter as tk

def sumar_numeros():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 + num2
    label_resultado.config(text="Resultado: " + str(resultado))

# Crear la ventana principal
root = tk.Tk()
root.title("Suma de dos números")

# Crear los widgets
label_num1 = tk.Label(root, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(root, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

btn_sumar = tk.Button(root, text="Sumar", command=sumar_numeros)
btn_sumar.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

label_resultado = tk.Label(root, text="")
label_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Ejecutar la aplicación
root.mainloop()
