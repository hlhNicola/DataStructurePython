import statistics
import matplotlib.pyplot as plt


# ---  Random Data Sets -----

randomBubble2000 = [0.5066161155700684, 0.5365660190582275, 0.4786856174468994, 0.47871828079223633, 0.4896860122680664]
randomBubble4000 = [2.6260151863098145, 1.9099087715148926, 1.858069896697998, 1.8869550228118896, 1.8390495777130127]
randomBubble6000 = [4.043210506439209, 4.641539573669434, 4.133908271789551, 4.3494062423706055, 4.700434923171997]
randomBubble8000 = [7.724292993545532, 7.970690011978149, 7.808124303817749, 7.38726019859314, 7.582760334014893]
randomBubble10000 = [13.004266738891602, 14.139231443405151, 12.957391738891602, 13.264524698257446, 13.879853963851929]

randomBubble2000Ave = statistics.mean(randomBubble2000)
randomBubble4000Ave = statistics.mean(randomBubble4000)
randomBubble6000Ave = statistics.mean(randomBubble6000)
randomBubble8000Ave = statistics.mean(randomBubble8000)
randomBubble10000Ave = statistics.mean(randomBubble10000)

randomSelected2000 = [0.11665606498718262, 0.09973311424255371, 0.0867772102355957, 0.10372066497802734, 0.10567998886108398]
randomSelected4000 = [0.5196123123168945, 0.4338400363922119, 0.3739907741546631, 0.7290151119232178, 0.43387722969055176]
randomSelected6000 = [1.1309726238250732, 0.9175467491149902, 1.1349291801452637, 1.235741138458252, 0.9335036277770996]
randomSelected8000 = [2.5960590839385986, 1.7313709259033203, 1.6874866485595703, 1.7662687301635742, 2.309788942337036]
randomSelected10000 = [2.5921106338500977, 3.2652697563171387, 2.5382137298583984, 2.5860860347747803, 3.1695613861083984]

randomSelected2000Ave = statistics.mean(randomSelected2000)
randomSelected4000Ave = statistics.mean(randomSelected4000)
randomSelected6000Ave = statistics.mean(randomSelected6000)
randomSelected8000Ave = statistics.mean(randomSelected8000)
randomSelected10000Ave = statistics.mean(randomSelected10000)

randomInsert2000 = [0.13962411880493164, 0.14261841773986816, 0.13464045524597168, 0.13862991333007812, 0.14261865615844727]
randomInsert4000 = [0.5694782733917236, 0.5784177780151367, 0.8267900943756104, 0.5734667778015137, 0.564490795135498]
randomInsert6000 = [1.259596824645996, 1.76228928565979, 1.264622449874878, 1.253648281097412, 1.3165173530578613]
randomInsert8000 = [2.2928695678710938, 2.4943301677703857, 3.000972032546997, 2.5172688961029053, 2.5920684337615967]
randomInsert10000 = [3.7978460788726807, 4.06213903427124, 3.7320332527160645, 3.4956541061401367, 4.264602422714233]

randomInsert2000Ave = statistics.mean(randomInsert2000)
randomInsert4000Ave = statistics.mean(randomInsert4000)
randomInsert6000Ave = statistics.mean(randomInsert6000)
randomInsert8000Ave = statistics.mean(randomInsert8000)
randomInsert10000Ave = statistics.mean(randomInsert10000)

# ---  Sorted Data Sets -----


sortedBubble2000 = [0.0, 0.0, 0.0009970664978027344, 0.0009951591491699219, 0.0]
sortedBubble4000 = [0.000997781753540039, 0.0009975433349609375, 0.0, 0.0, 0.0]
sortedBubble6000 = [0.0, 0.0, 0.0010068416595458984, 0.0, 0.0009961128234863281]
sortedBubble8000 = [0.001027822494506836, 0.0009975433349609375, 0.0, 0.0009987354278564453, 0.0]
sortedBubble10000 = [0.0009975433349609375, 0.0009970664978027344, 0.0009872913360595703, 0.0009975433349609375, 0.0009963512420654297]

sortedBubble2000Ave = statistics.mean(sortedBubble2000)
sortedBubble4000Ave = statistics.mean(sortedBubble4000)
sortedBubble6000Ave = statistics.mean(sortedBubble6000)
sortedBubble8000Ave = statistics.mean(sortedBubble8000)
sortedBubble10000Ave = statistics.mean(sortedBubble10000)

