import socket
from .models import ZPLLabel


def send_to_print(str_to_print):
    _send_to_print(_create_zpl_label(str_to_print))


def _send_to_print(zpl_str):
    sock = socket.socket()
    sock.connect(('10.21.8.33', 6101))
    cmd = bytes(zpl_str.encode('utf8'))
    sock.send(cmd)
    sock.close()


def _create_zpl_label(barcode):
    label = ZPLLabel(20, 30)
    label.origin(11, 3)
    label.append_code("^BY1")
    label.write_barcode(height=140, barcode_type='C', print_interpretation_line='N')
    label.write_text(barcode)
    label.endorigin()
    return label.dumpZPL()
