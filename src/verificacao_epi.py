# Verificação de Equipamentos de Proteção Individual
# Projeto-EPI

from classes_epi import EPIS


def verificar_epi(epi_detectados):
    """
    Verifica quais EPIs foram detectados.
    """

    print("================================")
    print("       VERIFICAÇÃO DE EPI")
    print("================================")

    for epi in EPIS:

        if epi in epi_detectados:
            print(f"✅ {epi}: DETECTADO")
        else:
            print(f"❌ {epi}: NÃO DETECTADO")