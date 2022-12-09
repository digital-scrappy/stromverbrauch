# preis_pro_kwh = 30.93
preis_pro_kwh = 43.48
preis_pro_wh = preis_pro_kwh / 1000

print(f"preis pro watt stunde = {preis_pro_wh}")

min_wh = 6
max_wh = 9

min_month_wh = min_wh * 30
max_month_wh = max_wh * 30

print(f"preis für jeden tag eine stunde pro monat min = {min_month_wh * preis_pro_wh / 100} €")
print(f"preis für jeden tag eine stunde pro monat max = {max_month_wh * preis_pro_wh / 100} €")

avg_kwh_pa = 200 
avg_kwh_pm = avg_kwh_pa / 12 


print(f"preis pro monat für waschen min = {avg_kwh_pm * preis_pro_kwh / 100} €")

min_kwh_pa = 109
max_kwh_pa = 253

min_kwh_pm = min_kwh_pa / 12
max_kwh_pm = max_kwh_pa / 12


print(f"preis pro kühlschrank pro monat min = {min_kwh_pm * preis_pro_kwh / 100} €")
print(f"preis pro kühlschrank pro monat max = {max_kwh_pm * preis_pro_kwh / 100} €")

avg_kwh_pl = 0.12


print(f"preis für 1 liter wasser im wasserkocher kochen = {avg_kwh_pl * preis_pro_kwh / 100} €")
