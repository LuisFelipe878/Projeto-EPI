# Projeto-EPI
# Sistema de identificação de Equipamentos de Proteção Individual
# Desenvolvido por Luis Felipe - IFG

import os
from ultralytics import YOLO
from verificacao_epi import verificar_epi


# Caminho do modelo treinado
CAMINHO_MODELO = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "best.pt"
)


def analisar_imagem(caminho_imagem):
    """
    Analisa uma imagem utilizando o modelo YOLO
    treinado para identificação de EPI.
    """

    if not os.path.exists(CAMINHO_MODELO):
        print("❌ Modelo best.pt não encontrado.")
        return

    if not os.path.exists(caminho_imagem):
        print("❌ Imagem não encontrada.")
        return

    print("\nCarregando modelo...")
    modelo = YOLO(CAMINHO_MODELO)

    print("Analisando imagem...")

    resultado = modelo.predict(
        source=caminho_imagem,
        conf=0.25,
        iou=0.45,
        verbose=False
    )[0]

    epis_detectados = []

    # Verificar objetos detectados
    for caixa in resultado.boxes:

        classe = int(caixa.cls[0])
        confianca = float(caixa.conf[0])
        nome = resultado.names[classe].lower()

        # Ignorar a pessoa
        if nome == "person":
            continue

        # Guardar somente EPIs
        if nome in ["helmet", "vest"]:
            if nome not in epis_detectados:
                epis_detectados.append(nome)

            print(
                f"EPI detectado: {nome} "
                f"(confiança: {confianca:.2%})"
            )

    # Enviar os EPIs para o sistema de verificação
    verificar_epi(epis_detectados)

    return epis_detectados


def main():

    print("================================")
    print("          PROJETO-EPI")
    print("================================")
    print("Sistema de identificação de EPI")
    print()

    caminho_imagem = input(
        "Digite o caminho da imagem: "
    )

    analisar_imagem(caminho_imagem)


if __name__ == "__main__":
    main()
