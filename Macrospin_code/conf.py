import numpy as np 


class conFile() :

	def __init__(self):
		
		self.g0 = 2.21e5	   							# mu0 * gamma
		self.gamma = 1.76e11							# gamma
		self.mu0 = 4*np.pi*1e-7							# mu zero 
		self.muB = 9.274e-24							# Bohr magneton
		self.kB = 1.38064852e-23						# Boltzman constant
		self.e = 1.602176364e-19 						# Elementary charge
		self.h  = 5.0e-15	   							# Euler step  
		self.t  = 0.500e-9 								# Total time   
		self.Lx = 100.0e-9 								# Dimension along x
		self.Ly = 100.0e-9 								# Dimension along y
		self.Lz = 1.0e-9       							# Dimension along z
		self.Area = self.Lx * self.Ly 					# Device Area
		self.Vol = self.Area * self.Lz 					# Device volume
		self.Temp=300.0 								# Temperature in K
		self.Temp_Ampl=0.0 								# Amplitude of temperature distribution
		self.a  = 0.05		   							# Damping Contant
		self.Ms = 566e3 								# Saturation Magnetization
		self.A0 = -0.248e-12							# Homogeneous interlattice exchange
		self.Ku = 28.3e3	   							# Uniaxial Anisotropy
		self.DMI_vec =  np.array([0.0,0.0,1.0])*1e-4	# DMI vector
		self.l = 0.5e-9									# lattice constant
		self.H = 0.0e-3									# Field
		self.Fr =1.0e9								    # Frequency 
		self.T = 1/self.Fr								# Period
		self.phase = 0.0*np.pi							# Phase 
		self.flagShape = False 							# flag for shape. If True, shape is cylindrical
		self.flag0 = False 								# Temperature flag
		self.flag1 = False								# Flag to activate J(t)
		self.flag2 = False								# flag1 is for J(t) # Flag to activate Ku(t)
		self.flag3 = False 								# Flag to activate H(t)	
		self.flag4 = False                              # Flag to activate Chirp signal
		self.flag5 = False                              # Flag to activate SOT
		self.flagSinc = False                              # Flag to activate sinc signal
		self.flagTempVarying = False                              # Flag to activate temperature varying parameters
		self.Hex_DC = np.array([0.0,0.0,0.0]) 			# Ex Field Components (DC)
		self.Hex_AC = np.array([0.0,0.0,0.0]) 			# Ex Field Components (AC)	
		self.m1 = np.array([ -0.3785504696409115, 0.0026628502418170, 0.9255768207789320])			# Initial Condition m_1
		self.m2 = np.array([0.3785504696409115, 0.0026628502418170, -0.9255768207789320])				# Initial Condition m_2
		self.p  = np.array([0.0,0.0,0.0])				# Polarizer
		self.Demag = 0*np.array([0.0259,0.0259,0.9482]) # Demag Tensor 
		self.u_ani =  np.array([0.0,0.0,1.0])				# Anisotropy easy axis
		self.u_ani_AC =  np.array([0.0,0.0,1.0])				# Anisotropy AC easy axis
		self.A0_Amp = 0.0e-12							# J  Amp
		self.Ku_Amp = 0.0e6								# Ku(t) Amp
		self.Ku_Fr = 0.0e9								# Ku(t) Frequency
		self.Ku_phase = 0.0								# Ku(t) phase
		self.H_Amp = 0.0e-3								# Field Amp

		self.t_chirp=0.1e-9 							# Duration of Chirp pulse
		self.Chirp_Amp=0.0e7 							# Amplitude of Chirp signal
		self.Chirp_min_Fr=10.0e9 						# Minimum Chrirp frequeuncy
		self.Chirp_max_Fr=1000.0e9 						# Maximum Chrirp frequeuncy
		self.Chirp_phase=0.0 							# Maximum Chrirp frequeuncy

		self.SHE_angle=0.1                              # SHE angle
		self.SOT_DC_Amp=0.0 							# SOT DC current amplitude in A/cm2
		self.SOT_AC_Amp=0.0e7 							# SOT AC current amplitude in A/cm2
		self.SOT_AC_Fr=10.0e9 								# SOT AC current frequency in Hz
		self.SOT_AC_phase=0.0  							# SOT AC current phase in radiants
		self.SOT_pol=np.array([0.0,1.0,0.0])			# SOT polarisation
		self.SOT_FL_q=0.0								# SOT FL strength
		
		
		
		
	


