import multiprocessing
import time  # ✅ Add this!

def fun1():
    for i in '1234':
        time.sleep(0.75)
        print(i, flush=True)
    
def fun2():
    for i in 'abcd':
        time.sleep(1.25)
        print(i, flush=True) # imp** flush=True for coreect output
        

if __name__=='__main__':
    pro1 = multiprocessing.Process(target=fun1)
    pro2 = multiprocessing.Process(target=fun2)

    t1 = time.time()
    pro1.start()
    pro2.start()

    pro1.join()
    pro2.join()

    t2 = time.time()

    print(t2 - t1)
