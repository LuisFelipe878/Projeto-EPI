# Classes de Equipamentos de Proteção Individual
# Projeto-EPI
# Desenvolvido por Luis Felipe - IFG

EPIS = [
    "capacete",
        "colete",
            "oculos",
                "luvas",
                    "botas"
                
                        ]

                        CLASSE_PESSOA = "pessoa"


                        def listar_classes():
                            """Retorna todas as classes que o Projeto-EPI deverá identificar."""
                                return [CLASSE_PESSOA] + EPIS


                                if __name__ == "__main__":
                                    print("================================")
                                        print("          PROJETO-EPI")
                                            print("================================")
                                                print("Classes de detecção:")
                                                    
                                                        for classe in listar_classes():
                                                                print(f"- {classe}")
