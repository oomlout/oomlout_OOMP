import OOMP

#Import detail lists
import OOMPdetailsColor

parts = list()

test = OOMP.oompItem(1)

#print(test)

print()
print()
print()


#### sample load list
import OOMPdetailsColor
import OOMPdetailsType

#### sample item
newPart = OOMP.oompItem(2)
newPart.addTag("oompType", "HEAD")
newPart.addTag("oompSize", "I01")
newPart.addTag("oompColor", "R")
newPart.addTag("oompDesc", "PI02")
newPart.addTag("oompIndex", "01")

parts.append(newPart)             

#print("OOMPTYPE    " + str(newPart.getTag("oompType")))
#print("OOMPName    " + str(newPart.getTag("oompName")))
print(newPart.getTag("oompType"))


print()
print()
      
print(newPart)
