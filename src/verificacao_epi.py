# Projeto-EPI
# Sistema de verificação dos equipamentos de proteção


def verificar_epi(epis_detectados):

    print("\n================================")
    print("       VERIFICAÇÃO DE EPI")
    print("================================")

    if not epis_detectados:
        print("Nenhum EPI foi identificado.")
        return

    print("EPIs identificados:")

    for epi in epis_detectados:

        if epi == "helmet":
            print("✓ Capacete")

        elif epi == "vest":
            print("✓ Colete")

        else:
            print(f"✓ {epi}")

    print("================================")