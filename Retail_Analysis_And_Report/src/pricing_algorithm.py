def calculate_recommended_price(row):
    """
    Five-Factor Dynamic Pricing Algorithm
    """
    # Step 1: Calculate Base Price
    target_margin = row['Target_Gross_Margin_%'] / 100
    base_price = row['Total_Cost'] / (1 - target_margin)
    
    # Step 2: Factor 1 - Competitive Positioning (-5% to +10%)
    if pd.notna(row['Avg_Competitor_Price']) and row['Avg_Competitor_Price'] > 0:
        price_ratio = row['Current_Price'] / row['Avg_Competitor_Price']
        if price_ratio > 1.15:  # Overpriced
            comp_factor = -0.05
        elif price_ratio > 1.10:  # Slightly high
            comp_factor = -0.03
        elif price_ratio > 0.95:  # At market
            comp_factor = 0.00
        elif price_ratio > 0.90:  # Slightly low
            comp_factor = 0.03
        elif price_ratio > 0.85:  # Underpriced
            comp_factor = 0.05
        else:  # Significantly underpriced
            comp_factor = 0.10
    else:
        comp_factor = 0.00
    
    adjusted_price = base_price * (1 + comp_factor)
    
    # Step 3: Factor 2 - Inventory Health (-8% to +8%)
    days_supply = row['days-of-supply']
    if days_supply > 120:  # Critical excess
        inv_factor = -0.08
    elif days_supply > 90:  # Excess
        inv_factor = -0.05
    elif days_supply > 60:  # High
        inv_factor = 0.00
    elif days_supply > 30:  # Healthy
        inv_factor = 0.00
    elif days_supply > 20:  # Low
        inv_factor = 0.05
    else:  # Critical low
        inv_factor = 0.08
    
    adjusted_price = adjusted_price * (1 + inv_factor)
    
    # Step 4: Factor 3 - Sales Velocity (-7% to +5%)
    velocity = row['Sales_Velocity']
    if velocity < 0.3:  # Very low
        vel_factor = -0.07
    elif velocity < 0.5:  # Low
        vel_factor = -0.04
    elif velocity < 3.0:  # Moderate
        vel_factor = 0.00
    elif velocity < 5.0:  # Strong
        vel_factor = 0.03
    else:  # High
        vel_factor = 0.05
    
    adjusted_price = adjusted_price * (1 + vel_factor)
    
    # Step 5: Factor 4 - Advertising Efficiency (-3% to +5%)
    acos = row['Avg_ACOS']
    if acos > 60:  # Very high ACOS
        acos_factor = 0.05
    elif acos > 50:  # High ACOS
        acos_factor = 0.03
    elif acos > 30:  # Moderate
        acos_factor = 0.00
    elif acos > 20:  # Efficient
        acos_factor = -0.02
    else:  # Very efficient
        acos_factor = -0.03
    
    adjusted_price = adjusted_price * (1 + acos_factor)
    
    # Step 6: Factor 5 - Returns Impact (-3% to +10%) [NEW]
    return_rate = row['Return_Rate']
    if return_rate > 10:  # Very high returns
        return_factor = 0.10
    elif return_rate > 7:  # High returns
        return_factor = 0.07
    elif return_rate > 4:  # Moderate returns
        return_factor = 0.03
    elif return_rate > 2:  # Low returns
        return_factor = 0.00
    else:  # Very low returns
        return_factor = -0.03
    
    adjusted_price = adjusted_price * (1 + return_factor)
    
    # Step 7: Apply maximum change limit (15%)
    max_price = row['Current_Price'] * 1.15
    min_price = row['Current_Price'] * 0.85
    recommended_price = np.clip(adjusted_price, min_price, max_price)
    
    # Step 8: Validate minimum margin
    min_margin = row['Minimum_Acceptable_Margin_%'] / 100
    min_acceptable_price = row['Total_Cost'] / (1 - min_margin)
    recommended_price = max(recommended_price, min_acceptable_price)
    
    # Store factors for analysis
    factors = {
        'base_price': base_price,
        'comp_factor': comp_factor,
        'inv_factor': inv_factor,
        'vel_factor': vel_factor,
        'acos_factor': acos_factor,
        'return_factor': return_factor,
        'recommended_price': recommended_price
    }
    
    return factors
