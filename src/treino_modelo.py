import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import time
from pathlib import Path


# Configurações de estilo para os prints
class Cores:
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    FIM = '\033[0m'


def treinar_modelo():
    """Função principal para treinar e avaliar o modelo"""
    try:
        # 1. Carregar dados
        inicio_carregamento = time.time()
        print(f"{Cores.AZUL}\n[1/4] Carregando dataset...{Cores.FIM}")

        caminho_dataset = Path('../dados/diabetes.csv')
        if not caminho_dataset.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho_dataset}")

        df = pd.read_csv(caminho_dataset)
        print(f"  → Dataset carregado com {df.shape[0]} registros e {df.shape[1]} features")

        # 2. Pré-processamento
        print(f"{Cores.AZUL}\n[2/4] Pré-processando dados...{Cores.FIM}")

        # Verificar valores nulos
        if df.isnull().sum().any():
            print(f"{Cores.AMARELO}  → Aviso: Dataset contém valores nulos. Preenchendo com medianas...{Cores.FIM}")
            df = df.fillna(df.median())

        # Separar features e target
        X = df.drop("Outcome", axis=1)
        y = df["Outcome"]

        # 3. Divisão treino-teste
        print(f"{Cores.AZUL}\n[3/4] Dividindo dados (treino/teste)...{Cores.FIM}")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=0.2,
            random_state=42,
            stratify=y  # Manter proporção das classes
        )
        print(f"  → Conjunto de treino: {X_train.shape[0]} amostras")
        print(f"  → Conjunto de teste: {X_test.shape[0]} amostras")

        # 4. Treinamento do modelo
        print(f"{Cores.AZUL}\n[4/4] Treinando modelo...{Cores.FIM}")
        modelo = RandomForestClassifier(
            n_estimators=150,
            max_depth=6,
            min_samples_split=5,
            class_weight='balanced',  # Lidar com desbalanceamento
            random_state=42,
            n_jobs=-1  # Usar todos os cores do CPU
        )

        modelo.fit(X_train, y_train)
        tempo_treinamento = time.time() - inicio_carregamento

        # 5. Avaliação
        print(f"\n{Cores.VERDE}✔ Modelo treinado com sucesso! (Tempo total: {tempo_treinamento:.2f}s){Cores.FIM}")

        # Previsões
        y_pred = modelo.predict(X_test)
        y_proba = modelo.predict_proba(X_test)[:, 1]

        # Métricas
        print(f"\n{Cores.AZUL}📊 Métricas de desempenho:{Cores.FIM}")
        print(classification_report(y_test, y_pred, target_names=['Não Diabético', 'Diabético']))

        # Feature importance
        print(f"\n{Cores.AZUL}🔍 Importância das features:{Cores.FIM}")
        for nome, importancia in sorted(zip(X.columns, modelo.feature_importances_), key=lambda x: x[1], reverse=True):
            print(f"  → {nome:<20}: {importancia:.3f}")

        # 6. Salvamento
        caminho_modelo = Path('../modelos/modelo_diabetes.pkl')
        caminho_modelo.parent.mkdir(exist_ok=True)

        joblib.dump(modelo, caminho_modelo)
        print(f"\n{Cores.VERDE}💾 Modelo salvo em: {caminho_modelo}{Cores.FIM}")

        return modelo

    except Exception as e:
        print(f"\n{Cores.AMARELO}⚠ Erro durante o treinamento: {e}{Cores.FIM}")
        return None


if __name__ == "__main__":
    print(f"{'=' * 50}")
    print(f"{' TREINAMENTO DO MODELO DE DIABETES ':.^50}")
    print(f"{'=' * 50}")

    modelo_treinado = treinar_modelo()

    if modelo_treinado is not None:
        print("\nProcesso concluído com sucesso!")
    else:
        print("\nFalha no treinamento do modelo.")