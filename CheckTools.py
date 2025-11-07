import CommLib

def CheckEven(ChkVal):
	if (ChkVal % 2) == 0:
		return True
	else:
		return False

def CheckMoveX(PosY, SaveMoveFrag):
	if SaveMoveFrag == True:
		ChkCnt = CommLib.MAX_WORLDSIZE
	else:
		ChkCnt = 0
	if PosY == ChkCnt:
		move(East)
		if SaveMoveFrag:
			SaveMoveFrag = False
		else:
			SaveMoveFrag = True
		return True, SaveMoveFrag
	else:
		return False, SaveMoveFrag

def CheckPlant(PosX, PosY):
	if CheckEven(PosX) == True and CheckEven(PosY) == True:
		plant(Entities.Tree)
	elif CheckEven(PosX) == True:
		CheckCarrots()

def Check5x5(PosX, PosY):
	if CommLib.MIN_POS <= PosX and PosX <= CommLib.MAX_SQUARESIZE:
		if CommLib.MIN_POS <= PosY and PosY <= CommLib.MAX_SQUARESIZE:
			return True
	return False

def CheckPlantCactus(PosX, PosY):
	if CommLib.MIN_POS <= PosX and PosX <= CommLib.MAX_SQUARESIZE:
		if CommLib.MIN_POS <= PosY and PosY <= CommLib.MAX_SQUARESIZE:
			CheckCanTill()
			plant(Entities.Cactus)
			return True
	return False

def CheckHarvestCuctus():
	Cur_Size = measure()
	E_Size = measure(East)
	N_Size = measure(North)
	

def CheckCanTill():
	if get_ground_type() == Grounds.Grassland:
		till()

def CheckCarrots():
	CheckCanTill()
	plant(Entities.Carrot)

def CheckPumpkin():
	CheckCanTill()
	plant(Entities.Pumpkin)
		
