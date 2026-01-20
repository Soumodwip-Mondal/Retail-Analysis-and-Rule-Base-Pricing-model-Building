# 🌱 Retail Analysis & Dynamic Pricing Model

A data-driven pricing optimization project for an eco-friendly tableware business, addressing systematic underpricing through a rule-based dynamic pricing algorithm.

[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Complete-success)](https://github.com/Soumodwip-Mondal/Retail-Analysis-and-Rule-Base-Pricing-model-Building)

## 📊 Project Overview

This project solves a critical profitability crisis where strong performance metrics (6.33x ROAS) masked systematic underpricing and hidden costs. Using comprehensive data analysis and a multi-factor pricing algorithm, we increased net margins by 14 percentage points.

**Key Results:**
- Average Price Increase: +19.6%
- Net Margin Improvement: +14.0 pp
- Monthly Profit Impact: +$81,451 (+110.5%)
- SKUs Below Target: 49 → 45

---

## 🔍 The Problem

An eco-friendly tableware company faced hidden profitability issues despite $1.3M+ revenue:

### Critical Issues

**1. Systematic Underpricing**
- 98% of SKUs operating 23-33 points below target margins
- 88% priced below competitors despite premium positioning
- No data-driven pricing framework

**2. Hidden Costs**
- FBA fees consuming 47% of total costs
- Returns (5.9% average) reducing margins from 10.0% to 4.1%
- 76% of products with excess inventory (>60 days supply)

**3. Lack of Integration**
- Advertising performance (ROAS, ACOS) not factored into pricing
- Competitive intelligence ignored
- Returns data not considered in margin calculations

---

## 💡 The Solution

### Multi-Factor Dynamic Pricing Algorithm

A rule-based pricing model that balances five key business dimensions:

**Base Formula:**
```
Base Price = Total Cost / (1 - Target Margin%)
Recommended Price = Base Price × Competitive Factor × Inventory Factor × 
                    Velocity Factor × Ad Factor × Return Factor
```

### The Five Pricing Factors

**1. Competitive Positioning (±3-5%)**
- Maintains market position while capturing value
- Overpriced products: -3-5% discount
- Underpriced products: +3-5% increase
- Target: 90-110% of market average

**2. Inventory Health (±5-8%)**
- Excess inventory (>90 days): -5-8% to accelerate turnover
- Low stock (<30 days): +5-8% for scarcity pricing
- Reduces carrying costs and stockout risks

**3. Sales Velocity (±4-7%)**
- High demand (>5 units/day): +5% premium
- Low velocity (<0.3 units/day): -7% to stimulate demand
- Aligns price with demand intensity

**4. Advertising Efficiency (±2-5%)**
- High ACOS (>50%): +3-5% for margin recovery
- Low ACOS (<20%): -2-3% for competitive pricing
- Maintains profitable customer acquisition

**5. Returns Impact (±3-10%)**
- High returns (>7%): +5-10% margin protection
- Low returns (<4%): -3% discount
- Protects against return-related erosion

### Safety Mechanisms
- **15% maximum price change** to prevent market shock
- **20% minimum margin floor** for sustainability
- Phased rollout with continuous monitoring

---

## 🧮 Algorithm Example

**SKU: 10" Square Plates (Pack of 50)**

**Input Data:**
- Total Cost: $35.53
- Current Price: $42.99
- Competitor Avg: $51.20
- Return Rate: 6.8%
- ACOS: 10.1% (efficient)

**Calculation Steps:**
1. Base Price: $35.53 / 0.65 = $54.66
2. Competitive (+5%): $54.66 × 1.05 = $57.39
3. Inventory (0%): $57.39 × 1.00 = $57.39
4. Velocity (+2%): $57.39 × 1.02 = $58.54
5. ACOS (-3%): $58.54 × 0.97 = $56.78
6. Returns (+5%): $56.78 × 1.05 = $59.62
7. Apply 15% cap: $42.99 × 1.15 = **$49.44**

**Result:** +15% increase, improving margin while staying competitive

---

## 📁 Project Structure

```
├── Retail_Analysis_And_Report/
│   └── Dynamic Pricing Model And Retail Analysis Report.pdf
├── data/
│   ├── Historical_Sales.csv
│   ├── Advertising_Performance.csv
│   ├── Inventory_Health.csv
│   ├── Competitive_Intelligence.csv
│   └── Returns_Data.csv
├── notebooks/
│   └── pricing_analysis.ipynb
└── src/
    ├── pricing_algorithm.py
    └── data_processing.py
```

---

## 📂 Datasets

### Data Sources & Description

**1. Historical Sales Data** (`Historical_Sales.csv`)
- **Records:** 4,243 transactions
- **Fields:** Product sessions, page views, units ordered, revenue, conversion rates
- **Purpose:** Analyze sales patterns and velocity trends

**2. Advertising Performance** (`Advertising_Performance.csv`)
- **Records:** 12,777 advertising campaigns
- **Fields:** Impressions, clicks, conversions, ROAS, ACOS, ad spend
- **Purpose:** Evaluate advertising efficiency and customer acquisition costs

**3. Inventory Health** (`Inventory_Health.csv`)
- **Records:** 50 SKUs with real-time inventory metrics
- **Fields:** Inventory levels, days of supply, weeks of cover, sell-through rates, storage metrics
- **Purpose:** Identify excess inventory and stockout risks

**4. Competitive Intelligence** (`Competitive_Intelligence.csv`)
- **Records:** 50 competitor product comparisons
- **Fields:** Competitor average price, minimum price, maximum price, market positioning
- **Purpose:** Benchmark pricing against market standards

**5. Cost Structure** (`Cost_Structure.csv`)
- **Records:** 50 SKUs with complete cost breakdown
- **Fields:** Product cost, FBA fees, storage fees, handling costs, total cost
- **Purpose:** Calculate base prices and margin requirements

**6. Returns Data** (`Returns_Data.csv`)
- **Records:** 50 SKUs with 90-day return tracking
- **Fields:** Units sold, units returned, return rate, return reasons
- **Purpose:** Adjust pricing for return-related margin erosion

### Data Overview

| Dataset | Records | Time Period | Key Metrics |
|---------|---------|-------------|-------------|
| Historical Sales | 4,243 | Historical | Units, Revenue, Conversions |
| Advertising | 12,777 | Campaign-level | ROAS (avg 6.33x), ACOS |
| Inventory | 50 SKUs | Real-time | Days of supply (avg 78) |
| Competitive | 50 SKUs | Current | Market price benchmarks |
| Cost Structure | 50 SKUs | Current | Total cost (avg $25.81) |
| Returns | 50 SKUs | 90-day | Return rate (avg 5.9%) |

---

## 🛠️ Technologies

- **Python 3.8+** - Core language
- **Pandas & NumPy** - Data analysis
- **Matplotlib/Seaborn** - Visualization
- **Jupyter Notebook** - Analysis environment

---

## 📈 Implementation Plan

**Phase 1 (Weeks 1-2):** Test 5 high-ROAS SKUs, establish monitoring  
**Phase 2 (Weeks 3-5):** Roll out Tier 1 & 2 SKUs (35 total)  
**Phase 3 (Weeks 6-8):** Complete rollout, optimize based on data

**Success Metrics:** Conversion decline <10%, ROAS >4.0, margin improvement >8%

---

## 📊 Expected Impact

| Metric | Current | Projected | Improvement |
|--------|---------|-----------|-------------|
| Monthly Revenue | $15,051 | $17,438 | +15.9% |
| Monthly Profit | $797 | $3,506 | +339.8% |
| Average Margin | 11.87% | 37.5% | +25.6 pp |

---

## 🔑 Key Takeaways

1. **Data-Driven Framework** - Replaces reactive pricing with systematic decisions
2. **Multi-Factor Model** - Balances competition, inventory, velocity, ads, and returns
3. **Risk-Managed** - Phased rollout with change caps and validation
4. **Scalable** - Framework adapts as business evolves

---

## 👥 Author

**Soumodwip Mondal** - Data Analysis & Algorithm Development

---

## 📄 License

Available for educational and reference purposes.

---

⭐ **Star this repo if you found it helpful!**
