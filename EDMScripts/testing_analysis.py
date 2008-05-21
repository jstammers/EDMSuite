from Analysis import *
from Analysis.EDM import *
from Data.EDM import *
from System.Collections.Generic import *
from System.IO import *
from System.Runtime.Serialization.Formatters.Binary import *
import time

bs = BlockSerializer()
block = bs.DeserializeBlockFromZippedXML("C:\\Users\\jony\\Files\\Data\\SEDM\\v3\\2008\\January2008\\16Jan0808_0.zip", "block.xml")
#tf = TOFFitter()
#rs = tf.FitTOF(block.GetAverageTOF(0))

bd = BlockDemodulator()
dc = DemodulationConfig()
#dg0 = DetectorExtractSpec.MakeGateFWHM(block, 0, 0, 1)
dg0 = DetectorExtractSpec()
dg0.Name = "top"
dg0.Index = 0
dg0.GateLow = 2100
dg0.GateHigh = 2300
#dg1 = DetectorExtractSpec.MakeGateFWHM(block, 1, 0, 1)
dg1 = DetectorExtractSpec()
dg1.Name = "norm"
dg1.Index = 1
dg1.GateLow = 548
dg1.GateHigh = 601
dg1.BackgroundSubtract = False
dg2 = DetectorExtractSpec.MakeWideGate(2)
dg2.Name = "mag1"
dg2.Integrate = False
dc.DetectorExtractSpecs.Add(dg0)
dc.DetectorExtractSpecs.Add(dg1)
dc.DetectorExtractSpecs.Add(dg2)

db = bd.DemodulateBlock(block, dc)

fs = FileStream("c:\\Users\\jony\\Desktop\\db.bin",FileMode.Create)
bf = BinaryFormatter()
bf.Serialize(fs, db)
fs.Close()

#t1 = time.clock()
#for i in range(0,100000):
#	db.ChannelValues[0].GetChannelIndex( ("E",) )
#dt = (time.clock() - t1)
#print "Time for 10^5 channel index lookups"
#print dt

t1 = time.clock()
for i in range(0,10):
	bd.DemodulateBlock(block, dc)
dt = (time.clock() - t1)
print "Time for 10^1 demodulations"
print dt

def run_script():
	print("done!")

l = list()
numBlocks = 10000

def serialize_a_lot():
	for i in range(0,numBlocks):
		fs = FileStream("C:\\Users\\jony\\Desktop\\test\\" + str(i) + ".bin", FileMode.Create)
		bf.Serialize(fs, db)
		fs.Close()

def deserialize_a_lot():
	for i in range(0,numBlocks):
		fs = FileStream("C:\\Users\\jony\\Desktop\\test\\" + str(i) + ".bin", FileMode.Open)
		l.Add(bf.Deserialize(fs))
		fs.Close()

p = list()
def grab_a_property(l):
	p.Clear()
	for i in range(0, l.Count):
		if (l[i].ChannelValues[0].GetValue(0) < 600) and (l[i].ChannelValues[0].GetValue(0) > 500): p.Add(i)
