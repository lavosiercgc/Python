import serial
import time

# Configurações da porta serial (ajuste a porta COM e a taxa de transmissão conforme necessário)
porta_serial = "COM4"  # Substitua pela porta COM à qual o Arduino está conectado
baud_rate = 9600

# Inicializa a conexão serial
arduino = serial.Serial(porta_serial, baud_rate, timeout=1)

# Aguarda um curto período para garantir que a comunicação serial seja estabelecida
time.sleep(2)

try:
    while True:
        # Lê uma linha da porta serial
        linha = arduino.readline().decode('utf-8').rstrip()
        #meu teste
        #print('lavos :',arduino)

        # Exibe os dados na tela
        print("Recebido: {}".format(linha))

except KeyboardInterrupt:
    # Encerra a conexão serial ao pressionar Ctrl+C
    arduino.close()
    print("\nConexão serial fechada.")
