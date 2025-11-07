import CheckTools
import CommLib

START_CACTUS_POS = CommLib.MAX_WORLDSIZE - CommLib.MIN_POS

def MoveDirection(MoveFrag):
	if MoveFrag == True:
		move(North)
	else:
		move(South)
		
def BaseHarvest(PosX, PosY, SaveMoveFrag, CntItems):
	harvest()
	if CheckTools.Check5x5(PosX, PosY):
		CheckTools.CheckPumpkin()
		if CntItems == CommLib.CNT_USEITEMS:
			use_item(Items.Fertilizer)
	#elif START_CACTUS_POS < get_pos_x() and START_CACTUS_POS < get_pos_y():
		
	else:
		CheckTools.CheckPlant(PosX, PosY)
	if CntItems == CommLib.CNT_USEITEMS:
		use_item(Items.Water)
	TempFrag, SaveMoveFrag = CheckTools.CheckMoveX(PosY, SaveMoveFrag)
	if TempFrag == False:
		MoveDirection(SaveMoveFrag)
	return SaveMoveFrag
