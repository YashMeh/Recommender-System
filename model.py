#Loading the dataset
import pandas as pd
dataset=pd.read_csv('Market_Basket_Optimisation.csv')
dataset=dataset.values
transactions=[]
for i in range(0,7500):
	sub_l=[]
	for j in range(0,20):
		if type(dataset[i,j])==str:
			sub_l.append(dataset[i,j])
	transactions.append(sub_l)
	sub_l=[]	
#Preprocessing the transactions array
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)
#Applying the Apriori	
from mlxtend.frequent_patterns import apriori
frequent_itemsets=apriori(df, min_support=0.003,use_colnames=True)
from mlxtend.frequent_patterns import association_rules
rules=association_rules(frequent_itemsets, metric="lift", min_threshold=3)
#Query to find the transactions where antecedants and consequent is one,lift is greater than 3 and confidence is greater than 0.2
index_list=[]
for i in range(len(rules['antecedants'])):
	if len(rules['antecedants'][i])==1 and len(rules['consequents'][i])==1:
		if rules['confidence'][i]>0.2:
			index_list.append(i)
for i in index_list:
	print('People who bought:'," ",[j for j in rules['antecedants'][i]]," ","also bought:"," ",[k for k in rules['consequents'][i]] )			