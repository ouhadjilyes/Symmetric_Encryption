import os , subprocess
import time


# execute simple terminal commands
#os.system("echo hello world")
#os.system('ls')

process = input("Encypt or decrypt enter E/D : ")

print('processing...')
time.sleep(1)

if process == 'E' or process == "e":
    args = ["openssl", "enc", "-aes-256-cbc", "-md" , "sha512", "-pbkdf2"]
    iterations = input("number of iterations ? click enter for default(10000) : ")
    if iterations == "":
        args += ["-iter", "250000", "-salt", "-in"]
    else:
        args.append("-iter")
        args += [str(iterations), "-salt", "-in"]
    path = input("choose file to encrypt (path) : ")
    args.append(str(path))
    output_file = input("name the output file : ")
    args.append("-out")
    args.append(str(output_file))
    my_process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    my_process.communicate() #[0]

elif process == 'D' or process == 'd':
    args = ["openssl", "enc", "-aes-256-cbc", "-md" , "sha512", "-pbkdf2"]
    path = input("choose file to decrypt (path) : ")
    args.append("-in")
    args.append(str(path))
    file_out = input("name the output file (extension required) : ")
    args.append("-out")
    args.append(str(file_out))
    args.append("-d")
    dec_process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    dec_process.communicate()

else:
    print("Bad input !!")

