#day1_python-task 
import numpy as np 
df=np.random.randint(0,100,50)
print(df)
print( f"mean: {df.mean()}")
print(f"medain:{np.median(df)}")
print(f"standard deviation:{df.std()}")
print(f"percentile:{np.percentile(df,25)}")
x1=[ x for x in df if x<40]
print(f"failed:{x1}")
x2=[ x for x in df if x>=85]
print(f"good score:{x2}")
array=df
print("noramlize marks")
normailze_score=(array-array.min())/(array.max()-array.min())
print(normailze_score)
print("reshaped array")
reshape=array.reshape(5,10)
print(reshape)
print("row-wise-average")
rowwiseaverage=np.mean(reshape,axis=1)
print(rowwiseaverage)