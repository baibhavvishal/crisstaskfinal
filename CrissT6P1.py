import pandas as pd
ax=2.5
ay=0
az=-9.8
l1=(ax,ay,az)
gx=0
gy=0
gz=1
lax=[]
lay=[]
laz=[]
lgz=[]
lgx=[]
lgy=[]
while gz<=9.99:
	gz+=0.1
	gy+=0.1
	ay+=0.1
	lax.append(ax)
	lay.append(ay)
	laz.append(az)
	lgx.append(gx)
	lgy.append(gy)
	lgz.append(gz)
df = pd.DataFrame({'AX':lax, 'AY':lay,'AZ':laz,'GX':lgx,'GY':lgy,'GZ':lgz})
writer = pd.ExcelWriter('accgyro.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)

writer.close()
