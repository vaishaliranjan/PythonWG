from multiprocessing import Process
####### SINGLE THREAD
import time
def ask_user():
	start = time.time()
	user_input = input('Enter your name: ')
	greet = f'Hello, {user_input}'
	print(greet)
	print('ask_user: ', time.time() - start)

def complex_calculation():
	print('Started calculating...')
	start = time.time()
	[x**2 for x in range(20000000)]
	print('complex_calculation: ', time.time() - start)


# With a single thread, we can do one at a time—e.g.
# start = time.time()
# ask_user()
# complex_calculation()
# print('Single thread total time: ', time.time() - start, '\n\n')







 # With multiple Process
if __name__=="__main__":
	process1= Process(target=complex_calculation)
	#process2= Process(target=ask_user)
	process2= Process(target=complex_calculation)

	start = time.time()
	process1.start()
	process2.start()
	process1.join()
	process2.join()
	print(f"Two thread total time: {time.time()-start}")
