import time
def time_this(num_runs=10):
	def decorator(func):
		def time_counter():
			avg_time = 0
			for i in range(num_runs):
				t0 = time.time()
				func()
				t1 = time.time()
				avg_time += (t1-t0)
			avg_time /= num_runs
			print('Выполнение заняло {} секунд'.format(avg_time))
		return time_counter
	return decorator
@time_this()
def f():
    for j in range(1000000):
        pass
f()
