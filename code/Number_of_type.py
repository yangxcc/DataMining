import pandas as pd

#  电吹风
file_hair_dryer = pd.read_csv("hair_dryer.tsv", sep='\t',usecols=[3,4,7,11])
df=pd.DataFrame(file_hair_dryer)

print(file_hair_dryer.loc[:,'product_id'].value_counts())
print(len(file_hair_dryer.loc[:,'product_id'].value_counts()))

print('电吹风')
print(file_hair_dryer.loc[:,'product_parent'].value_counts()[0:10])
print(len(file_hair_dryer.loc[:,'product_parent'].value_counts()))

#print(df.loc[df['product_parent'] == '732252283'].loc[:,'star_rating'].value_counts())
print(df.loc[df['product_id'] == 'B000H05X0K'].loc[:,'star_rating'].value_counts())
# print(df.loc[df['product_id'] == 'B003V264WW'].loc[:,'verified_purchase'].value_counts())
print('**************************************')


# 微波炉
file_microwave = pd.read_csv("microwave.tsv", sep='\t',usecols=[3,4,7,11])
df=pd.DataFrame(file_microwave)

print(file_microwave.loc[:,'product_id'].value_counts())
print(len(file_microwave.loc[:,'product_id'].value_counts()))
print('微波炉')
print(file_microwave.loc[:,'product_parent'].value_counts()[0:10])
print('**************************************')

# 奶瓶
file_pacifier = pd.read_csv("pacifier.tsv", sep='\t',usecols=[3,4,7,11])
df=pd.DataFrame(file_pacifier)

print(file_pacifier.loc[:,'product_id'].value_counts())
print(len(file_pacifier.loc[:,'product_id'].value_counts()))
print('奶瓶')
print(file_pacifier.loc[:,'product_parent'].value_counts()[0:10])

