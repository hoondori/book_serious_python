
from memory_profiler import profile 

@profile
def read_random():
    ba = bytearray(1024*10000)
    ba_at_1024 = memoryview(ba)[1024:]
    
    with open('/dev/urandom', 'rb') as source:
        source.readinto(ba_at_1024)
        content = ba
        content_to_write = ba_at_1024   # <--- 제로 복사
    print('Content length: %d, content to write length: %d' % (len(content), len(content_to_write)))
    
    with open('/dev/null', 'wb') as target:
        target.write(content_to_write)
        
if __name__ == "__main__":
    read_random()  