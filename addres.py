def ip_add():
    addres = input("Enter your IP address: ")

    parts = addres.split('.')

    A = int(parts[0])
    B = int(parts[1])
    C = int(parts[2])
    D = int(parts[3])

    ORCidre = input("Enter its Mask (e.g., /24 or 255.255.255.0): ")

    if "/" in ORCidre:
        number_after = int(ORCidre[1:])
        zeros = '0' * (32 - number_after)
        ones = '1' * number_after
        AEK = ones + zeros
        
        E = AEK[:8]
        F = AEK[8:16]
        G = AEK[16:24]
        H = AEK[24:32]
        E, F, G, H = int(E, 2), int(F, 2), int(G, 2), int(H, 2)
        
        addr1 = A & E
        addr2 = B & F
        addr3 = C & G
        addr4 = D & H
        
        inverted_mask = (255 - E) & 255
        inverted_mask2 = (255 - F) & 255
        inverted_mask3 = (255 - G) & 255
        inverted_mask4 = (255 - H) & 255
        
        broadcast_address = f"{addr1 | inverted_mask}.{addr2 | inverted_mask2}.{addr3 | inverted_mask3}.{addr4 | inverted_mask4}"
        num_devices = (2 ** (32 - number_after)) - 2
        first_machine = f"{addr1}.{addr2}.{addr3}.{addr4 + 1}"
        broadcast_parts = broadcast_address.split('.')
        last_machine = f"{int(broadcast_parts[0])}.{int(broadcast_parts[1])}.{int(broadcast_parts[2])}.{int(broadcast_parts[3]) - 1}"

    else:
    
        parts2 = ORCidre.split('.')
        E = int(parts2[0])
        F = int(parts2[1])
        G = int(parts2[2])
        H = int(parts2[3])

        addr1 = A & E
        addr2 = B & F
        addr3 = C & G
        addr4 = D & H

        
        broadcast_address = (
            str((E | (255 - E)) & 255) + '.' +
            str((F | (255 - F)) & 255) + '.' +
            str((G | (255 - G)) & 255) + '.' +
            str((H | (255 - H)) & 255)
        )
        host_bits = 32 - (bin(E).count('1') + bin(F).count('1') + bin(G).count('1') + bin(H).count('1'))
        num_devices = 2**host_bits - 2
        first_machine = f"{addr1}.{addr2}.{addr3}.{addr4 + 1}"
        broadcast_parts = broadcast_address.split('.')
        last_machine = f"{int(broadcast_parts[0])}.{int(broadcast_parts[1])}.{int(broadcast_parts[2])}.{int(broadcast_parts[3]) - 1}"
    
    print('0000000000000000000000000000000000000000000000000000000000000000000')
    print(f"The network @ is: {addr1}.{addr2}.{addr3}.{addr4}")
    print(f"The broadcast address is: {broadcast_address}")
    print(f"Number of devices that can be placed in the network: {num_devices}")
    print(f"The address of the first machine is: {first_machine}")
    print(f"The address of the last machine is: {last_machine}")
print('0000000000000000000000000000000000000000000000000000000000000000000')