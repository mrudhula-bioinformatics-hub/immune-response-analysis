{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b8382e45-024a-41ed-8387-9381a73135f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     Gene  Control  Infected\n",
      "0     IL6        5        25\n",
      "1     TNF        4        18\n",
      "2    IFNG        6        30\n",
      "3    IL10       10         8\n",
      "4  CXCL10        3        40\n",
      "5    CCL2        7        14\n",
      "6   STAT1        5        22\n",
      "7    IRF7        4        28\n",
      "     Gene  Control  Infected  Fold_change\n",
      "0     IL6        5        25     5.000000\n",
      "1     TNF        4        18     4.500000\n",
      "2    IFNG        6        30     5.000000\n",
      "3    IL10       10         8     0.800000\n",
      "4  CXCL10        3        40    13.333333\n",
      "5    CCL2        7        14     2.000000\n",
      "6   STAT1        5        22     4.400000\n",
      "7    IRF7        4        28     7.000000\n",
      "     Gene  Control  Infected  Fold_change\n",
      "0     IL6        5        25     5.000000\n",
      "1     TNF        4        18     4.500000\n",
      "2    IFNG        6        30     5.000000\n",
      "4  CXCL10        3        40    13.333333\n",
      "6   STAT1        5        22     4.400000\n",
      "7    IRF7        4        28     7.000000\n",
      "     Gene  Control  Infected  Fold_change\n",
      "4  CXCL10        3        40    13.333333\n",
      "7    IRF7        4        28     7.000000\n",
      "0     IL6        5        25     5.000000\n",
      "2    IFNG        6        30     5.000000\n",
      "1     TNF        4        18     4.500000\n",
      "6   STAT1        5        22     4.400000\n",
      "Mean Control: 5.5\n",
      "Mean Infected: 23.125\n",
      "\n",
      "--- Interpretation ---\n",
      "Genes like CXCL10, IRF7, IL6, and IFNG show high fold change, indicating strong immune activation.\n",
      "IL10 shows lower fold change, suggesting reduced anti-inflammatory response.\n",
      "Overall, the infected condition shows higher gene expression compared to control.\n"
     ]
    }
   ],
   "source": [
    "#Importing the data analysis library pandas\n",
    "import pandas as pd\n",
    "#commanding pandas to read our csv file\n",
    "#also naming the table as df\n",
    "df = pd.read_csv(\"immune_exe.csv\")\n",
    "print(df)\n",
    "#adding fold change as a column\n",
    "df[\"Fold_change\"] = df[\"Infected\"] / df[\"Control\"]\n",
    "print (df)\n",
    "#Now deleting the genes with low fold chnage\n",
    "high = df[df[\"Fold_change\"] > 3]\n",
    "print (high)\n",
    "#sorting the genes according to their fold change\n",
    "sorted_df = high.sort_values(by=\"Fold_change\", ascending=False)\n",
    "print(sorted_df)\n",
    "#calculating mean\n",
    "mean_Control = df[\"Control\"].mean()\n",
    "mean_Infected = df[\"Infected\"].mean()\n",
    "print(\"Mean Control:\", mean_Control)\n",
    "print(\"Mean Infected:\", mean_Infected)\n",
    "print(\"\\n--- Interpretation ---\")\n",
    "\n",
    "print(\"Genes like CXCL10, IRF7, IL6, and IFNG show high fold change, indicating strong immune activation.\")\n",
    "print(\"IL10 shows lower fold change, suggesting reduced anti-inflammatory response.\")\n",
    "print(\"Overall, the infected condition shows higher gene expression compared to control.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
