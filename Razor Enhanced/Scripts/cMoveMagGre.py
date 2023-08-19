from Scripts.utilities.items import MoveItem
from Scripts import config

SEARCH_STRING = "Greater Magic Item"

sourceBox = Target.PromptTarget( 'Select container to move items out of' )
sourceBoxItem = Items.FindBySerial( sourceBox )
if sourceBoxItem == None:
    sourceBox = Mobiles.FindBySerial( sourceBox ).Backpack
else:
    sourceBox = sourceBoxItem

targetBox = Target.PromptTarget( 'Select container to move items into' )
targetBoxItem = Items.FindBySerial( targetBox )
if targetBoxItem == None:
    targetBox = Mobiles.FindBySerial( targetBox ).Backpack
else:
    targetBox = targetBoxItem

Items.UseItem( sourceBox )
Misc.Pause( config.dragDelayMilliseconds )

Items.UseItem( targetBox )
Misc.Pause( config.dragDelayMilliseconds )

for item in sourceBox.Contains:
    properties = item.Properties
    if(len(properties) > 0):
        prop = properties[len(properties) - 1].Args
        if(SEARCH_STRING in prop):
#            Misc.SendMessage(item)
#            Misc.SendMessage(properties[len(properties) - 1].Args)
            MoveItem( Items, Misc, item, targetBox )
