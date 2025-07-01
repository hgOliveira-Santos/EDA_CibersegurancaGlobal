import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Global_Cybersecurity_Threats_2015-2024.csv')
df.head(10)

df.columns
df.shape
df.dtypes

# Verificando a existência de valores nulos
df.isnull().sum()

# Quais os tipos de ataque mais comuns?
attack_types = df['Attack Type'].value_counts()
attack_types

plt.bar(attack_types.index, attack_types.values, color='blue', edgecolor='lightblue')
plt.xlabel('Tipos de ataque')
plt.ylabel('Quantidade de ataques')
plt.xticks(rotation=45)
plt.show()


# Quais as indústrias mais afetadas?
industries_affected = df['Target Industry'].value_counts()
industries_affected

plt.bar(industries_affected.index, industries_affected.values, color='green')
plt.xlabel('Indústrias')
plt.ylabel('Quantidade de ataques')
plt.xticks(rotation=45)
plt.show()


# Qual o total de perdas financeiras por ano?
financial_loss_per_year = df.groupby('Year').agg(
    FinancialLoss = ('Financial Loss (in Million $)', 'sum')
    )
financial_loss_per_year

plt.bar(financial_loss_per_year.index, financial_loss_per_year['FinancialLoss'], 
        color='orange')
plt.xlabel('Anos')
plt.ylabel('Perdas Financeiras (em milhões de dólares)')
plt.show()


# Análises por país

df_countries = df.groupby('Country').agg(
    AttackFrequency = ('Country', 'count'),
    MeanResolutionTime = ('Incident Resolution Time (in Hours)', 'mean'),
    MeanAffectedUsers = ('Number of Affected Users', 'mean'),
    TotalAffectedUsers = ('Number of Affected Users', 'sum'),
    FinancialLoss = ('Financial Loss (in Million $)', 'sum')
    )

AvgLossPerAttack = df_countries['FinancialLoss'] / df_countries['AttackFrequency']
df_countries['AvgLossPerAttack'] = AvgLossPerAttack

most_common_attack = df.groupby('Country')['Attack Type'].agg(lambda x: x.mode().iloc[0])
most_affected_industry = df.groupby('Country')['Target Industry'].agg(lambda x: x.mode().iloc[0])
most_common_attack_source = df.groupby('Country')['Attack Source'].agg(lambda x: x.mode().iloc[0])
most_explored_security_vulnerability = df.groupby('Country')['Security Vulnerability Type'].agg(lambda x: x.mode().iloc[0])
most_common_defense_mechanism = df.groupby('Country')['Defense Mechanism Used'].agg(lambda x: x.mode().iloc[0])


df_countries['MostCommonAttack'] = most_common_attack
df_countries['MostAffectedIndustry'] = most_affected_industry
df_countries['MostCommonAttackSource'] = most_common_attack_source
df_countries['MostExploredSecurityVulnerability'] = most_explored_security_vulnerability
df_countries['MostCommonDefenseMechanism'] = most_common_defense_mechanism

df_countries

# Países mais afetados?

df_countries_sorted = df_countries.sort_values(by='AttackFrequency', ascending=False)

plt.figure(figsize=(10, 6))  
plt.barh(df_countries_sorted.index, df_countries_sorted['AttackFrequency'], color='red')
plt.xlabel('Quantidade de ataques')
plt.ylabel('Países')
plt.title('Frequência de Ataques por País')
plt.gca().invert_yaxis() 
plt.show()

# Países com maiores prejuízos financeiros 

df_countries_sorted = df_countries.sort_values(by='FinancialLoss', ascending=False)

plt.barh(df_countries_sorted.index, df_countries_sorted['FinancialLoss'], color='blue')
plt.ylabel('Países')
plt.xlabel('Perdas Financeiras (em milhoes de dólares')
plt.xticks(rotation=45)
plt.gca().invert_yaxis() 
plt.show()

# Perda média por ataque por país 

df_countries_sorted = df_countries.sort_values(by='AvgLossPerAttack', ascending=False)

plt.barh(df_countries_sorted.index, df_countries_sorted['AvgLossPerAttack'], color='blue')
plt.xlabel('Países')
plt.ylabel('Perda Financeira Média (em milhoes de dólares')
plt.xticks(rotation=45)
plt.gca().invert_yaxis() 
plt.show()

# Média de usuários afetados por ataque por país

df_countries.sort_values('MeanAffectedUsers', ascending=True)['MeanAffectedUsers'].plot(kind='barh', figsize=(10, 8), color='skyblue')
plt.xlabel('Média de Usuários Afetados por Ataque')
plt.title('Média de Usuários Afetados por Ataque por País')
plt.tight_layout()
plt.show()