sortedSelected2000 = [0.08776521682739258, 0.10272526741027832, 0.08675718307495117, 0.08776593208312988, 0.0937490463256836]
sortedSelected4000 = [0.3560760021209717, 0.41289615631103516, 0.3430824279785156, 0.3530459403991699, 0.3909146785736084]
sortedSelected6000 = [0.8726732730865479, 0.9255251884460449, 0.8287482261657715, 1.197772741317749, 0.9345376491546631]
sortedSelected8000 = [1.5388875007629395, 1.8221662044525146, 1.5119576454162598, 2.298886775970459, 1.727379322052002]
sortedSelected10000 = [3.0448243618011475, 2.6299307346343994, 2.303877115249634, 2.6748509407043457, 2.8952627182006836]

sortedSelected2000Ave = statistics.mean(sortedSelected2000)
sortedSelected4000Ave = statistics.mean(sortedSelected4000)
sortedSelected6000Ave = statistics.mean(sortedSelected6000)
sortedSelected8000Ave = statistics.mean(sortedSelected8000)
sortedSelected10000Ave = statistics.mean(sortedSelected10000)

sortedInsert2000 = [0.0009975433349609375, 0.000997304916381836, 0.0, 0.0010027885437011719, 0.0009949207305908203]
sortedInsert4000 = [0.000997304916381836, 0.0, 0.0009982585906982422, 0.0009927749633789062, 0.0010001659393310547]
sortedInsert6000 = [0.0019638538360595703, 0.001994609832763672, 0.001001119613647461, 0.0009970664978027344, 0.0009963512420654297]
sortedInsert8000 = [0.002023935317993164, 0.0019948482513427734, 0.001992940902709961, 0.001994609832763672, 0.001994609832763672]
sortedInsert10000 = [0.0019969940185546875, 0.001994609832763672, 0.001994609832763672, 0.001996755599975586, 0.0029931068420410156]

sortedInsert2000Ave = statistics.mean(sortedInsert2000)
sortedInsert4000Ave = statistics.mean(sortedInsert4000)
sortedInsert6000Ave = statistics.mean(sortedInsert6000)
sortedInsert8000Ave = statistics.mean(sortedInsert8000)
sortedInsert10000Ave = statistics.mean(sortedInsert10000)

# ---  Reversed Data Sets -----


reversedBubble2000 = [0.7190790176391602, 0.7130930423736572, 0.7320425510406494, 0.7210664749145508, 0.7778782844543457]
reversedBubble4000 = [2.932159662246704, 2.8812968730926514, 3.563473701477051, 3.263273239135742, 3.098717212677002 ]
reversedBubble6000 = [7.089007377624512, 7.142902135848999, 6.6442344188690186, 6.471657991409302, 7.252643823623657]
reversedBubble8000 = [12.34399676322937, 12.040844440460205, 13.002277374267578, 12.507596731185913, 13.667458057403564]
reversedBubble10000 = [19.840991973876953, 21.26015877723694, 19.36322569847107, 20.387489795684814, 21.595260858535767]

reversedBubble2000Ave = statistics.mean(reversedBubble2000)
reversedBubble4000Ave = statistics.mean(reversedBubble4000)
reversedBubble6000Ave = statistics.mean(reversedBubble6000)
reversedBubble8000Ave = statistics.mean(reversedBubble8000)
reversedBubble10000Ave = statistics.mean(reversedBubble10000)

reversedSelected2000 = [0.1545875072479248, 0.16655421257019043, 0.1515824794769287, 0.19351696968078613, 0.15059566497802734]
reversedSelected4000 = [0.6103658676147461, 0.6522932052612305, 0.6372952461242676, 0.6253294944763184, 0.634300708770752]
reversedSelected6000 = [1.3503906726837158, 1.686490535736084, 1.892904281616211, 1.430177927017212, 1.5378530025482178]
reversedSelected8000 = [3.201404571533203, 2.70776104927063, 3.0388739109039307, 2.4823596477508545, 2.7177343368530273]
reversedSelected10000 = [4.1529319286346436, 4.23065185546875, 5.376624584197998, 3.9544272422790527, 3.9953176975250244]

reversedSelected2000Ave = statistics.mean(reversedSelected2000)
reversedSelected4000Ave = statistics.mean(reversedSelected4000)
reversedSelected6000Ave = statistics.mean(reversedSelected6000)
reversedSelected8000Ave = statistics.mean(reversedSelected8000)
reversedSelected10000Ave = statistics.mean(reversedSelected10000)

reversedInsert2000 = [0.2982001304626465, 0.34204888343811035, 0.29920244216918945, 0.3091731071472168, 0.3041868209838867]
reversedInsert4000 = [1.2326669692993164, 1.4311718940734863, 1.2705988883972168, 1.2277281284332275, 1.2187416553497314]
reversedInsert6000 = [1.3503906726837158, 2.9501125812530518, 2.7875118255615234, 2.8134689331054688, 2.7765400409698486]
reversedInsert8000 = [4.94573974609375, 5.9102349281311035, 4.968753099441528, 5.056442975997925, 5.529252529144287]
reversedInsert10000 = [8.374646663665771, 9.430748701095581, 8.08539366722107, 8.664834976196289, 8.335719108581543]

