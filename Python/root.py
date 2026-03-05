import uproot
import numpy
print("STARTED ROOT INSPECTION")

file = uproot.open("E:/FYP/Python/2_shower_event_preselection_and_selection_v2.root")
file.classnames()
file.keys()
print(file.classnames())


