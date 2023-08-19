import manuf

def get_vendor(mac_address):
    try:
        p = manuf.MacParser()
        vendor_name = p.get_manuf(mac_address)
        return vendor_name
    except manuf.MacParserError:
        return "Error al obtener el nombre del vendedor."

if __name__ == "__main__":
    # Banner en ASCII
    banner = r"""
___  ___  ___  _____   _     _____  _____ _   ___   _______ 
|  \/  | / _ \/  __ \ | |   |  _  ||  _  | | / / | | | ___ \
| .  . |/ /_\ \ /  \/ | |   | | | || | | | |/ /| | | | |_/ /
| |\/| ||  _  | |     | |   | | | || | | |    \| | | |  __/ 
| |  | || | | | \__/\ | |___\ \_/ /\ \_/ / |\  \ |_| | |    
\_|  |_/\_| |_/\____/ \_____/\___/  \___/\_| \_/\___/\_|    
                                                            
                                                            
    """

    print(banner)
    
    mac_address = input("Ingresa la dirección MAC: ")
    vendor = get_vendor(mac_address)
    print(f"Vendedor: {vendor}")
