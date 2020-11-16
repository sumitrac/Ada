'''
This program output everything progam ask for and work well in calculating all outcomes. 
'''

#Assign variables
single_month = 7.00
three_months = 18.00
ad_free = 2.00
video_on_demand = 27.99

#list to store data from accounts
months_susbscribed = []
ad_free_months = []
video_on_demand_purchases = []
totals = []

def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    """
    Parameters:
      months_subscribed: How many months each account purchased.
      ad_free_months: How many months each account paid for ad free viewing.
      video_on_demand_purchases: How many Videos on Demand each account purchased.
    """
    print("Welcome to the Ada+ Account Dashboard\n")
    
    counter = 1
    all_accounts = 0
    Premium_content = 0

    #section for months_susbscribed
    for i in range(len(months_subscribed)):
        total = 0
        #print("Account",counter)
        number_of_three_months = (months_subscribed[i]) // 3
        number_of_single_months = (months_subscribed[i]) % 3 
        months = number_of_three_months * three_months + number_of_single_months * single_month
        total = total+months
        #print(months , "from monthly subscription fees")

    #section for ad free months 
        ad = int(ad_free_months[i]) * ad_free
        Premium_content = Premium_content+ad
        total = total+ad
        #print(ad , " from Ad-free upgrades")
    
    #section for video on demand 
        video = int(video_on_demand_purchases[i]) * video_on_demand
        Premium_content = Premium_content + video
        total = total + video
        totals.append(total)
        all_accounts = all_accounts + total
        #print( video , " from Video on Demand purchases")
        
#prints summary of each accounts 
        print("Account " + str(counter) + " made $" + format(total, '.2f') + " total")
        print(">>> $" + format(months, '.2f')  + " from monthly subscription fees")
        print(">>> $" + format(ad, '.2f') + " from Ad-free upgrades")
        print(">>> $" + format(video, '.2f') + " from Video on Demand purchases\n")
        counter = counter + 1

#prints account summary 
    print("Combined all accounts made $" + format(sum(totals), '.2f') + " total")
    print("Premium content (Ad-free watching and Video on Demand) made $" + format(Premium_content,'.2f') + " total\n")
    print("$" + format(max(totals),'.2f') + " was the most earned by any single account")
    
    max_value = max(totals)
    #1, #3
    max_indexes = [f'#{idx + 1}' for idx in range(len(totals)) if totals[idx] == max_value]
    print("The accounts that earned the most were: ", end='')
    print(', '.join(max_indexes))

##Taking input for three Accounts
#months_subscribed
print("months_subscribed:")
months_susbscribed.append(int(input(" ")))
months_susbscribed.append(int(input(" ")))
months_susbscribed.append(int(input(" ")))

#ad_free_months
print("ad_free_months:")
ad_free_months.append(int(input(" ")))
ad_free_months.append(int(input(" ")))
ad_free_months.append(int(input(" ")))

#video_on_demand_purchases
print("video_on_demand_purchases:")
video_on_demand_purchases.append(int(input(" ")))
video_on_demand_purchases.append(int(input(" ")))
video_on_demand_purchases.append(int(input(" ")))

subscription_summary(months_susbscribed, ad_free_months, video_on_demand_purchases)
      
