# Projeto-EPI
# Sistema de identificação de Equipamentos de Proteção Individual
# Desenvolvido por Luis Felipe - IFG

from verificacao_epi import verificar_epi


def main():
    print("================================")
        print("          PROJETO-EPI")
            print("================================")
                print("Sistema de identificação de EPI")
                    print()

                        # Resultado temporário para teste.
                            # Futuramente será substituído pelas detecções da IA.
                                epis_detectados = [
                                        "capacete",
                                                "colete",
                                                        "oculos"
                                                            ]

                                                                verificar_epi(epis_detectados)
analisar_imagem("teste_epi.jpg")
def analisar_imagem(caminho_imagem):
    """
    Ponto de entrada para a análise da imagem.
    
    Futuramente, esta função receberá o resultado
    de um modelo de visão computacional especializado em EPI.
    """

    print(f"Imagem selecionada: {caminho_imagem}")
    print("Análise de EPI ainda não conectada ao modelo de IA.")
                   .                                             if __name__ == "__main__":
                                                                    main()
