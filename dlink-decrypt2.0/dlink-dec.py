import subprocess

def analyze_with_radare2(bin_file):
    # Command to analyze firmware with Radare2
    r2_cmd = f'r2 -A -qc "aaa; afl" {bin_file}'
    
    try:
        # Run Radare2 command
        output = subprocess.check_output(r2_cmd, shell=True, text=True)
        print("Radare2 Analysis:")
        print(output)
        
        # Extract function addresses from the output
        functions = []
        for line in output.split('\n'):
            if line:
                parts = line.split()
                if len(parts) > 0 and parts[0].startswith('0x'):
                    functions.append(parts[0])
        
        return functions
        
    except subprocess.CalledProcessError as e:
        print(f"Error analyzing firmware with Radare2: {e}")
        return []

def decompile_function_with_radare2(bin_file, func_addr):
    # Command to decompile a specific function with Radare2
    r2_cmd = f'r2 -A -qc "s {func_addr}; pdd" {bin_file}'
    
    try:
        # Run Radare2 command
        output = subprocess.check_output(r2_cmd, shell=True, text=True)
        print(f"Radare2 Decompiled Code for Function {func_addr}:")
        print(output)
        
    except subprocess.CalledProcessError as e:
        print(f"Error decompiling function {func_addr} with Radare2: {e}")

# Main function to prompt user for file and analyze
def main():
    # Prompt user for firmware file path
    firmware_file = input("Enter the path to the firmware file: ").strip()
    
    # Perform analysis using Radare2
    functions = analyze_with_radare2(firmware_file)
    
    # Perform decompilation for each function found
    for func_addr in functions:
        decompile_function_with_radare2(firmware_file, func_addr)

# Entry point of the script
if __name__ == "__main__":
    main()

