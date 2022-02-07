import numpy as np

import Aerodynamics.Aero_IntegratedWorkflow as aiw
import Aerodynamics.Aero_InputFileWimpress as aif # Read Input File
import Auxiliary.Aux_PlotWingAndLoads as xpw
import Auxiliary.Aux_AeroWriteToFile as xwf

def AddNumbers(x1, x2):
	return (x1 + x2)

def MultiplyNumbers(x1, x2):
	return (x1 * x2)

def TwoOutputsModel(x1, x2):
	y1 = x1 + x2
	y2 = x1 * x2
	return (y1, y2)
	
