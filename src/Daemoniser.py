'''
Standalone class to handle daemonisation.
'''
import os, signal, sys

class Daemoniser:
	@staticmethod
	def daemonise() -> None:
		Daemoniser.__resetSignals()
		Daemoniser.__resetSignalMask()

		Daemoniser.__sanitiseEnv()
		Daemoniser.__closeFd()

		Daemoniser.__forkAndExit()
		os.setsid()

	@staticmethod
	def __resetSignals() -> None:
		# Essentially 
		for sig in range(1, signal.NSIG): # Iterate via avalible signums
			try:
				signal.signal(sig, signal.SIG_DFL) #TODO: Explain this
			except (OSError, RuntimeError): # Py version of catch
				pass
				
	@staticmethod
	def __resetSignalMask() -> None: #TODO: Explain this
		signal.pthread_sigmask(signal.SIG_SETMASK,[int])

	@staticmethod
	def __sanitiseEnv() -> None:
		return
	@staticmethod
	def __closeFd() -> None:
		return
	@staticmethod
	def __forkAndExit() -> None:
		# This will immediately exit parent and keep child running
		pid: int = os.fork
		if pid > 0:
			os._exit(0)
	@staticmethod
	def __redirectStdio() -> None:
		return
	@staticmethod
	def __finalizeDaemon() -> None:
		return
