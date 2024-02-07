import time

# Configurações da porta serial (ajuste a porta COM conforme necessário)
porta_serial = "COM4"  # Substitua pela porta COM à qual o Arduino está conectado
baud_rate = 9600

try:
    # Abre a conexão serial
    arduino = open(porta_serial, 'r', encoding='utf-8', buffering=1)
    # Aguarda um curto período para garantir que a comunicação serial seja estabelecida
    time.sleep(2)
    while True:
        try:
            caractere = arduino.readline().rstrip()
            print('recived: ', caractere)
        except Exception as e:
            print("Exception:", e)

except KeyboardInterrupt:
    # Encerra a conexão serial ao pressionar Ctrl+C
    arduino.close()
    print("\nConexão serial fechada.")
