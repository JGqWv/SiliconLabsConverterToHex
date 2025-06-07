def txt_to_intel_hex(input_file, output_file):
    # Read the hexadecimal values from the input file
    with open(input_file, 'r') as f:
        hex_values = f.read().splitlines()

    # Prepare to write to the output Intel HEX file
    with open(output_file, 'w') as f:
        # Start address for the data
        address = 0x0000
        # Record type for data
        record_type = 0x00
        
        # Write the data records
        for i in range(0, 0x0020, 16):  # 16 bytes per line
            # Get the next 16 bytes (or less if at the end)
            data_bytes = hex_values[i:i + 16]
            data_bytes = [byte for byte in data_bytes if byte]  # Remove empty strings
            
            # Create the data record
            data_length = len(data_bytes)
            if data_length == 0:
                continue
            
            # Convert hex strings to bytes
            data = ''.join(data_bytes)
            data_length_hex = f"{data_length:02X}"
            data_hex = ''.join(data_bytes)
            
            # Calculate checksum
            record = f":{data_length_hex}{address:04X}{record_type:02X}{data_hex}"
            checksum = (-(sum(int(record[i:i+2], 16) for i in range(1, len(record), 2))) & 0xFF)
            checksum_hex = f"{checksum:02X}"
            
            # Write the record to the file
            f.write(f"{record}{checksum_hex}\n")
            
            # Increment the address
            address += data_length

        # Write the end of file record
        f.write(":00000001FF\n")

# Example usage
input_file = 'firmware'  # Replace with your input file name
output_file = 'output.hex'  # Replace with your desired output file name
txt_to_intel_hex(input_file, output_file)