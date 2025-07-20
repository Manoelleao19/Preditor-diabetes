import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font
import joblib
import numpy as np
from utils import interpretar_resultado

# Configurações de estilo
COR_PRIMARIA = "#2c3e50"
COR_SECUNDARIA = "#3498db"
COR_TERCIARIA = "#ecf0f1"
COR_TEXTO = "#2c3e50"
COR_FUNDO = "#f9f9f9"
FONTE_TITULO = ("Arial", 16, "bold")
FONTE_CAMPOS = ("Arial", 10)
FONTE_BOTAO = ("Arial", 10, "bold")

# Carregar modelo
modelo = joblib.load('../modelos/modelo_diabetes.pkl')


class AplicacaoDiabetes:
    def __init__(self, root):
        self.root = root
        self.configurar_janela()
        self.criar_widgets()

    def configurar_janela(self):
        self.root.title("Sistema de Predição de Diabetes")
        self.root.geometry("600x650")
        self.root.resizable(True, True)
        self.root.configure(bg=COR_FUNDO)
        self.root.minsize(500, 600)

        # Centralizar janela
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        position_right = int(self.root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.root.winfo_screenheight() / 2 - window_height / 2)
        self.root.geometry(f"+{position_right}+{position_down}")

    def criar_widgets(self):
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Cabeçalho
        self.cabecalho = ttk.Frame(self.main_frame)
        self.cabecalho.pack(fill=tk.X, pady=(0, 20))

        self.titulo = tk.Label(
            self.cabecalho,
            text="Predição de Diabetes",
            font=FONTE_TITULO,
            bg=COR_FUNDO,
            fg=COR_PRIMARIA
        )
        self.titulo.pack(side=tk.TOP)

        self.subtitulo = tk.Label(
            self.cabecalho,
            text="Preencha os dados clínicos para análise",
            font=("Arial", 10),
            bg=COR_FUNDO,
            fg=COR_TEXTO
        )
        self.subtitulo.pack(side=tk.TOP)

        # Frame de formulário com scrollbar
        self.canvas = tk.Canvas(self.main_frame, bg=COR_FUNDO, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Campos do formulário
        self.campos = [
            "Nº de gestações",
            "Glicose (mg/dL)",
            "Pressão sanguínea (mmHg)",
            "Espessura da pele (mm)",
            "Insulina (µU/mL)",
            "IMC (kg/m²)",
            "Função Pedigree Diabetes",
            "Idade (anos)"
        ]

        self.entradas = []
        for i, campo in enumerate(self.campos):
            frame_campo = ttk.Frame(self.scrollable_frame)
            frame_campo.pack(fill=tk.X, padx=10, pady=5)

            label = tk.Label(
                frame_campo,
                text=campo,
                width=25,
                anchor="w",
                font=FONTE_CAMPOS,
                bg=COR_FUNDO,
                fg=COR_TEXTO
            )
            label.pack(side=tk.LEFT)

            entrada = ttk.Entry(
                frame_campo,
                font=FONTE_CAMPOS
            )
            entrada.pack(side=tk.RIGHT, expand=True, fill=tk.X)
            self.entradas.append(entrada)

        # Frame do botão
        self.btn_frame = ttk.Frame(self.main_frame)
        self.btn_frame.pack(fill=tk.X, pady=20)

        self.btn_prever = tk.Button(
            self.btn_frame,
            text="Realizar Predição",
            command=self.prever,
            bg=COR_SECUNDARIA,
            fg="white",
            font=FONTE_BOTAO,
            bd=0,
            padx=20,
            pady=10,
            activebackground="#2980b9",
            activeforeground="white"
        )
        self.btn_prever.pack()

        # Rodapé
        self.rodape = tk.Label(
            self.main_frame,
            text="© 2023 Sistema de Predição de Diabetes - Fins educacionais",
            font=("Arial", 8),
            bg=COR_FUNDO,
            fg="gray"
        )
        self.rodape.pack(side=tk.BOTTOM, pady=10)

    def prever(self):
        try:
            entrada = [float(e.get()) for e in self.entradas]
            prob = modelo.predict_proba([entrada])[0][1] * 100
            self.mostrar_resultado(prob)
        except ValueError:
            messagebox.showerror(
                "Erro de Validação",
                "Por favor, preencha todos os campos com valores numéricos válidos.",
                parent=self.root
            )

    def mostrar_resultado(self, probabilidade):
        # Criar janela de resultado
        result_window = tk.Toplevel(self.root)
        result_window.title("Resultado da Predição")
        result_window.geometry("450x400")
        result_window.resizable(False, False)

        # Configurar cores com base no risco
        if probabilidade > 70:
            cor_fundo = "#ffebee"  # Vermelho claro
            cor_texto = "#c62828"
        elif probabilidade > 40:
            cor_fundo = "#fff8e1"  # Amarelo claro
            cor_texto = "#f57f17"
        else:
            cor_fundo = "#e8f5e9"  # Verde claro
            cor_texto = "#2e7d32"

        result_window.configure(bg=cor_fundo)

        # Frame principal
        main_frame = ttk.Frame(result_window, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Ícone (simulado com texto)
        tk.Label(
            main_frame,
            text="⚕",
            font=("Arial", 40),
            bg=cor_fundo,
            fg=cor_texto
        ).pack(pady=10)

        # Valor da probabilidade
        tk.Label(
            main_frame,
            text=f"{probabilidade:.1f}%",
            font=("Arial", 36, "bold"),
            bg=cor_fundo,
            fg=cor_texto
        ).pack()

        # Classificação
        interpretacao = interpretar_resultado(probabilidade)
        tk.Label(
            main_frame,
            text=interpretacao,
            font=("Arial", 12),
            bg=cor_fundo,
            fg=cor_texto
        ).pack(pady=10)

        # Barra de progresso visual
        canvas = tk.Canvas(
            main_frame,
            width=300,
            height=20,
            bg=cor_fundo,
            highlightthickness=0
        )
        canvas.pack(pady=10)

        # Desenhar barra
        largura_barra = (probabilidade / 100) * 300
        canvas.create_rectangle(
            0, 0, largura_barra, 20,
            fill=cor_texto,
            outline=""
        )

        # Recomendações
        frame_recomendacoes = ttk.Frame(main_frame)
        frame_recomendacoes.pack(fill=tk.X, pady=10)

        tk.Label(
            frame_recomendacoes,
            text="Recomendações:",
            font=("Arial", 10, "underline"),
            bg=cor_fundo,
            fg=cor_texto
        ).pack(anchor="w")

        recomendacoes = self.gerar_recomendacoes(probabilidade)
        tk.Label(
            frame_recomendacoes,
            text=recomendacoes,
            font=("Arial", 10),
            bg=cor_fundo,
            fg=cor_texto,
            wraplength=400,
            justify="left"
        ).pack(anchor="w", fill=tk.X)

        # Botão de fechar
        ttk.Button(
            main_frame,
            text="Fechar",
            command=result_window.destroy
        ).pack(pady=5)

    def gerar_recomendacoes(self, probabilidade):
        if probabilidade > 70:
            return ("Recomenda-se consulta médica urgente. Realize exames de glicemia em jejum "
                    "e hemoglobina glicada. Mantenha acompanhamento médico regular e adote "
                    "mudanças imediatas na dieta e atividade física.")
        elif probabilidade > 40:
            return ("Recomenda-se acompanhamento médico preventivo. Monitore seus níveis de "
                    "glicose regularmente. Adote hábitos alimentares saudáveis e pratique "
                    "atividades físicas pelo menos 3 vezes por semana.")
        else:
            return ("Seu risco atual é baixo. Mantenha hábitos saudáveis como alimentação "
                    "balanceada e prática regular de exercícios. Consulte um médico "
                    "anualmente para check-ups preventivos.")


# Inicializar aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacaoDiabetes(root)
    root.mainloop()