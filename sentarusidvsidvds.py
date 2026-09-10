import pandas as pd
import matplotlib.pyplot as plt


vds_qs = pd.read_csv("idvds_qs_vg=3.csv")
vds_tox = pd.read_csv("idvds_tox_vg=3.csv")

plt.figure(figsize=(8,6))

plt.plot(vds_qs.iloc[:,0], vds_qs.iloc[:,1],
         label="QS, VGS = 3 V")

plt.plot(vds_tox.iloc[:,0], vds_tox.iloc[:,1],
         label="TOX, VGS = 3 V")

plt.xlabel("VDS (V)")
plt.ylabel("ID (A)")
plt.title("ID vs VDS")
plt.legend()
plt.grid(True)
plt.show()


vgs_qs = pd.read_csv("idvgs_qs_vd=1.csv")
vgs_tox = pd.read_csv("idvgs_tox_vd=1.csv")

plt.figure(figsize=(8,6))

plt.plot(vgs_qs.iloc[:,0], vgs_qs.iloc[:,1],
         label="QS, VDS = 1 V")

plt.plot(vgs_tox.iloc[:,0], vgs_tox.iloc[:,1],
         label="TOX, VDS = 1 V")

plt.xlabel("VGS (V)")
plt.ylabel("ID (A)")
plt.title("ID vs VGS")
plt.legend()
plt.grid(True)
plt.show()