import pandas as pd




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tecnologias = {"Cursos":["Java","Python","C++"],
                    "Precios":[800, 900, 700],"Duracion":["90dias","60 dias", "40dias"],
                    "Descuento":[100,150,100]
                  }
    df = pd.DataFrame(tecnologias)
    print(df)

   # print()
   # print()
   # df = pd.read_csv("DataChurn.csv")
   # print(df.head(5))

   # print()
   #  print()
    #Max(), retorna el valor máximo de una variable:
   # df2 = df[["PaymentMethod", "TotalChargesRg"]][df.TotalChargesRg == df["TotalChargesRg"].max()]
   # print(df2)

    #print()
    #print()
# Podemos filtrar los valores de una  variable en función a su valor:
   # df4 = df.loc[:, ["Churn", "TotalChargesRg"]]
   # print(df4)
   # df5 = df4.loc[df4.loc[:, "Churn"] == "Yes"]
   # print(df5)
   # print()
   # print()

