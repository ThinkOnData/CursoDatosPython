BaseDeDatos = pd.read_excel(Direccion_De_Base_De_Datos)
BaseDeDatos.index = BaseDeDatos["n�m_corre"]
BaseDeDatos.drop("n�m_corre", axis=1, inplace=True)
BaseDeDatos.head()