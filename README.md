# 🚗 EV Price Prediction Project (Machine Learning)

This project focuses on exploring and analyzing an **Electric Vehicle (EV) dataset** that already includes **both specifications and price details**.  
The ultimate goal is to use this data to build a **machine learning model that predicts EV prices** based on battery capacity, range, performance, and features.

This repository is organized in **weekly progress format**, starting with dataset understanding and EDA.

---

## 📊 Dataset Information

**Dataset Source:** Provided dataset (EV specifications + prices)  
**Dataset Format:** CSV

| Feature | Description |
|--------|-------------|
| brand | Manufacturer name |
| model | Vehicle model |
| battery_capacity_kWh | Battery capacity (kWh) |
| range_km | Realistic driving range in km |
| efficiency_wh_per_km | Energy consumption |
| top_speed_kmh | Maximum speed |
| seats | Number of seats |
| drivetrain | RWD / FWD / AWD |
| segment | Vehicle category (Hatchback/SUV/Sedan etc.) |
| price_in_rupees (or similar column) | **Target variable** |

---

## 🗂 Folder Structure

EV_Price_Prediction_Project/
│
├── data/
│ └── electric_vehicles_data.csv
│
├── notebooks/
│ └── week1_data_exploration.ipynb
│
└── README.md


---

## ✅ Week 1 Work Completed

- Imported the dataset into Jupyter Notebook / VS Code
- Displayed dataset shape and columns
- Checked for null values
- Performed initial descriptive statistics
- Observed correlations between price and key features
- Saved notebook inside `notebooks/` folder

---

## 🛠 Tools Used

| Tool | Purpose |
|------|---------|
| Python | Data processing & model development |
| Pandas | Data manipulation |
| NumPy | Mathematical operations |
| Matplotlib / Seaborn | Exploratory visualizations |
| Jupyter Notebook / VS Code | Development environment |

---

## 🧠 Learning Objective

- Understand how EV specifications influence market pricing.
- Prepare cleaned data for price prediction modeling.
- Learn the ML workflow step-by-step (EDA → Feature Selection → Model Training).

---

## 🚀 Next Week (Week 2 Plan)

- Remove irrelevant or correlated features
- Handle missing values (if any)
- Feature scaling / encoding
- Begin model selection (Linear Regression / Random Forest)

---

## ✨ Author

**Malavika Das**  
GitHub: `Malavika_08`