reversedInsert2000Ave = statistics.mean(reversedInsert2000)
reversedInsert4000Ave = statistics.mean(reversedInsert4000)
reversedInsert6000Ave = statistics.mean(reversedInsert6000)
reversedInsert8000Ave = statistics.mean(reversedInsert8000)
reversedInsert10000Ave = statistics.mean(reversedInsert10000)


#  -----  Graph base on different algorithm but same input  ----

listRandomBubble = [randomBubble2000Ave, randomBubble4000Ave, randomBubble6000Ave, randomBubble8000Ave, randomBubble10000Ave]
listRandomInsert = [randomInsert2000Ave, randomInsert4000Ave, randomInsert6000Ave, randomInsert8000Ave, randomInsert10000Ave]
listRandomSelected = [randomSelected2000Ave, randomSelected4000Ave, randomSelected6000Ave, randomSelected8000Ave, randomSelected10000Ave]

listSortedBubble = [sortedBubble2000Ave, sortedBubble4000Ave, sortedBubble6000Ave, sortedBubble8000Ave, sortedBubble10000Ave]
listSortedInsert = [sortedInsert2000Ave, sortedInsert4000Ave, sortedInsert6000Ave, sortedInsert8000Ave, sortedInsert10000Ave]
listSortedSelected = [sortedSelected2000Ave, sortedSelected4000Ave, sortedSelected6000Ave, sortedSelected8000Ave, sortedSelected10000Ave]

listReversedBubble = [reversedBubble2000Ave, reversedBubble4000Ave, reversedBubble6000Ave, reversedBubble8000Ave, reversedBubble10000Ave]
listReversedInsert = [reversedInsert2000Ave, reversedInsert4000Ave, reversedInsert6000Ave, reversedInsert8000Ave, reversedInsert10000Ave]
listReversedSelected = [reversedSelected2000Ave, reversedSelected4000Ave, reversedSelected6000Ave, reversedSelected8000Ave, reversedSelected10000Ave]

xAxis = [2000, 4000, 6000, 8000, 10000]

# -- random --
plt.plot(xAxis, listRandomBubble, label="Bubble Sort")
plt.plot(xAxis, listRandomInsert, label="Insert Sort")
plt.plot(xAxis, listRandomSelected, label="Selected Sort")

plt.xlabel('number of input')

plt.ylabel('run time')
plt.legend()
plt.title('Bubble, Insert, Selected Sort with Random input')
plt.show()

# -- sorted --
plt.plot(xAxis, listSortedBubble, label="Bubble Sort")
plt.plot(xAxis, listSortedInsert, label="Insert Sort")
plt.plot(xAxis, listSortedSelected, label="Selected Sort")

plt.xlabel('number of input')

plt.ylabel('run time')
plt.legend()
plt.title('Bubble, Insert, Selected Sort with Sorted input')
plt.show()

# -- reversed --
plt.plot(xAxis, listReversedBubble, label="Bubble Sort")
plt.plot(xAxis, listReversedInsert, label="Insert Sort")
plt.plot(xAxis, listReversedSelected, label="Selected Sort")

plt.xlabel('number of input')

plt.ylabel('run time')
plt.legend()
plt.title('Bubble, Insert, Selected Sort with Reversed input')
plt.show()
#  -----  Graph base on same algorithm but different input  ----------------------------------


# -- Bubble --
plt.plot(xAxis, listRandomBubble, label="Random Input")
plt.plot(xAxis, listSortedBubble, label="Sorted Input")
plt.plot(xAxis, listReversedBubble, label="Reversed Input")

plt.xlabel('number of input')

plt.ylabel('run time')
plt.legend()
plt.title('Bubble Sort with different input')
plt.show()


# -- Insertion --
plt.plot(xAxis, listRandomInsert, label="Random Input")
plt.plot(xAxis, listSortedInsert, label="Sorted Input")
plt.plot(xAxis, listReversedInsert, label="Reversed Input")

plt.xlabel('number of input')

plt.ylabel('run time')
plt.legend()
plt.title('Insert Sort with different input')
plt.show()


# -- Selection --
plt.plot(xAxis, listRandomSelected, label="Random Input")
plt.plot(xAxis, listSortedSelected, label="Sorted Input")
plt.plot(xAxis, listReversedSelected, label="Reversed Input")

plt.xlabel('number of input')

plt.ylabel('run time')
plt.legend()
plt.title('Selected Sort with different input')
plt.show()
