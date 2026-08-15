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


                                                                if __name__ == "__main__":
                                                                    main()