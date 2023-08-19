#Author: Hearto Lazor
#Script for organize containers in subcontainers at the root container level automatically
#The script search for all boxes in a container, read the box name and then move the items that have a text on the name that match the box name
#For example if there is a chest named "Cache" and there is a map at the same level on the container, the script will find the "Cache" word inside 
#the map name "A tattered Treasure Map Leading To An Artisan's Cache" and move the map to the chest
#The script ignores the case of the names in the comparisons.
#The script requires a way to rename the containers
from Scripts import config

sourceBox = Target.PromptTarget( 'Select container to organize' )
sourceBoxItem = Items.FindBySerial( sourceBox )
if sourceBoxItem == None:
    sourceBox = Mobiles.FindBySerial( sourceBox ).Backpack
else:
    sourceBox = sourceBoxItem

boxesList = []
for item in sourceBox.Contains:
    if(item.IsContainer):
        boxesList.append(item)

for item in sourceBox.Contains:
    if(not item.IsContainer):
        for box in boxesList:
            if(box.Name.lower() in item.Name.lower()):
                Items.Move( item, box, 0 )
                # Wait for the move to complete
                Misc.Pause( config.dragDelayMilliseconds )
                break
