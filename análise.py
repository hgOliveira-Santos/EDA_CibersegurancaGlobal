# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 11:40:06 2025

@author: Hgsann
"""

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

# Quais os países mais afetados?

plt.bar(df_countries.index, df_countries['AttackFrequency'], color='red')
plt.xlabel('Países')
plt.ylabel('Quantidade de ataques')
plt.xticks(rotation=45)
plt.show()

# Quais países tiveram maiores prejuízos financeiros 

plt.bar(df_countries.index, df_countries['FinancialLoss'], color='blue')
plt.xlabel('Países')
plt.ylabel('Perdas Financeiras (em milhoes de dólares')
plt.xticks(rotation=45)
plt.show()

