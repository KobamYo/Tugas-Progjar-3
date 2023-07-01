import socket
import logging

logging.basicConfig(format='%(message)s', level=logging.WARNING)
def kirim_data(nama=""):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = ("localhost", 45000)
    logging.warning(f"[CLIENT]:: {nama}")
    logging.warning(f"[CLIENT]::OPENING_SOCKET...\t \"{server_address[0]}:{server_address[1]}\"")

    sock.connect(server_address)

    try:
        # Send data
        message = 'TIME\r\n'
        logging.warning(f"[CLIENT]::SENDING...\t\t \"{message[:-2]}\"")
        sock.sendall(message.encode('utf-8'))
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16).decode('utf-8')
            amount_received += len(data)
            logging.warning(f"[SERVER]::RECEIVED...\t\t \"{data}\"")
    finally:
        logging.warning("[CLIENT]::CLOSING_SOCKET...")
        logging.warning("================================================")
        sock.close()
    return
