import BaseCommand
import CommLib

SaveMoveFrag = True
CntItems = 0
while True:
	for i in range(get_world_size()):
		PosX, PosY = get_pos_x(), get_pos_y()
		SaveMoveFrag = BaseCommand.BaseHarvest(PosX, PosY, SaveMoveFrag, CntItems)
		if CntItems == 1:
			if PosX == CommLib.MAX_WORLDSIZE and PosY == 0:
				CntItems = 0
		else:
			if PosX == CommLib.MAX_WORLDSIZE and PosY == 0:
				CntItems += CommLib.CNT_USEITEMS