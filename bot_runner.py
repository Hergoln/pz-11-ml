from time import sleep
from src import spawn_bots, RandomAgent
import numpy as np
import signal

global_done = False
def terminate_bots(*args, **kwargs):
	global global_done
	global_done = True

if __name__ == "__main__":
	signal.signal(signal.SIGINT, terminate_bots)
	gen= np.random.default_rng(2137)

	manager = spawn_bots("ws://botbattles.iis.p.lodz.pl:2137", 
                      	 "session_ca59144551889265", 
                         RandomAgent, 
                         1, 
                         generator=gen)

	try:
		while not global_done:
			sleep(0.1)
	except:...
	finally: manager.terminate(30)	
