
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
pokemon_df=pd.read_csv("Pokemon.csv")
pokemon_df["Sp_Atk"]=pokemon_df["Sp. Atk"]
pokemon_df["Sp_Def"]=pokemon_df["Sp. Def"]
pokemon_df["Type 2"]= pokemon_df['Type 2'].apply(lambda x: "None" if pd.isna(x) else x)
def get_pokemon(t1,t2):
    sorted_pokemon=pokemon_df[(pokemon_df["Type 1"]==t1)&(pokemon_df["Type 2"]==t2)][["Name", "Total","Generation"]].head(10)
    return sorted_pokemon.to_dict(orient="records")

def get_top_10(stat):
    df_name=pokemon_df.sort_values(stat,ascending=False).head(10)[["Name", "Total","Generation",stat]]
    return df_name.to_dict(orient="records")

def get_stat():
    stat_df=pokemon_df[["HP","Attack","Defense","Sp_Atk","Sp_Def","Speed"]]
    return  stat_df.to_dict(orient="records")
def gen():
    gen_df=pokemon_df.groupby("Generation")[["#"]].count()
    return gen_df.to_dict(orient="records")


def type_():
    type_df=pokemon_df[["Type 1","Type 2"]]
    return type_df


if __name__=="__main__":
    # print(get_pokemon("Grass","Poison",1))
    # print(get_top_10("HP"))#not working as planned
    # print(get_stat())
    # print(type_())
    df=type_()
    # print(pokemon_df.isnull().sum())
    # print(gen())
    # print(pokemon_df.columns)
    # df=get_top_10("Sp. Atk")
    # df = pd.DataFrame(df)
    # sns.barplot(df.set_index("Name")["Sp. Atk"])
    plt.show()
