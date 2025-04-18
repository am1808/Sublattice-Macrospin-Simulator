import numpy as np 
from conf import conFile
from scipy.signal import chirp

class Current:
	def __init__(self):  
		self.param = conFile()

	def j(self, J, t0):
		J = np.float64(J)
		t0 = np.float64(t0)

		if not self.param.flag1:
			return J
		else:
			TT = np.float64(self.param.T * (self.param.g0 * self.param.Ms))
			omega = np.float64(2 * np.pi / TT)
			Jamp = np.float64((4 * self.param.A0_Amp) / (self.param.mu0 * self.param.Ms**2 * self.param.l**2))
			j = np.float64(J + Jamp * np.sin(omega * t0 + self.param.phase))
			return j

	def ku(self, k, t0):
		k = np.float64(k)
		t0 = np.float64(t0)

		if not self.param.flag2:
			return k
		else:
			TT = np.float64(self.param.T * (self.param.g0 * self.param.Ms))
			omega = np.float64(2 * np.pi / TT)
			kamp = np.float64((2 * self.param.Ku_Amp) / (self.param.g0 * self.param.Ms**2))
			kk = np.float64(k + kamp * np.sin(omega * t0 + self.param.phase))
			return kk

	def H(self, H, t0):
		H = np.float64(H)
		t0 = np.float64(t0)

		if not self.param.flag3:
			return np.float64(H * self.param.Hex_DC)
		else:
			TT = np.float64(self.param.T * (self.param.g0 * self.param.Ms))
			omega = np.float64(2 * np.pi / TT)
			H_Amp = np.float64(self.param.H_Amp / (self.param.mu0 * self.param.Ms))
			HH = np.float64(H * self.param.Hex_DC + self.param.Hex_AC * (H_Amp * np.sin(omega * t0 + self.param.phase)))
			return HH

	def Je_Chirp(self, t0):
		t0 = np.float64(t0 / (self.param.g0 * self.param.Ms))
		Je_Chirp = np.float64(0.0)

		if self.param.flag4 and self.param.t_chirp > t0:
			sigma = 1.0e4 * 2.0 * self.param.muB / (self.param.e * self.param.g0 * self.param.Ms**2 * self.param.Lz)
			Je_Chirp = np.float64(sigma * self.param.Chirp_Amp * chirp(t=t0, f0=self.param.Chirp_min_Fr, t1=self.param.t_chirp, f1=self.param.Chirp_max_Fr, method='linear', phi=self.param.Chirp_phase))

		return Je_Chirp

	def Je_SOT(self, t0):
		
		Je_SOT = np.float64(0.0)

		if self.param.flag5:
			omega = np.float64(2 * np.pi * self.param.SOT_AC_Fr / (self.param.g0 * self.param.Ms))

			sigma = 1.0e4 * 2.0 * self.param.muB / (self.param.e * self.param.g0 * self.param.Ms**2 * self.param.Lz)
			Prefactor = np.float64(self.param.SHE_angle * sigma)
			Je_SOT = np.float64(Prefactor * (self.param.SOT_DC_Amp + self.param.SOT_AC_Amp * np.sin(omega * t0 + self.param.SOT_AC_phase)))

		return Je_SOT