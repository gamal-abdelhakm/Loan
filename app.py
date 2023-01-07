import streamlit as st
import joblib 
import pandas as pd

Inputs = joblib.load("Inputs.pkl")
Model = joblib.load("Model.pkl")

def predict(Gender, Married, Dependents, Education, Self_Employed,ApplicantIncome, CoapplicantIncome, LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
#def predict(Gender, Married, Dependents, Education, Self_Employed,Credit_History,Property_Area):
    test_df = pd.DataFrame(columns = Inputs)
    test_df.at[0,"Gender"] = Gender
    test_df.at[0,"Married"] = Married
    test_df.at[0,"Dependents"] = Dependents
    test_df.at[0,"Education"] = Education
    test_df.at[0,"Self_Employed"] = Self_Employed
    test_df.at[0,"ApplicantIncome"] = float(ApplicantIncome)
    test_df.at[0,"CoapplicantIncome"] = float(CoapplicantIncome)
    test_df.at[0,"LoanAmount"] = float(LoanAmount)
    test_df.at[0,"Loan_Amount_Term"] = float(Loan_Amount_Term)
    test_df.at[0,"Credit_History"] = float(Credit_History)
    test_df.at[0,"Property_Area"] = Property_Area
    result = Model.predict(test_df)[0]
    return result
    
def main():
    st.title("Loan App")
    Gender = st.selectbox("Gender" , ['Male', 'Female'])
    Married = st.selectbox("Married" , ['Yes', 'No'])
    Dependents = st.selectbox("Dependents" , ['0', '1', '2', '3+'])
    Education = st.selectbox("Education" , ['Graduate', 'Not Graduate'])
    Self_Employed = st.selectbox("Self_Employed" , ['Yes', 'No'])
    ApplicantIncome = st.slider("ApplicantIncome" , min_value=0, max_value=81000, value=0, step=1)
    CoapplicantIncome = st.slider("CoapplicantIncome" , min_value=0, max_value=41667, value=0, step=1)
    LoanAmount = st.slider("LoanAmount" , min_value=0, max_value=1000, value=0, step=1)
    Loan_Amount_Term = st.slider("Loan_Amount_Term" , min_value=12, max_value=480, value=12, step=12)
    Credit_History = st.selectbox("Credit_History" , [0, 1])
    Property_Area = st.selectbox("Property_Area" , ['Urban', 'Rural', 'Semiurban'])    
    
    if st.button("Predict"):
        result = predict(Gender, Married, Dependents, Education, Self_Employed,ApplicantIncome,CoapplicantIncome, LoanAmount, Loan_Amount_Term,Credit_History,Property_Area)
        #result = predict(Gender, Married, Dependents, Education, Self_Employed,Credit_History,Property_Area)
        label = ["Fail","Success"]
        st.text("The output is {}".format(label[result]))

    
if __name__ == '__main__':
    main()
    
    
