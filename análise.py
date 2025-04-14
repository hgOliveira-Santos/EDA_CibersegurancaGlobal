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


# Quais os tipos de ataque mais comuns?
attack_types = df['Attack Type'].value_counts()
attack_types

plt.bar(attack_types.index, attack_types.values, color='blue', edgecolor='lightblue')
plt.xticks(rotation=45)
plt.show()


# Quais as indústrias mais afetadas?
industries_affected = df['Target Industry'].value_counts()
industries_affected

plt.bar(industries_affected.index, industries_affected.values, color='green')
plt.xticks(rotation=45)
plt.show()


# Qual o total de perdas financeiras por ano:?
financial_loss_per_year = df.groupby('Year').agg(
    FinancialLoss = ('Financial Loss (in Million $)', 'sum')
    )
financial_loss_per_year

plt.bar()

