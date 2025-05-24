from concurrent.futures import ProcessPoolExecutor
import time

def fun(num):
    time.sleep(1)
    return f'Square of {num} is: {num * num}'

if __name__=='__main__':


    nums = [1, 2, 3, 4, 5]

    with ProcessPoolExecutor(max_workers=3) as executor:
        res = executor.map(fun, nums)
        for r in res:
            print(r)



# import multiprocessing
# import time

# def fun(num):
#     time.sleep(1)
#     print(f'Square of {num} is: {num * num}')

# if __name__ == '__main__':
#     nums = [1, 2, 3, 4, 5]
#     processes = []

#     for num in nums:
#         p = multiprocessing.Process(target=fun, args=(num,))
#         p.start()
#         processes.append(p)

#     # Wait for all processes to finish
#     for p in processes:
#         p.join()
