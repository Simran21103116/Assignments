


standard_deduction=10000;
depend_deduction=3000;
gross=input("Enter your gross income : ");
No_of_dependents=input("Enter the number of dependents : ");
taxable_income=int(gross)-int(standard_deduction)-(int(depend_deduction)+int(No_of_dependents));
tax=(float(taxable_income)*0.2);
print("Your tax is :");
print(float(tax));

