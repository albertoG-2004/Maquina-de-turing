import tkinter as tk
from turingMachine import TuringMachine

class AutomataInterfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina de Turing - Verificación de Cadenas")
        self.root.geometry("400x300")
        self.root.configure(bg="#2c3e50")

        self.title_label = tk.Label(
            root, text="Máquina de Turing", font=("Helvetica", 20, "bold"), bg="#2c3e50", fg="#ecf0f1"
        )
        self.title_label.pack(pady=20)

        self.label = tk.Label(
            root, text="Ingresa la cadena a analizar:",
            font=("Helvetica", 12), bg="#2c3e50", fg="#bdc3c7"
        )
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 12))
        self.entry.pack(pady=10)

        self.verify_button = tk.Button(
            root, text="Verificar", font=("Helvetica", 12, "bold"), bg="#3498db", fg="white",
            relief="flat", padx=10, pady=5, command=self.verify_string
        )
        self.verify_button.pack(pady=20)

        self.result_label = tk.Label(
            root, text="", font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1"
        )
        self.result_label.pack(pady=10)

    def verify_string(self):
        input_string = self.entry.get()

        if not isinstance(input_string, str) or not input_string.strip():
            self.show_error_popup("Error: Lo ingresado no es una cadena válida")
            return

        try:
            tm = TuringMachine(list(input_string))
            result = tm.run()
            
            if result:
                self.show_success_popup()
            else:
                self.show_invalid_popup()
        
        except Exception as e:
            self.show_error_popup(f"Error: {str(e)}")

    def show_success_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Resultado")
        popup.geometry("300x150")
        popup.configure(bg="#2c3e50")

        label = tk.Label(
            popup, text="¡Cadena válida!", font=("Helvetica", 14, "bold"), bg="#2c3e50", fg="#ecf0f1"
        )
        label.pack(pady=20)

        close_button = tk.Button(
            popup, text="Cerrar", font=("Helvetica", 12, "bold"), bg="#3498db", fg="white",
            relief="flat", padx=10, pady=5, command=popup.destroy
        )
        close_button.pack(pady=10)

    def show_invalid_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Resultado")
        popup.geometry("300x150")
        popup.configure(bg="#2c3e50")

        label = tk.Label(
            popup, text="¡Cadena inválida!", font=("Helvetica", 14, "bold"), bg="#2c3e50", fg="#ecf0f1"
        )
        label.pack(pady=20)

        close_button = tk.Button(
            popup, text="Cerrar", font=("Helvetica", 12, "bold"), bg="#3498db", fg="white",
            relief="flat", padx=10, pady=5, command=popup.destroy
        )
        close_button.pack(pady=10)

    def show_error_popup(self, message):
        popup = tk.Toplevel(self.root)
        popup.title("Error")
        popup.geometry("300x150")
        popup.configure(bg="#2c3e50")

        label = tk.Label(
            popup, text=message, font=("Helvetica", 12, "bold"), bg="#2c3e50", fg="#e74c3c"
        )
        label.pack(pady=20)

        close_button = tk.Button(
            popup, text="Cerrar", font=("Helvetica", 12, "bold"), bg="#3498db", fg="white",
            relief="flat", padx=10, pady=5, command=popup.destroy
        )
        close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutomataInterfaz(root)
    root.mainloop()