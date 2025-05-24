from concurrent.futures import  ThreadPoolExecutor
import time

def fun(number):
    time.sleep(1)
    print( f'this is number : {number}' )


numbers = [1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=4) as executor:
    res = executor.map(fun, numbers)

# print(res)


# Equivalent Code
# import threading
# import time

# def fun(number):
#     time.sleep(1)
#     print(f'this is number : {number}')

# numbers = [1, 2, 3, 4, 5]
# threads = []

# # Manually create and start threads (up to 4 at a time)
# max_workers = 4

# for i in range(0, len(numbers), max_workers):
#     batch = numbers[i:i+max_workers]
#     threads = []

#     for num in batch:
#         t = threading.Thread(target=fun, args=(num,))
#         t.start()
#         threads.append(t)
    
#     # Wait for current batch to finish
#     for t in threads:
#         t.join()
