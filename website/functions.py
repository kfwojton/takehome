
    
# This function takes in raw post django data and outputs the allocation. This functions works by prorating the allocation amount based on the requested amount and the historical amounts; with people who hav
# This function defines, primary investors, and secondary investors.
# Primary Investors are people who get to invest 100% of their requested amount 
# Secondary Investors are people who have to take less then 100% of their requested amount 
# Allocated Amount is the amount of money that is allocated to the investor based on a proration of % of previous holdings. 

# Case 1: If the round is undersubscribed all investors are primary investors 
# Case 2: If the round is oversubscribed, all investors whose requested amount is less than or equal to their "allocated amount" are primary investors. All others will be secondary investors; and will receive a prorated amount of the remaining funds. This is because the requested amount of the primary investors is less than their allocated amount thus they get 100% of their requested amount.  

# Algorithm Considerations: The difficult part about this algorightm is the case where it is over subscribed and primary investors want to invest less than their allocated amount. As such they would not be receiving their full allocated amounts, thus the remaining amount would be prorated to the secondary investors. The alogrithm below takes these primary investors out of the pool; and allocates the reaminging amount of the offer (after primary investors) to the secondary investors based on their historical amounts. 

# Contemplated Improvements: It is of note; that this algortithm could be refined further by making a recursive algorithm that after the first round of primary investors are taken out of the pool, then with this new pool take out newly identified primary investors and perform that until all investors are exhausted. This likely would be a much more complex algorithm; 
from core.models import Logs

def transform_to_allocation_input(input_data, user):
    # Intitialize some data structures 
    final_data = {}
    input_data = dict(input_data)
    target_fundraise = int(input_data["allocation_amount"][0])
    final_data["target_fundraise"] = target_fundraise
    previous_holdings = 0 
    investors = []
    second_list = []
    
    # Extract investor names and normalize data
    investor_names = input_data["investor_name"]
    requested_amounts = [int(a) for a in input_data["requested_amount"]]
    historical_amounts = [int(a) for a in input_data["average_amount"]]
    
    total_historical_amount = sum(historical_amounts)
    total_requested_amount = sum(requested_amounts)

    #check to see if the round is undersubscribed, if yes make the total amount fundraised equal to the total subscription not the target fundraised amount.  
    if target_fundraise > total_requested_amount: 
        total_amount_fundraised = total_requested_amount
        post_money_valuation = total_historical_amount + total_requested_amount
        final_data['post_money_valuation'] = post_money_valuation
        
    else: 
        total_amount_fundraised = target_fundraise
        post_money_valuation = total_historical_amount + target_fundraise
        final_data['post_money_valuation'] = post_money_valuation

    # set a total which we subtract from as we go through the list; providing a remaining allocation to 2nd degree investors. 
    running_total = total_amount_fundraised
    final_data["total_amount_fundraised"] = running_total
    for a in range(len(investor_names)):
        
        final_amount = target_fundraise * historical_amounts[a]/total_historical_amount
        # first go through the list and pull out all of the primary investors 
        if final_amount > requested_amounts[a]: 
            previous_holdings += historical_amounts[a]
            running_total -= requested_amounts[a]
            rounded_requested_amount = round((requested_amounts[a]),2)
            pre_money_ownership = int(historical_amounts[a] / total_historical_amount * 100)            
            post_money_holdings = round(historical_amounts[a] + requested_amounts[a],2)
            rounded_post_money_ownership = int(post_money_holdings / post_money_valuation * 100)


            investors.append({"name":  investor_names[a], 
                        "previous_holdings": historical_amounts[a], 
                        "requested_amount": requested_amounts[a], 
                        "percent_of_previous_round":pre_money_ownership, 
                        "final_amount": rounded_requested_amount, 
                        "post_money_ownership": rounded_post_money_ownership,
                        "post_money_holdings": post_money_holdings
                        
                        })
        else: 
            second_list.append({"name": investor_names[a],
                                "requested_amount" : requested_amounts[a],
                                "historical_amount" : historical_amounts[a] }) 
            
    total_remaining_historical_amount = sum([a['historical_amount'] for a in second_list])
    # Then allocate the remaining amount to secondary investors on the prorated amount of remaining funds and historical data. 
    for a in second_list: 
        previous_holdings += a['historical_amount']
        final_amount = running_total *  a['historical_amount']/total_remaining_historical_amount
        post_money_holdings = round(a['historical_amount'] + a['requested_amount'],2)
        rounded_post_money_ownership = int(post_money_holdings / post_money_valuation * 100)
        
        investors.append({"name": a['name'], 
                        "previous_holdings": a['historical_amount'], 
                        "requested_amount": a['requested_amount'], 
                        "final_amount": round(final_amount,2) , 
                        "percent_of_previous_round": round(a['historical_amount'] / total_historical_amount * 100,2), 
                        "post_money_ownership": round((a['historical_amount'] + final_amount) / post_money_valuation * 100,2), 
                        "amount_fundraised" : total_amount_fundraised,
                        'post_money_holdings' : round(a['historical_amount'] +final_amount,2),
                        })
        
    final_data["pre_money_valuation"] = total_historical_amount
    final_data["investor_amounts"] = investors
    final_data["total_amount_requested"] = total_requested_amount
    
    
    if Logs.objects.filter(log = 'POST DATA:' + str(input_data) + ' \n FINAL DATA:' + str(final_data)):
        #already loged this log. Prevent extra un neeed logs. 
        pass
    else: 
        if user.is_authenticated:
            Logs.objects.create( log = 'POST DATA:' + str(input_data) + ' \n FINAL DATA:' + str(final_data), 
                                user = user)
        else: 
            Logs.objects.create( log = 'POST DATA:' + str(input_data) + ' \n FINAL DATA:' + str(final_data)
            )
    return final_data


# Note: This is the improve recursive function that is not used, but could be an alternative to the solution. In my opinion this solution is more complex, adds more run time, and is less readable. Should there be interest from stakeholders I would likely implement this solution but for now the original solution represents a fair and equitable solution. I do believe this recursive solution is elegant, but not the most efficient solution for the problem at hand. 

# def allocate_shares_recursive(investors, available_shares):
#     # Base case: if there are no available shares, return an empty allocation
#     if available_shares <= 0:
#         return {}

#     # Calculate total prorated ownership
#     total_prorated_ownership = sum(investor[1] for investor in investors)

#     # Calculate allocation for each investor
#     allocation = {}
#     remaining_investors = []
#     for investor, ownership in investors:
#         if total_prorated_ownership == 0:
#             # If total prorated ownership is 0, allocate shares evenly
#             allocation[investor] = available_shares // len(investors)
#         else:
#             # Calculate prorated shares for each investor
#             prorated_shares = min(available_shares, int(ownership / total_prorated_ownership * available_shares))
#             allocation[investor] = prorated_shares

#         # Update available shares
#         available_shares -= allocation[investor]

#         # If the investor's request is fully satisfied, remove them from the list
#         if allocation[investor] == ownership:
#             continue
#         else:
#             remaining_investors.append((investor, ownership - allocation[investor]))

#     # Recursive call for remaining investors and remaining shares
#     remaining_allocation = allocate_shares(remaining_investors, available_shares)

#     # Merge allocations
#     allocation.update(remaining_allocation)

#     return allocation

# # Example usage:
# investors = [("Investor A", 0.3), ("Investor B", 0.2), ("Investor C", 0.5)]
# available_shares = 1000

# allocation = allocate_shares(investors, available_shares)
# print("Final Allocation:")
# for investor, shares in allocation.items():
#     print(f"{investor}: {shares} shares")